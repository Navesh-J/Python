#Function to add 2 numbers

def add(x,y):
    return x+y
a=10
b=40
print(add(a,b))
operation=add
print(operation(a,-b))
print()


#NameError

def func():
    print(str)

func()
str="Hello World"   


#Keyword Arguments

def func(x,y,z):
    print("\nInteger : ",x)
    print("Float : ",y)
    print("String : ",z)
func(z="Hello",x=12,y=3.14)


# Lambda Function/Anonymous Function
sum=lambda x,y:x+y
print("\nSum= ",sum(3,4))