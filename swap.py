a=int(input("Enter a number "))
b=int(input("Enter another number "))
a,b=b,a
print(a)
print(b)
print()
a,b=b,a
a=a+b
b=a-b
a=a-b
print(a)
print(b)