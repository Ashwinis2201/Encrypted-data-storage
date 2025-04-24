a=int(input("enter a numbers"))
b=int(input("enter a numbers"))
c=int(input("enter a numbers"))
if a>b + a>c:
    print(a,"is the largest")
elif b>a + b>c:
    print(b,"is the largest")
elif c>a + c>b:
    print(c,"is the largest")
else:
    print("2 or more numbers are equal")