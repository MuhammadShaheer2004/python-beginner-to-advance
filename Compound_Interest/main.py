principle=0
interest_rate=0
time=0
print("*******************Compound Interest Calculator***************")

principle=float(input("Enter Principle Amount: "))
while principle <=0:
    print("Principle Amount cannot be zero or less")
    principle=float(input("Enter Priniciple Amount: "))

interest_rate=float(input("Enter Interest Rate: "))
while interest_rate <=0:
    print("Interest Rate cannot be zero or less")
    interest_rate=float(input("Enter Interest Rate: "))

time=int(input("Enter Time in years: "))
while time <=0:
    print("Time cannot be zero or less")
    time=int(input("Enter Time in years: "))


print(f"Principle Amount: {principle:,}")
print(f"Interest Rate: {interest_rate}")
print(f"Time in Years: {time}")

compound_interest= principle * pow((1+ (interest_rate/100)),time)
print(f"Compound Interest Calculated: {compound_interest }")