class CustomerDataAccess:

    def __init__(self, path):
        con = sqlite3.connect(path)
        self.cursor = con.cursor()

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)

    def print_all_customers(self):
        cursor.execute("SELECT * FROM Customer")
        print(self.cursor.fetchall())

    def insert_customer(self, Customer):
            self.cursor.execute(f'INSERT INTO {Customer} VALUES ({Customer.id}, "{Customer.fname}",' +
                           f' {Customer.lname}, {Customer.address}, {Customer.phone})')


    def delete_customer(self, id):
        self.cursor.execute("DELETE FROM Customer WHERE id=?", (id,))

    def get_all_customers(self):
        self.cursor.execute("SELECT * FROM Customer")
        _lst1 = []
        for row in cursor:
            print(row)
            _lst1.append(Customer(row[0], row[1], row[2], row[3], row[4]))
        print(_lst1)

    def get_customers_by_id(self, id):
        self.cursor.execute("SELECT * FROM Customer WHERE id=?", (id))
        print(self.cursor.fetchall())

    def update_customer(self, id, Customer):
        self.cursor.execute(f'UPDATE {Customer} SET {Customer.fname}=?,{Customer.lname}=?,{Customer.address}=?,{Customer.phone}=? WHERE {Customer.id}=?', (id,))
