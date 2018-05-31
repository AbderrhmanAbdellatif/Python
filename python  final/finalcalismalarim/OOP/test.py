from employee import Employee
from employee import Developer
from employee import Driver

emp_1= Employee("Ayla","Gülcü", 10)
emp_2= Employee("Ömer", "Gülcü", 3)


print(emp_1.full_name)
print(emp_1.e_mail)
emp_1.first= "Leyla"
print(emp_1.full_name)
print(emp_1.e_mail)
emp_1.full_name= "İsim Soyisim"
print(emp_1.full_name)

#==============================================================================
# 
# print(Employee.full_name(emp_1)) 
# # identical to calling emp_1.full_name()
# 
# #==============================================================================
# # print(emp_1.pay)
# # emp_1.apply_raise()
# # print(emp_1.pay)
# #==============================================================================
# #print("emp_1 pay: " + str(emp_1.pay))
# #print(emp_1.raise_amt)
# #emp_1.raise_amt= 1.05
# #emp_1.apply_raise()
# #print("emp_1 pay: " + str(emp_1.pay))
# #
# #print("Number of employees created:" + str(Employee.employee_cnt))
# 
# Employee.set_raise_amt(1.06)
# print(emp_1.raise_amt)
# 
# #print(Employee.__dict__)
# #print(emp_1.__dict__)
# #print(emp_2.__dict__)
# 
# # class methods as alternative constructors:
# emp_3_str= "Ali-Geldi-5"
# #first, last,pay= emp_3_str.split('-')
# #emp_3= Employee(first, last,pay)
# #print(emp_3.full_name())
#
# # instead use the following:
# emp_3= Employee.from_string(emp_3_str)
# print(emp_3.full_name())
#
# print(Employee.nbr_employees())
# print(emp_3.nbr_employees())
# print(emp_3.__dict__)
# 
# print('*******')
# 
# dev_1= Developer("Ayşe","Gül", 5, "Python")
# print(dev_1.full_name())
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)
# print(dev_1.prog_lang)
# 
# #print(help(Developer))
# 
# print(isinstance(dev_1, Employee))
# 
# print(issubclass(Developer, Driver))
# 
# print(dev_1)
# 
# print(1+2)
# print(int.__add__(1,2))
# 
# print('a'+ 'b')
# print(str.__add__('a','b'))
# 
# print(emp_1+emp_2)
#==============================================================================
