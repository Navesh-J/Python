sum=lambda x,y:x+y
print("\nSum= ",sum(3,4))

# filter() function  - new list is returned which contains items for which the lambda function evaluates to True.
listi=[1,3,5,7,8,10]
new_list=list(filter(lambda x:(x%2==0),listi))
print(new_list)

#map() function  - new list is returned which contains items returned by the lambda function for each item.
new_list=list(map(lambda x:x*2,listi))
print(new_list)

#reduce() - Initially take 2 elements and perform operations upon them and continue the process until the end of the list is obtained
import functools
print("The sum of elements of list = ",end=" ")
print(functools.reduce(lambda x,y:x+y,listi))
print("Greatest element is : ",end=" ")
print(functools.reduce(lambda x,y:x if x>y else y,listi))