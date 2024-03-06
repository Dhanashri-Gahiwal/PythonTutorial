num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("choose any operator (+, -, *, /) you want to perform: ")

if(operator == "+"):
    print(num1,"+",num2,"=",num1 + num2)
elif(operator == "-"):
    print(num1,"-",num2,"=",num1 - num2)
elif(operator == "*"):
    print(num1,"*",num2,"=",num1 * num2)
elif(operator == "/"):
    print(num1,"/",num2,"=",num1 / num2)
else:
    print("Please enter a valid operator")