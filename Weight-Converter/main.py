
#Ask the user for their weight and the unit they want to convert to
weight = float(input("Enter Your weight: "))
unit = input("Is it in 'KG' and 'LB'?: ")

if unit.upper()=="KG":
      weight*=2.205
      print(f"Your weight in LB is {weight}")
elif unit.upper()=="LB":
      weight/=2.205
      print(f"Your weight in KGs in {weight}")
else:
      print("Invalid unit. Please enter 'KG' or 'LB'.")