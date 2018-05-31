class Employee:
    raise_amt= 1.04
    employee_cnt= 0
    def __init__(self,first, last, pay):
        # below are instance variables
        self.first= first
        self.last= last
        self.pay= pay
        #self.e_mail= first+last+'@'+'email.com'
        
        Employee.employee_cnt += 1
    
    @property    
    def e_mail(self):
        return self.first+ self.last+'@'+'email.com'
    
    @property      
    def full_name(self):
        return self.first+' '+self.last
    
    @full_name.setter 
    def full_name(self, full):
        self.first, self.last= full.split()
    
    def apply_raise(self):
        self.pay= self.pay * self.raise_amt
        
    @classmethod # decorator
    def set_raise_amt(cls, amount):
        cls.raise_amt= amount
        
    @classmethod
    def from_string(cls, emp_str):
        first, last,pay= emp_str.split('-')
        return cls(first, last,pay)
    
    # static method
    @staticmethod
    def nbr_employees():
        return Employee.employee_cnt
    
    
    # Special methods:
    def __repr__(self):
        return "Employee: "+self.first+" "+ self.last+ " "+ str(self.pay)
    
#    def __str__(self):
#        return "Employee: "+self.first+" "+ self.last+ " "+ str(self.pay)
    
    def __add__(self, other):
        return self.pay + other.pay

class Developer(Employee):
    def __init__(self,first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang= prog_lang
    
class Driver(Employee):
    pass
    