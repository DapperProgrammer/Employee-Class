#Calvin Tracy
#CS 222 02
#Program Assignment 03
#Due Date: 2/23/2018
#Date Turned in: 2/23/2018
#Program to test the Employee and Production worker class


from EmployeeClass import *
  
def main():
  user_input = Production_worker (input('Enter your name: '),int(input('Enter your employee number: ')),int(input('Enter your shift: ')), float(input('Enter your payrate: ')))
  
  print()
  
  print( "Name: ", user_input.get_name(),"Emp Number: ",user_input.get_employee_number(), "shift : ",user_input.get_shift_num(),"Payrate: $", user_input.get_pay_rate())
   
main()
