using System;

namespace hellocsharp { 
    class mySuperPiggy {
        private myPiggyLog piggyLog;
        public string name { get;}
        public uint maxMoneySave { get; }             // uint : unsigned int
        private uint currentMoneySave { get {         // uint : unsigned int
            int setMoney = 0;
            foreach(var money in this.piggyLog.Money)
                setMoney += money;
            return ((uint)setMoney);
        }}   
        public mySuperPiggy (string Name, uint maxMoney) {
            this.name = Name;
            this.maxMoneySave = maxMoney;
            // Create Empty PiggyBank
            // this.currentMoneySave = 0;
            piggyLog = new myPiggyLog();
            piggyLog.addLog(0, DateTime.Now, "初始金額");
        }
        public void addMoney (uint money, DateTime date, string note) {
            if(currentMoneySave + money <= maxMoneySave)
            {
                // currentMoneySave += money;
                piggyLog.addLog(((int)money), date, note);
            }
            else
                throw new IndexOutOfRangeException("This Piggy is full!!!");
        }
        public uint breakPiggy () {
            uint backMoney = this.currentMoneySave;
            piggyLog.addLog(-((int)backMoney), DateTime.Now, "打破小豬");
            // set current Money to Zero
            // this.currentMoneySave = 0;
            return backMoney;
        }

        public void ListLog() {
            Console.WriteLine($"{this.name} 的小豬內存的金額 NT$ {this.currentMoneySave}/{this.maxMoneySave}.");
            piggyLog.ListLog();
        }
    }
}