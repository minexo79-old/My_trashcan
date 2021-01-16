#include <msp430fr5969.h>

void Pin_Initialize(void);                      // Initialize All pins
void Clock_Setting(void);                       // System Clock
void UCA0_DMA_TX_Init(void);                    // UART0 TX Transfer Channel Using DMA
void GetVolt(float);
void InsertSort(unsigned int *,char);

// ADC and REF offset in TLV structure memory address
#define REF25_Cal           *((unsigned int*)0x1A2C)       // REF_2.5_FACTOR stored in TLV
#define ADC_Offset          *((int*)0x1A18)                // for read out ADC_Offset stored in Flash
#define ADC_Gain            *((unsigned int*)0x1A16)       // for read out ADC_Gain stored in Flash

// Voltage
unsigned char VoltOut[2] = "";
#pragma PERSISTENT(VoltOut)

void Pin_Initialize(void) {                     // Initialize All pins
    P1OUT = 0; P1DIR = 0xFF;
    P2OUT = 0; P2DIR = 0xFF;
    P3OUT = 0; P3DIR = 0xFF;
    P4OUT = 0; P4DIR = 0xFF;
    // PJBIT
    PJDIR = 0xFFFF;
}

void Clock_Setting(void) {                      // System Clock
    PJSEL0 = BIT4 | BIT5;                       // For XT1
    CSCTL0_H = CSKEY >> 8;                      // UnLock CS registers
    CSCTL1 = DCOFSEL_0;                         // DCO 1Mhz
    CSCTL2 = SELA__LFXTCLK | SELM__DCOCLK | SELS__DCOCLK;
    CSCTL3 = DIVA__1 | DIVM__1 | DIVS__1;
    CSCTL4 &= ~LFXTOFF;                         // Enable LFXT1

    do {
        CSCTL5 &= ~LFXTOFFG;                    // Clear XT1 fault flag
        SFRIFG1 &= ~OFIFG;
    } while (SFRIFG1 & OFIFG);                  // Test oscillator fault flag

    CSCTL0_H = 0;                               // Lock CS registers
}

void UCA0_TX_Init(void) {                   // UART0 TX Transfer Channel Using DMA
    P2SEL0 &= ~(BIT0 + BIT1);                   // UCA0TX,RX
    P2SEL1 |= (BIT0 + BIT1);                    // UCA0TX,RX
    // UART
    UCA0CTLW0 |= (UCSWRST | UCSSEL__SMCLK);
    UCA0BRW = 6;                                // 9600 bps
    UCA0MCTLW |= (0x2000 | UCOS16 | UCBRF_8);
    UCA0CTLW0 &= ~UCSWRST;

    // Use TX Interrupt
    UCA0IE &= ~UCTXCPTIE;                    // Disable Tx Interrupt

    // DMA
//    DMACTL0 |= DMA0TSEL__UCA0TXIFG;
//    DMA0CTL |= DMADT_4 | DMASRCINCR_3 | DMASRCBYTE | DMADSTBYTE | DMALEVEL;
//    __data16_write_addr((unsigned short)&DMA0DA,(unsigned short)&UCA0TXBUF);
//    DMA0CTL &= ~DMAEN;
}

void InsertSort(unsigned int *src, char len) {
    char i,j;
    unsigned int tmp;
    for(i=1;i<len;i++) {
        tmp = src[i];
        for(j=i;j>=1;j--) {
            if(src[j-1] >= tmp) {
                src[j] = src[j-1];
                src[j-1] = tmp;
            }
        }
    }
}

void GetVolt(float Volt_scale) {
    unsigned int ADC12Value[9] = {0}, ADCMiddle;
    char k;
    float SystemVolt;

    // P1.5 Mode: Analog A5 pin
    P1SEL1 |= BIT5;
    P1SEL0 |= BIT5;

    /*
     * open reference generater
     */
    // while(REFCTL0 & REFGENBUSY);              // Wait for reference generator
    REFCTL0 = REFVSEL1 + REFON;               // VREF on and set to 2.5V
    while(!(REFCTL0 & REFGENRDY));            // Wait for reference generator

    /*
     * Open ADC
     */
    ADC12CTL0 = ADC12SHT10 | ADC12ON;
    ADC12CTL1 = ADC12SHP;                     // Use sampling timer hold
    ADC12CTL2 = ADC12RES_2;                   // 12-bit conversion results
    ADC12CTL3 = 0;                            // reset register
    ADC12MCTL0 |= ADC12VRSEL0 | ADC12INCH_5;  // select channel_5
    for(k=0;k<9;k++) {
        ADC12CTL0 |= (ADC12ENC | ADC12SC);    // Sampling and conversion start
        __delay_cycles(50);                   // hold 50ms
        while ((ADC12BUSY & ADC12CTL1));      // Wait for the end of conversion
        ADC12Value[k] += (unsigned int)ADC12MEM0;
    }

    ADC12CTL0 &= ~ADC12ENC;                   // Disable ADC conversion
    ADC12CTL0 &= ~ADC12ON;                    // ADC12 off
    /*
     * Get ADC Value Middle
     */
    InsertSort(ADC12Value, 9);
    ADCMiddle =ADC12Value[4];
//    ADC12Value = (ADC12Value / 10);
    /*
     * ADC_Correct_Value = ADC_Source * ADC_Gain / 2^15 + ADC_OFFSET + REF2.5 / 2^15
     */
    ADCMiddle = (((float)ADCMiddle * ((float)ADC_Gain / 32768)) + (float)ADC_Offset) + ((float)REF25_Cal / 32768) + 0.5;
    SystemVolt = (ADCMiddle * (2.5 / 4095)) + ((ADCMiddle * (2.5 / 4095)) * (1 / Volt_scale));

    // Voltage Integer
    VoltOut[0] = (unsigned char)SystemVolt;
    // Voltage Decimal
    VoltOut[1] = (unsigned char)((SystemVolt - VoltOut[0]) * 10);
}
