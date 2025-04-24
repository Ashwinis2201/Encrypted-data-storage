def add(a,b):
    return a+b
a=int(input("enter a:"))
b=int(input("enter b:"))
print(add(a,b))

def sub(a,b):
    return a-b
a=int(input("enter a:"))
b=int(input("enter b:"))
print(sub(a,b))

def mul(a,b):
    return a*b
a=int(input("enter a:"))
b=int(input("enter b:"))
print(mul(a,b))

def div(a,b):
    return a/b
a=int(input("enter a:"))
b=int(input("enter b:"))
print(div(a,b))

try:
    return a/b
 except:
     return "It is infinity"

