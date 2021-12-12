import sqlite3
import sys
from Customer import Customer
from CustomerDataAccess import CustomerDataAccess

con = sqlite3.connect('Customer.db')
cursor = con.cursor()

print("Connected to Database Successfully")

cursor.execute("SELECT * FROM Customer")

def print_all_customers():
     cursor.execute("SELECT * FROM Customer")
     print(cursor.fetchall())


def insert_customer(cursor,id,fname,lname,address,phone):
        cursor.execute("INSERT INTO Customer (id, fname, lname,address,phone) VALUES (? ,? ,?, ?, ?)",(id, fname, lname,address,phone))


def delete_customer (cursor,id):
    cursor.execute("DELETE FROM Customer WHERE id=?", (id,))
    print(cursor.fetchall())



def get_all_customers (cursor):
    cursor.execute("SELECT * FROM Customer")
    _lst1 = []
    for row in cursor:
        print(row)
        _lst1.append(Customer(row[0], row[1], row[2], row[3], row[4]))


def get_customers_by_id (cursor, id):
    cursor.execute("SELECT * FROM Customer WHERE id=?", (id,))
    data = cursor.fetchall()
    if len(data) == 0:
        print(f"Customer with id: {id} does not exist")
    print(data)



def update_customer(cursor,fname,lname,address,phone,id):
    cursor.execute("UPDATE Customer SET fname=?,lname=?,address=?,phone=? WHERE id=?", (fname,lname,address,phone,id))


print ("***Welcome to the main menu - please choose one of the following options***")
print(" 1. Get all customers \n 2. Get customer by id \n 3. Insert customer \n 4. Delete customer \n 5. Update customer \n 6. Exit")
choice = int(input("Please enter your choice: "))

while True:
    if choice == 1:
        print_all_customers()
        break
    elif choice == 2:
        id=int(input("Enter customer ID to fetch:"))
        get_customers_by_id(cursor, id)
        break
    elif choice == 3:
        id = int(input("Enter customer ID:"))
        fname = input("Enter customer first name:")
        lname = input("Enter customer last name:")
        address = input("Enter customer address:")
        phone = input("Enter customer phone number:")
        insert_customer(cursor,id,fname,lname,address,phone)
        break
    elif choice ==4:
        id=int(input("Enter customer ID to delete: "))
        delete_customer(cursor, id)
        break
    elif choice == 5:
        id=int(input("Enter customer ID to update: "))
        fname = input("Enter new customer first name:")
        lname = input("Enter new customer last name:")
        address = input("Enter new customer address:")
        phone = input("Enter new customer phone number:")
        update_customer(cursor,fname,lname,address,phone,id)
        break
    elif choice == 6:
        print ("Exiting....")
        break

    else:
        print ("Invalid choice - Exiting...")
        break

con.commit()
printupdated =input("Would you like to see the updated customer list? Y/N ")


if printupdated == 'Y' or 'y':
        get_all_customers(cursor)
else:
   print ('OK bye bye...')


cursor.close()






