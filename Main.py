#import mysql.connector as pb
import sys
import random
from prettytable import from_db_cursor
import datetime

def validDate(date):
    return (len(date)==10 and
        date[0:4].isdigit() and
        date[4]=='-' and
        date[5:7].isdigit() and
        date[7]=='-' and
        date[8:10].isdigit())

def above18(date, _format='%Y-%m-%d'):
    dateobj=datetime.datetime.strptime(date, _format)
    today=datetime.date.today()
    today_datetime=datetime.datetime(today.year, today.month, today.day)
    x=(today_datetime-dateobj)
    return (x>=datetime.timedelta(days=18*365))


def create():
        hn=input("Enter Name:")
        an=random.randrange(111111111111,999999999999)

        while True:
            dob=input("Enter DOB in (YYYY-MM-DD):")
            if not validDate(dob):
                print("Invalid date format, re-enter it")
                continue
            elif not above18(dob):
                print("You must be atleast 18 years to create a bank account")
            else:
                break

        fn=input("Father name:")
        mn=input("Mother name:")

        while True:
            adn=input("Enter aadhar number:")
            if len(adn)==12 and adn.isdigit():
                break
            else:
                print("Wrong aadhar number. Must be 12 digit")
                continue
       
        ads=input("Enter address:")

        while True:
            ph=input("Enter phone no:")
            if not (len(ph)==10 and ph.isdigit()):
                print("Enter 10 digit phone number")
    
        pno=input("Enter PAN no:")

        while True:
            ph=input("Enter phone no:")
            if not (len(ph)==10 and ph.isdigit()):
                print("Enter 10 digit PAN number")
        
        de=int(input("Please Insert a Money to Deposit to Start an Account:"))
       
        at=input("Enter the account type (Savings/current):")
        q="insert into pers_det values('{}',{},'{}','{}','{}','{}')".format(hn,an,dob,fn,mn,ads)
        q2="insert into hold_det values('{}',{},{},{},{},'{}')".format(hn,an,adn,pno,ph,at)
        q6="insert into balence values('{}',{},{})".format(hn,an,de)
        q7="create table {} (date char(10),Balance int)".format(hn)
        q9="insert into {} values(DATE(CURDATE()),{})".format(hn,de)
        curdb.execute(q)
        curdb.execute(q2)
        curdb.execute(q6)
        curdb.execute(q7)
        curdb.execute(q9)
        db.commit()
        sys.stderr.write("ACCOUNT CREATED SUCESSFULLY\n")
        print("ACCOUNT DETAILS ARE GIVEN BELOW")
        q4=f"""\
select hold_det.Acc_Holder, hold_det.Acc_no, Aadhar_No, Pan_no, Phone_no, Acc_Type, DOB, Father_Name, Mother_Name, Address
from pers_det, hold_det
where Hold_det.Acc_No=pers_det.Acc_no and pers_det.Acc_no={an};"""
        curdb.execute(q4)
   
        data=from_db_cursor(curdb)
   
        print(data)

def display():
    flag=0
    q3="select * from pers_det,hold_det where pers_det.Acc_no=hold_det.Acc_no"
    r=input("Enter Account_Holder name to search:")
    curdb.execute(q3)
    data=curdb.fetchall()
    
    #DISPLAYING DATA
    sys.stderr.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    sys.stderr.write("HOLDER_NAME\t\tACC_NO\t\t\tPHONE_NO\t\tPAN_NO\t\t\tACC_TYPE\n")
    sys.stderr.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    for row in data:
        if row[0]==r:
            print(row[0],"\t\t\t",row[1],"\t\t",row[10],"\t\t",row[9],"\t\t",row[11])
            flag=1        
    sys.stderr.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    if flag==0:
        print("ACCOUNT NUMBER NOT FOUND")
    sys.stderr.write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    
def deposit():
    q5="select * from balence"
    curdb.execute(q5)
    data2=curdb.fetchall()
    dn=input("Enter holder name to deposit")
    for i in data2:
        if i[0]==dn:
            sys.stderr.write("ACCOUNT FOUND")
            de2=int(input("Enter Amount to Deposit:"))
            da2=datetime.datetime.today().strftime("%Y-%m-%d")
            q8="insert into {} values('{}',{})".format(dn,da2,de2)
            curdb.execute(q8)
            q10="select sum(balance) from {}".format(dn)
            curdb.execute(q10)
            data3=float(curdb.fetchone()[0])
            q3="select * from pers_det,hold_det where pers_det.Acc_no=hold_det.Acc_no"
            q11="insert into {} values('{}',{})".format(dn,da2,de2)
            curdb.execute(q11)
            curdb.execute(q3)
            data=curdb.fetchall()
            sys.stderr.write("-----------------------------------------------------------------------------------------------------------------------------------------\n")
            sys.stderr.write("HOLDER_NAME\t\tACC_NO\t\t\tPHONE_NO\t\tPAN_NO\t\t\tACC_TYPE\n")
            sys.stderr.write("-----------------------------------------------------------------------------------------------------------------------------------------\n")
            for row in data:
                if row[0]==dn:
                    print(row[0],"\t\t\t",row[1],"\t\t",row[10],"\t\t",row[9],"\t\t",row[11])
                    flag=1
                    print("Your Account No is",row[1],"has current balance",data3)
            sys.stderr.write("-----------------------------------------------------------------------------------------------------------------------------------------\n")
        else:
            sys.stderr.write("ACCOUNT NOT FOUND!!! ENTER VALID HOLDER NAME")
    db.commit()
def history():
    dan=input("enter holder name:")
    q12="select * from {}".format(dan)
    data3=curdb.fetchall()
    sys.stderr.write("------------------------------------------------------------\n")
    sys.stderr.write("DATE\t\tBALANCE\t\t\t\n")
    sys.stderr.write("------------------------------------------------------------\n")
    if row[0]==dan:
         for row in data3:
            print(row[0],"\t\t\t",row[1])
            
            
    sys.stderr.write("-----------------------------------------------------------\n")
#Main
db=pb.connect(host="localhost",user="root",passwd="sagar@123",database="bank")
if db.is_connected():
    sys.stderr.write("---------WELCOME TO HDFC BANK---------\n")
curdb=db.cursor()
while True:
    sys.stderr.write("MAIN MENU\n")
    print("1.CREATE ACCOUNT")
    print("2.DEPOSIT AMOUNT")
    print("3.WITHDRAW AMOUNT")
    print("4.UPDATE ACCOUNT DETAILS")
    print("5.SEARCH ACCOUNT")
    print("6.DISPLAY DETAILS")
    print("7.DROP ACCOUNT")
    print("8.STATEMENT")
    print("9.EXIT")
    ch=int(input("Enter Choice (1-9):"))
    if ch==1:
        create()
    elif ch==2:
        deposit()
    elif ch==3:
        withdraw()
    elif ch==4:
        update()
    elif ch==5:
        search()
    elif ch==6:
        display()
    elif ch==7:
        drop()
    elif ch==8:
        history()
    elif ch==9:
        break
    else:
        sys.stderr.write("SORRY!!! YOU HAVE ENTERED THE WRONG CHOICE! TRY WITH OTHER CHOICE")
