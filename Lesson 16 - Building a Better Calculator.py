#Great lesson. Building calculators is a great way to get started with learning about input and comparisons. 

num1 = float(input ("Enter 1st number: "))  # Prompt the user to enter the first number, convert it to float, and store it in 'num1'
op = input("Enter Operator: ") # Prompt the user to enter an operator and store it in 'op'
num2 = float(input("Enter second number: "))  # Prompt the user to enter the second number, convert it to float, and store it in 'num2'

if op == "+": #if user puts in + sign 
    print(num1 + num2) #then the two numbers will be added
elif op == "/": #if user puts in / sign 
    print(num1 / num2)#then the two numbers will be divided
elif op == "*": #if user puts in * sign 
    print(num1 * num2)#then the two numbers will be multiplied
else:
    print("Invalid Operator!") #any other operator input besides +, -, or * is invalid
