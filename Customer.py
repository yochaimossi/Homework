class Customer:

    def __init__(self,id,fname,lname,address,phone):
        self.id=id
        self.fname=fname
        self.lname=lname
        self.address=address
        self.phone=phone

    def __str__(self):
        return str(self.__dict__)

    def __repr__(self):
        return str(self.__dict__)