dict={
    'roll': 36,
    'name': "Navesh",
    'course':"B.tech",
    'roll': 96
}
print(dict)

#Print Keys
for key in dict:
    print(key,end=" ")
print()

#Print Values
for val in dict.values():
    print(val,end=" ")
print()

#Print Items
for key,val in dict.items():
    print(key,val ,"\t",end=" ")
print()

#string representation
print(str(dict))