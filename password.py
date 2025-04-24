password='  '
while password !='admin':
    password=input("enter the password")
    if password=='admin':
        print("you are logged in!")
    else:
        print("sorry! try again")