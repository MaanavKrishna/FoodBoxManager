import mysql.connector,tabulate

mydb = mysql.connector.connect(host="localhost", user="root", passwd="root")
mycursor = mydb.cursor()
mycursor.execute("USE FoodBox")

def checktableexists(tablename):
    mycursor.execute("SHOW TABLES LIKE %s", (tablename,))
    rec1 = mycursor.fetchone()
    return rec1

def inventory():
    if checktableexists("inventory"):
        pass
    else:
        mycursor.execute("CREATE TABLE inventory(Food_Number INT PRIMARY KEY, Food_Name VARCHAR(20), Food_Type VARCHAR(20), Price INT, Quantity INT);")

def sales():
    if checktableexists("sales"):
        pass
    else:
        mycursor.execute("CREATE TABLE sales(Date DATE, Food_Number INT, Food_Name VARCHAR(20), Quantity INT, Price INT, Total_Cost INT);")

def addinventory():
    n = int(input("No. Records to be Added:"))
    for i in range(n):
        print("\nRecord:" + str(i + 1))
        fono = int(input("Enter Food Number:"))
        fona = input("Enter Food Name:")
        while True:
            foty = input("Enter Food Type(South_Indian/North_Indian/Chinese/Continental):")
            if foty in ["South_Indian", "North_Indian", "Chinese", "Continental"]:
                break
            else:
                print("Not a valid Option:")
        price = int(input("Enter Price:"))
        qty = int(input("Enter Quantity:"))
        mycursor.execute("INSERT INTO inventory VALUES(%s, %s, %s, %s, %s)", (fono, fona, foty, price, qty))
        mydb.commit()


def delete(tablename):
    fono = int(input("Enter Food Number:"))
    mycursor.execute("DELETE FROM %s WHERE Food_Number=%s" % (tablename, fono))
    mydb.commit()
    print("Record has successfully been deleted")

def search():
    ch = int(input("Search Using\n1.Food Number\n2.Food Name\nOption:"))
    if ch == 1:
        fono = int(input("Enter Food Number:"))
        mycursor.execute("SELECT * FROM Inventory WHERE Food_Number=%s", (fono,))
    elif ch == 2:
        fona = input("Enter Food Name:")
        mycursor.execute("SELECT * FROM Inventory WHERE Food_Name=%s", (fona,))
    rec = mycursor.fetchall()
    header = ["Food Number", "Food Name", "Food Type", "Price", "Quantity"]
    print(tabulate.tabulate(rec, header, tablefmt="grid"))

def addsales():
    n = int(input("No. Records to be Added:"))
    for i in range(n):
        print("\nRecord:" + str(i + 1))
        date = input("Enter date(YY/MM/DD):")
        fono = int(input("Enter Food Number:"))
        fona = input("Enter Food Name:")
        qty = int(input("Enter Quantity:"))
        price = int(input("Enter Price:"))
        totcos = qty * price
        mycursor.execute("INSERT INTO sales VALUES(%s, %s, %s, %s, %s, %s)", (date, fono, fona, qty, price, totcos))
        mycursor.execute("UPDATE inventory SET Quantity=Quantity-%s WHERE Food_Number=%s", (qty, fono))
        mydb.commit()

def admin():
    while True:
        ch = int(input("\nAdmin Menu\n\t1.Inventory\n\t2.Sales\n\t3.Exit\nOption:"))
        if ch == 1:
            inventory()
            opt = int(input("\nInventory Menu\n\t1.Add\n\t2.Modify\n\t3.Delete\n\t4.Search\nOption:"))
            if opt == 1:
                addinventory()
            elif opt == 2:
                modify("inventory")
            elif opt == 3:
                delete("inventory")
            elif opt == 4:
                search()
            else:
                print("Option does not exist")
        elif ch == 2:
            sales()
            opt = int(input("\nSales Menu\n\t1.Add\n\t2.Modify\n\t3.Delete\nOption:"))
            if opt == 1:
                addsales()
            elif opt == 2:
                modify("sales")
            elif opt == 3:
                delete("sales")
            else:
                print("Option does not exist")
        elif ch == 3:
            break
        else:
            print("Option does not exist")

def user():
    while True:
        ch = int(input("\nUser Menu\n\t1.Add\n\t2.Modify\n\t3.Exit\nOption:"))
        if ch == 1:
            addsales()
        elif ch == 2:
            modify("sales")
        elif ch == 3:
            break
        else:
            print("Option does not exist")

def ger():
    while True:
        ch = int(input("\nReport Menu\n\t1.Current Stock\n\t2.Net Profit\n\t3.Exit\nOption:"))
        if ch == 1:
            print("\nCurrent Stock")
            mycursor.execute("SELECT * FROM Inventory")
            rec = mycursor.fetchall()
            headers = ["Food Number", "Food Name", "Food_Type", "Price", "Quantity"]
            print(tabulate.tabulate(rec, headers, tablefmt="grid"))
        elif ch == 2:
            op = int(input("\nSales Report\n1.Net Profit For the Day\n2.Net Profit For the month\nOption:"))
            if op == 1:
                mycursor.execute("SELECT SUM(Total_Cost) FROM sales WHERE Date = CURDATE()")
                totprof = mycursor.fetchone()[0]
                print("Net Profit for the Day:", totprof)
            elif op == 2:
                mycursor.execute("SELECT SUM(Total_Cost) FROM sales WHERE MONTH(Date) = MONTH(CURDATE()) AND YEAR(Date) = YEAR(CURDATE())")
                totprof_month = mycursor.fetchone()[0]
                print("Net Profit for the Month:", totprof_month)
            else:
                print("Option does not exist")
        elif ch == 3:
            break
        else:
            print("Option does not exist")

while True:
    op = int(input("--------" * 7 + "Food Box" + "--------" * 7 + "\n\nWelcome To FoodBox\n\nMain Menu\n\t1.Admin\n\t2.User\n\t3.Generate Report\n\t4.Exit\nOption:"))
    if op == 1:
        admin()
    elif op == 2:
        user()
    elif op == 3:
        ger()
    elif op == 4:
        break
    else:
        print("Option does not exist")
