# Traversing

message="Hello"
index=0
for i in message:
    print("message[",index,"] = ",i)
    index+=1
print()

#rfind = reverse find
str = "is this your bag"
print(str.rfind("is",0,len(str)))

#Reversing a String
s="Palindrome"
print(s[::-1])


print(s[-1:-7:-1])