import sqlite3
from sqlite3 import Error


conn = sqlite3.connect('ResDB.db')
c=conn.cursor()

# Create table - EMPLOYEE
c.execute('''CREATE TABLE EMPLOYEE
                 ([EID] INTEGER PRIMARY KEY,[Ename] text, [Phno] INTEGER, [EXP] INTEGER)''')
c.execute('insert into EMPLOYEE values(1,"Nitin",456789123,2)')
c.execute('insert into EMPLOYEE values(2,"Nitish",123789123,2)')
c.execute('insert into EMPLOYEE values(3,"Om",454569123,1)')
c.execute('insert into EMPLOYEE values(4,"Ram",987456123,2)')
c.execute('insert into EMPLOYEE values(5,"Rahul",452369871,2)')
conn.commit()
# Create table - CUSTOMER
c.execute('''CREATE TABLE CUSTOMER
                 ([CID] INTEGER PRIMARY KEY,[Cname] text,[Address] text,[DOB] date,[EID] integer,[Ctoken] integer, FOREIGN KEY(EID) REFERENCES EMPLOYEE(EID))''')
c.execute('insert into CUSTOMER values(11,"Raj","Shillong","04-02-1999",1,10)')
c.execute('insert into CUSTOMER values(12,"Simran","Punjab","08-06-1999",2,11)')
c.execute('insert into CUSTOMER values(13,"Irfan","Haryana","10-02-1999",3,12)')
c.execute('insert into CUSTOMER values(14,"Suresh","Delhi","14-08-1999",4,13)')
c.execute('insert into CUSTOMER values(15,"Dhoni","Ranchi","20-12-1999",5,14)')
# Create table - testresults
c.execute('''CREATE TABLE ORD
                 ([OID] INTEGER PRIMARY KEY,[OName] text,[ONo] INTEGER,[OPrice] INTEGER,[Portion] INTEGER,[CID] INTEGER,FOREIGN KEY(CID) REFERENCES CUSTOMER(CID) )''')



#create table VALET
c.execute('''CREATE TABLE VALET
                 ([EID] INTEGER,[Vname] text , [Ctoken] int,PRIMARY KEY(EID),FOREIGN KEY(Ctoken) REFERENCES CUSTOMER(Ctoken))''')
c.execute('insert into VALET values(101,"Ramesh",1)')
c.execute('insert into VALET values(102,"Koorfi",2)')
c.execute('insert into VALET values(103,"Michael",3)')
c.execute('insert into VALET values(104,"Yamraj",4)')
c.execute('insert into VALET values(105,"Devilha",5)')

#create table BILL
c.execute('''CREATE TABLE "BILL" ("BID" INTEGER,"CID" INTEGER,"AMOUNT" FLOAT,PRIMARY KEY(BID),FOREIGN KEY(CID) REFERENCES CUSTOMER(CID))''')



c.execute('''CREATE TABLE BILL1([CID] INTEGER,[BILL] INTEGER,PRIMARY KEY(CID,BILL))''')

#create trigger BILL_logger
c.execute('CREATE TABLE Cust_logs (C_id INTEGER, time_added TIMESTAMP)')

c.execute('''CREATE TRIGGER Cust_logger
         AFTER INSERT ON CUSTOMER
         BEGIN
             INSERT INTO Cust_logs VALUES (new.CID, strftime('%s', 'now'));
         END
         ;
         ''')


conn.commit()
