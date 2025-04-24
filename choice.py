a=int(input("enter a"))
b=int(input("enter b"))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    try:
        return a/b
    except:
        return 'zero division'
choice=input("enter 1 for add,2 for sub,3 for mul,4 for div")
if choice=='1':
    print(add(a,b))
elif choice=='2':
    print(sub(a,b))
elif choice=='3':
    print(mul(a,b))
elif choice=='4':
    print(div(a,b))
else:
    print("invalid choice")
