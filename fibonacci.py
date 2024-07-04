n=(int(input("Enter the limit :  ")))
a,b=0,1
while(n):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
    n-=1