
temp=float(input("Enter the temperature: "))
unit=input("Is it in 'C' or 'F'?: ")

if unit.upper()=="C":
    temp=temp*(9/5)+32
    print(f"Temperature in F: {temp}")
elif unit.upper()=="F":
    temp=(temp -32) * 5/9
    print(f"Temperature in C: {temp}")
else:
    print(f"{unit} is not a valid unit!")