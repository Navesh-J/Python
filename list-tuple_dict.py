list1=[2, 3, 5.7, 'Hello']
list2=['hehe',9,234 , 2+3j]
print (list1)       # Prints complete list
print (list1[0])    # Prints first element of the list
print (list1[1:3])  # Prints elements starting from 2nd till 3rd
print (list1[2:])    # Prints elements starting from 3rd element
print (list2 * 2)    # Prints list two times
print (list1 + list2) # Prints concatenated lists
list1.insert(0,"new")
print(list1)
list1.remove("new")
print(list1)
s=list1.pop(3)
print(s)
print(list1)
del list1[0]
print(list1)
list1[1]=5.5
print(list1)

tuple=(1,5,2.8,'mochi')
tuple1=(1,5,2.8)
print(tuple)
l=len(tuple)
min=min(tuple1)
max=max(tuple1)
print(l,min,max)
list(tuple)
# dictionary
dict={
    'name':'john',
    'code': 2423,
    'branch': 'assassian'
}
print(dict)
print(dict.keys())
print(dict.values())