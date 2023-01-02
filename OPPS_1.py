class Student:
    sname = 'Delhi Public School'
    sloc = 'Bangalore'
    
    def __init__(self, st_firstname, st_lastname, st_address, st_phnum, ):
        self.st_firstname = st_firstname
        self.st_lastname = st_lastname
        self.st_address  = st_address
        self.st_phnum = st_phnum
        
arvind= Student('arvind', 'singh', 'Bng', 781236548)
#siddharth = Student()
#rakesh = Student()

print('Student school name :', arvind.sname, 'Student Address :', arvind.st_address)
print(arvind.__dict__)