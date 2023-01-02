class Company:
    company_name = 'Tv9'
    
    def __init__(self, name, id, dept):
        self.name = name
        self.id = id
        self.dept = dept
    def compinfo(self):
        return f"Name is : {self.name}, ID is : {self.id}, 'And',  Departhment : {self.dept}"
    
    def ch_company_name(cls,new_company_name):
        cls.ch_company_name = new_company_name
    
class Employee(Company):
    total_employee = 25
    
    def __init__(self, f_name, l_name, ph_num, address):
        self.f_name = f_name
        self.l_name = l_name
        self.ph_num = ph_num
        self.address = address
        
    def empinfo(self):
        return f"Employee Name : {self.f_name} , Employee Last Name : {self.l_name}, Phone Number is : {self.ph_num}, Employee Address : {self.address}"
    
    @classmethod
    def ch_address(cls, new_address):
        cls.ch_address = new_address
    
class Programer(Employee):
    languages = 'Pytnon'
    
    def __init__(self, languages):
        self.languages = languages
        return f"Languages : {self.languages}"
        
    
    
    
ravi = Company('Ravi', 22, 'IT')
dhanu = Company('Dhanu', 55, 'Input')
print(ravi.compinfo())


Company.ch_company_name = 'Tv9 Kannada'
print(ravi.ch_company_name)
    
sri = Employee('Srinivas', 'GB', 88963252214, 'Shantinagar')
print(sri.empinfo())

sri.ch_address = 'Rajajinagar'
print(sri.ch_address)


print(Programer.languages)

