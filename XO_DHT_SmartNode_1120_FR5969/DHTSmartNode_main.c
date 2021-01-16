#include <msp430fr5969.h>
#include <NodeConfig.h>

#define NodeID          2
#define DHT_TYPE        22
#define COLLECT_TIME    300
#define Volt_scale      0.34

typedef struct DHT_Value {
    unsigned short Humi_H;
    unsigned short Humi_L;
    unsigned short Temp_H;
    unsigned short Temp_L;
    unsigned int CRC;
} DHT_Value;

char dataOut[13] = "";                          // Send Data
char DHT_rawData[40] = "";                      // Source Data
char Uart_Tx_index = 0;
unsigned int TAtimer_count = 0;                 // Send Time

#pragma PERSISTENT(dataOut)
#pragma PERSISTENT(DHT_rawData)

char DHT_Initialize(void);
void DHT_readData(char *);
char DHT_countData(char *,DHT_Value *);
void Set_And_Wait_TimerA(unsigned int);
void PacketPrepair(DHT_Value *);

int main(void) {
    // stop watchdog timer

    WDTCTL = WDTPW | WDTHOLD;
	// Initialize All pins
	Pin_Initialize();
	// Disable LOCKLPM5
	PM5CTL0 &= ~LOCKLPM5;
	// System Clock 1Mhz
	Clock_Setting();
	// UART0 TX Transfer Channel
	UCA0_TX_Init();
	// Initialize Node Infomation

	TAtimer_count = COLLECT_TIME - 5;

    TA0CTL |= TASSEL__ACLK | ID__1 | MC__UP;
    TA0CCTL0 |= CCIE;
    TA0R = 0;
    TA0CCR0 = 0x7FFF;

    /*
     *  1 TimerA Cycle ~= 30us
     */
    __bis_SR_register(GIE | LPM3_bits);
}

#pragma vector = TIMER0_A0_VECTOR
__interrupt void TA0_ISR (void) {
    if(TAtimer_count < COLLECT_TIME)
        TAtimer_count++;
    else {
        TA0CCTL0 &= ~CCIE;
        TAtimer_count = 0;
        DHT_Value dhtValue;

        P3DIR |= BIT7;
        P3OUT |= BIT7;                      // Enable DHT LDO

        if(DHT_Initialize()) {
           DHT_readData(DHT_rawData);
        }
        __delay_cycles(100000);             // Wait 100 ms
        P3OUT &= ~BIT7;                     // Disable DHT LDO
        P3DIR &= ~BIT7;

        __delay_cycles(100000);             // Wait 100 ms
        GetVolt(Volt_scale);                // Get SystemVolt

        P3DIR |= BIT6;
        P3OUT |= BIT6;                      // Enable HC12 LDO

        __delay_cycles(500000);             // Wait 500 ms
        if(DHT_countData(DHT_rawData,&dhtValue)) {
            PacketPrepair(&dhtValue);
            Uart_Tx_index = 0;                  // Clear Tx Index
            UCA0IE |= UCTXCPTIE;                // Enable Tx Interrupt
            UCA0TXBUF = dataOut[Uart_Tx_index];     // Send DataOut Data
            Uart_Tx_index++;
            UCA0IFG &= ~UCTXCPTIFG;
        }
        TA0CCTL0 |= CCIE;                       // restart Timer count
    }
}

#pragma vector = USCI_A0_VECTOR
__interrupt void HC12_TX_ISR (void) {
    if(Uart_Tx_index == 12) {
        __delay_cycles(250000);
        UCA0IE &= ~UCTXCPTIE;                   // Disable Tx Interrupt
        P3OUT &= ~BIT6;                         // Disable HC12 LDO
        P3DIR &= ~BIT6;
    }
    else {
        UCA0TXBUF = dataOut[Uart_Tx_index];     // Send DataOut Data
        Uart_Tx_index++;                        // Switch To Next bit
        UCA0IFG &= ~UCTXCPTIFG;
    }
}

void Set_And_Wait_TimerA(unsigned int counter) {
    TA2R = 0;
    TA2CCR0 = TA2R + counter;
    while(TA2CCR0 > TA2R);
}

char DHT_Initialize(void) {
    TA2CTL |= TASSEL__ACLK | ID__1 | MC__CONTINUOUS;
    TA2R = 0;
    volatile unsigned int i;
    P4DIR |= BIT0;                      // Switch P4.0 to Output
    P4OUT |= BIT0;                      // Make P4.0 Default Status
    for(i=0;i<5;i++)                    // Wait 5s
        Set_And_Wait_TimerA(32768);
    P4OUT &= ~BIT0;                     // Pull Down P4.0
    if(DHT_TYPE == 11)
        Set_And_Wait_TimerA(667);       // Wait 20000 us
    else
        Set_And_Wait_TimerA(40);        // Wait 1200 us
    P4OUT |= BIT0;                      // Pull UP P4.0
    Set_And_Wait_TimerA(1);             // Wait 30 us
    P4DIR &= ~BIT0;                     // Switch P4.0 to Input
    Set_And_Wait_TimerA(4);             // Wait 120us to let DHT11/22 Singal Up
    if((P4IN & BIT0) == BIT0) {
       while((P4IN & BIT0) == BIT0);    // Wait DHT Signal Down
       return 1;
    }
    return 0;
}

void DHT_readData(char *src) {
    unsigned char i;
    for(i=0;i<40;i++) {
        while((P4IN & BIT0) != BIT0);
        Set_And_Wait_TimerA(1);
        if ((P4IN & BIT0) == BIT0) {
            // If Rise up over 30us
            src[i] = 1;
            while((P4IN & BIT0) == BIT0);
        }
        else {
            // If Rise up less than 30us
            src[i] = 0;
        }
    }
    TA2CTL |= TASSEL__ACLK | ID__1 | MC__STOP;
}

char DHT_countData(char *raw,DHT_Value *src) {
    unsigned int i;
    // Humi_H
    src->Humi_H = 0;
    for(i=0;i<8;i++)
        src->Humi_H += raw[i] << (7 - i);
    // Humi_L
    src->Humi_L = 0;
    for(i=0;i<8;i++)
        src->Humi_L += raw[8+i] << (7 - i);
    // Temp_H
    src->Temp_H = 0;
    for(i=0;i<8;i++)
        src->Temp_H += raw[16+i] << (7 - i);
    // Temp_L
    src->Temp_L = 0;
    for(i=0;i<8;i++)
        src->Temp_L += raw[24+i] << (7 - i);
    // CRC
    src->CRC = 0;
    for(i=0;i<8;i++)
        src->CRC += raw[32+i] << (7 - i);
    unsigned int CRC_Check = 0;
    CRC_Check = (src->Humi_H + src->Humi_L + src->Temp_H + src->Temp_L);
    if(CRC_Check % 256)
        CRC_Check -= (256 * (CRC_Check / 256));
    if(CRC_Check == src->CRC)
        return 1;
    return 0;
}

void PacketPrepair(DHT_Value *src) {
    dataOut[0] = 'H';
    dataOut[1] = NodeID;
    dataOut[2] = DHT_TYPE;
    dataOut[3] = src->Humi_H;
    dataOut[4] = src->Humi_L;
    dataOut[5] = src->Temp_H;
    dataOut[6] = src->Temp_L;
    dataOut[7] = VoltOut[0];
    dataOut[8] = VoltOut[1];
    dataOut[9] = 'H';
    dataOut[10] = '\r';
    dataOut[11] = '\n';
    dataOut[12] = 0x00;
}
