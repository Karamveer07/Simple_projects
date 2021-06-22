from Mainpackage import some_main_script
from Mainpackage.Subpackage import mysubscript
'''
File got imported from modules
'''
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number:"))
'''
Functions are called to do the action
'''
some_main_script.add(num1,num2)
mysubscript.subt(num1,num2)