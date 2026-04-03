
temp=float(input("Enter the temperature: "))
unit=input("Is it in 'C' or 'F'?: ")

if unit.upper()=="C":
    temp=round(temp*(9/5)+32,2)
    print(f"Temperature in F: {temp}")
elif unit.upper()=="F":
    temp=round((temp -32) * 5/9,2)
    print(f"Temperature in C: {temp}")
else:
    print(f"{unit} is not a valid unit!")