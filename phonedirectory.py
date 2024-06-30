import mysql.connector as mys
import argparse

parser=argparse.ArgumentParser(description="Phone Directory using Python and MySQL")
parser.add_argument('-u', '--username',help="Enter the username of MySQL Server", required=True)
parser.add_argument('-p', '--password',help="Enter the password of MySQL Server", required=True)
args=parser.parse_args()

mydb=mys.connect(user=args.username,passwd=args.password)
c=mydb.cursor()
c.execute('create database if not exists PHONE_DIRECTORY')
c.execute('use PHONE_DIRECTORY')
c.execute('create table  if not exists CONTACTS(contact_id int primary key,contact_name varchar(20) not null,contact_number varchar(15) not null,email_id varchar(30) not null)')

# INSERTING CONTACTS

def insert(n):
    for i in range(n):
        con_id=int(input("enter contact_id:"))
        con_name=input("enter contact_name:")
        con_no=int(input("enter contact_number:"))
        email_id=input("enter email_id:")
        c.execute("insert into CONTACTS values({},'{}','{}','{}')".format(con_id,con_name,con_no,email_id))
        mydb.commit()
        print("\tCONTACTS INSERTED\t")

# SEARCHING CONTACTS BASED ON contact_id, contact_name , contatct_number , email_id 
        
def search():
    ans=int(input("what do you want to search [1=contact_id,2=contact_name,3=contact_number,4=email_id]:"))
    if ans==1:
        s=input("enter contact_id to be searched:") 
        c.execute('select * from CONTACTS')
        data=c.fetchall()
        for i in data :
            if i[0]==s:
                print("\tCONTACT FOUND\t")
                print("THE CONTACT DETAIL IS :",i)
            else:
                print("\tCONTACT NOT FOUND\t")
    elif ans==2:
        s=input("enter contact_name to be searched:") 
        c.execute('select * from CONTACTS')
        data=c.fetchall()
        for i in data :
            if i[1]==s:
                print("\tCONTACT FOUND\t")
                print("THE CONTACT DETAIL IS :",i)
            else:
                print("\tCONTACT NOT FOUND\t")
    elif ans==3:
        s=input("enter contact_number to be searched:") 
        c.execute('select * from CONTACTS')
        data=c.fetchall()
        for i in data :
            if i[2]==s:
                print("\tCONTACT FOUND\t")
                print("THE CONTACT DETAIL IS :",i)
            else:
                print("\tCONTACT NOT FOUND\t")
    elif ans==4:
        s=input("enter email_id to be searched:") 
        c.execute('select * from CONTACTS')
        data=c.fetchall()
        for i in data :
            if i[3]==s:
                print("\tCONTACT FOUND\t")
                print("THE CONTACT DETAIL IS :",i)
            else:
                print("\tCONTACT NOT FOUND\t")
    else:
        print("invalid choice")
                
# UPDATING CONTACTS BASED ON contact_id, contact_name, contact_number, email_id

def update():
    ans=int(input("what do you want to update [1=contact_id,2=contact_name,3=contact_number,4=email_id]:"))
    if ans==1:
        old_id=input("enter contact_id whose id is to be updated:")
        new_id=input("enter new contact_id:")
        c.execute("update CONTACTS set contact_id='{}' where contact_id='{}' ".format(new_id,old_id))
        mydb.commit()
        print("\CONTACT ID UPDATED\t")
    elif ans==2:
        old_name=input("enter contact_name whose name is to be updated:")
        new_name=input("enter new contact_name:")
        c.execute("update CONTACTS set contact_name='{}' where contact_name='{}' ".format(new_name,old_name))
        mydb.commit()
        print("\tCONTACT NAME UPDATED\t")
    elif ans==3:
        old_name=input("enter contact_number whose number is to be updated:")
        new_name=input("enter new contact_number:")
        c.execute("update CONTACTS set contact_number='{}' where contact_number='{}' ".format(new_name,old_name))
        mydb.commit()
        print("\tCONTACT NUMBER UPDATED\t")
    elif ans==4:
        old_name=input("enter email_id whose email is to be updated:")
        new_name=input("enter new email_id:")
        c.execute("update CONTACTS set email_id='{}' where email_id='{}' ".format(new_name,old_name))
        mydb.commit()
        print("\tCONTACT EMAIL UPDATED\t")
    else:
        print("invalid choice")

# DELETING CONTACTS BASED ON contact_id, contact_name, cntact_number, email_id 
        
def delete():
    ans=int(input("what do you want to delete [1=contact_id,2=contact_name,3=contact_number,4=email_id]:"))
    if ans==1:
        d=int(input("enter contact_id to be deleted"))
        c.execute("delete from CONTACTS where contact_id='{}' ".format(d))
        mydb.commit()
        print("\tCONTACT DELETED\t")
    elif ans==2:
        d=input("enter contact_name to be deleted")
        c.execute("delete from CONTACTS where contact_name='{}' ".format(d))
        mydb.commit()
        print("\tCONTACT DELETED\t")
    elif ans==3:
        d=int(input("enter contact_number to be deleted"))
        c.execute("delete from CONTACTS where contact_number='{}' ".format(d))
        mydb.commit()
        print("\tCONTACT DELETED\t")
    elif ans==4:
        d=input("enter email_id to be deleted")
        c.execute("delete from CONTACTS where email_id='{}' ".format(d))
        mydb.commit()
        print("\tCONTACT DELETED\t")
    else:
        print("invalid choice")
        
# DISPLAYING CONTACTS

def display():
    c.execute("select * from CONTACTS")
    for i in c:
        if len(i)==0:
            print("\tCONTACTS TABLE IS EMPTY\t")
        else:    
            print(i)
while True:
    print()
    print("ENTER 1 TO INSERT")
    print("ENTER 2 TO SEARCH")
    print("ENTER 3 TO UPDATE")
    print("ENTER 4 TO DELETE")
    print("ENTER 5 TO DISPLAY")
    print("ENTER 6 TO EXIT")
    print()
    n=int(input("enter your choice(1-6):"))
    if n==1:
        n=int(input("enter number of records to be inserted:"))
        insert(n)
    elif n==2:
        search()
    elif n==3:
        update()
    elif n==4:
        delete()
    elif n==5:
        display()
    elif n==6:
        break
    else :
        print("Invalid choice")
print("\t\tTHANK YOU...\t\t")  