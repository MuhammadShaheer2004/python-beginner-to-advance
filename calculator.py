#first user se poocho phir uske hisaab se calculation kro

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operator = input("Enter Operator '+', '-', '*', '/'")

if operator=="+":
    print(f"The sum of {num1} and {num2} is {num1+num2}")
elif operator =="-":
    print(f"The difference of {num1} and {num2} is {num1-num2}")
elif operator =="*":
    print(f"The multiplication of {num1} and {num2} is {num1*num2}")
elif operator =="/":
    print(f"The division of {num1} and {num2} is {num1/num2}")
else:
    print("You have entered wrong operator")

