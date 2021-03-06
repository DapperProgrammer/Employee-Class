#day shift == 1 : night shift == 2
# user_name is the object name of type production_worker
# when you create an object you initialize all values at that time, after that, you can use the set_ methods to change values.  The 
# get_ methods always return the current value of that variable.
# production_worker is the subclass of Employee

class Employee:
  def __init__(self, name = 'Error please enter your name!', number = 'Error please input your employee number!'):
    self.employee_name = name #Assigns the value of 'name' to self.employee_name
    self.employee_number = number #Assigns the value of 'number' to 'self.employee_number'
    
  def get_name(self):
    employee_name = self.employee_name #Assigns 'employee_name' with the value of 'self.employee_name'
    return employee_name #Returns the value of 'employee_name'
  
  def get_employee_number(self):
    employee_number = self.employee_number #Assigns 'employee_number' with the value of 'self.employee_number'
    return employee_number #Returns the value of 'employee_number'
    

class Production_worker(Employee):
  def __init__(self, name, number, shift_num, pay_rate ):
    Employee.__init__(self, name, number)
    self.employee_shift = shift_num
    self.employee_pay_rate = pay_rate
  
  def set_shift_num(self, shift_num):
    self.employee_shift = shift_num
  
  def get_shift_num(self):
    employee_shift = self.employee_shift
    return self.employee_shift
  
  def set_pay_rate(self, pay_rate):
    self.employee_pay_rate = pay_rate
  
  def get_pay_rate(self):
    pay_rate = self.employee_pay_rate
    return pay_rate
    
    
def main():
 # user_input = Employee (input('Enter your name:'), int(input('Enter your employee number:')))
 # print(user_input.employee_name, user_input.employee_number)
  
  user_input = Production_worker (input('Enter your name: '),int(input('Enter your employee number: ')),int(input('Enter your shift: ')), float(input('Enter your payrate: ')))
  print( "user name: ", user_input.get_name(),"Emp Number: ",user_input.get_employee_number(), "shift : ",user_input.get_shift_num(),"Payrate: $", user_input.get_pay_rate())
   #
main()
