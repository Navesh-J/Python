def exp(x,y):
    if y==0:
        return 1
    else:
        return x*exp(x,y-1)

a=int(input("Enter base "))
b=int(input("Enter exponent "))
print(exp(a,b))