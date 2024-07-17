s=str(input("Enter your String : "))
rev=s[::-1]
print(rev)
rev2=""
for i in rev:
    rev2=i+rev2
print(rev2)
rev3=''.join(reversed(rev2))
print(rev3)