using System;

namespace hellocsharp
{
    class Program
    {
        static void Main(string[] args)
        {
            mySuperPiggy kevenSuperPiggy = new mySuperPiggy("Keven", 1000); 

            kevenSuperPiggy.addMoney(300, DateTime.Now, "零用錢盈餘");
            kevenSuperPiggy.addMoney(300, DateTime.Now, "零用錢盈餘");
            kevenSuperPiggy.addMoney(300, DateTime.Now, "零用錢盈餘");

            kevenSuperPiggy.breakPiggy();

            kevenSuperPiggy.addMoney(20, DateTime.Now, "今天的飲料錢");
            kevenSuperPiggy.addMoney(40, DateTime.Now, "今天的早餐錢");
            kevenSuperPiggy.addMoney(20, DateTime.Now, "今天的飲料錢");

            kevenSuperPiggy.ListLog();

            // End the Program
            return;
        }
    }
}
