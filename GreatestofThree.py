print("Greatest Among 3 numbers")
a=int(input("Enter No.1: "))
b=int(input("Enter No.2: "))
c=int(input("Enter No.3: "))
if a>b and a>c:
    print(a," is Greatest")
elif b>c:
    print(b," is Greatest")
else:
    print(c," is Greatest")
