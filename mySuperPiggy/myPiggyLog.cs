using System;
using System.Collections.Generic;

namespace hellocsharp {
    class myPiggyLog {
        private List<string> Note;
        private List<DateTime> dateTimes;
        public List<int> Money;

        public myPiggyLog() {
            this.Note = new List<string>();
            this.dateTimes = new List<DateTime>();
            this.Money = new List<int>();
        }

        public void addLog(int money, DateTime date, string note) {
            Money.Add(money);
            dateTimes.Add(date);
            Note.Add(note);
        }

        public void ListLog () {
            Console.WriteLine("日期\t\t金額\t用途");
            Console.WriteLine("--------------------------------------------");
            for(int index=0;index<Money.Count;index++) {
                Console.Write($"{this.dateTimes[index].ToShortDateString()}\t");
                Console.Write($"{this.Money[index]}\t");
                Console.WriteLine($"{this.Note[index]}");
            }
        }
    }
}