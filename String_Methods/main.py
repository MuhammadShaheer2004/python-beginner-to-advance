#Validate user input exercise
 #1. username is no more than 12 characters
 #2. username must not contain any spaces
 #3. username must not contain digits
print("Validate user input exercise \n 1. username is no more than 12 characters \n 2. username must not contain any spaces \n 3. username must not contain digits or special characters")
username= input("Enter username: ")

if len(username)>12:
    print("Username cannot be more than 12 characters")
elif username.find(" ")>=0:
    print("Username cannot contain spaces")
elif not username.isalpha():
    print("Username can only contain alaphabets")
else:
    print("Username is available")