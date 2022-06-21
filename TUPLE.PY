# converting a tuple into a string
a=(2,7,8,5,9)
y=str([a])
print(y)
# Write a Python program to find the repeated items of a tuple. 
tuplex = (2, 4, 5, 6, 2, 3, 4, 4, 7 )

#return the number of times it appears in the tuple.
count = tuplex.count(4)
print(count)
# Write a Python program to convert a list to a tuple
listx = [5, 10, 7, 4, 15, 3]
print(listx)
#use the tuple() function built-in Python, passing as parameter the list
tuplex = tuple(listx)
print(tuplex)
#  Write a Python program to remove an item from a tuple
# first convert it into a list and then back to tuples
a = (1, 2, 3, 4, 5)  
ls_a = list(a)      
ls_a[2]

b = tuple(ls_a)
print(b)
sort(["Ford","BMW","Volvo"])
student={34:"den",24:"webs",23:"fete"}
print(sorted(student.items()))

# this returns the removed name

list=["yasmin","judy","lorna"]
def remove_item():
 y=list.pop(1)
 print(y)
remove_item()
# #prints out the names remaining    
# def names(x):
#    x.pop()
#    print(x)
# names(["judy","yasmin","mitchelle","lorna"])

# d = {"key1": 10, "key2": 23}

# if 10 in d.values():
#     print("True")
# um=[1,2,3,4,5,6,7]
# first=0
# last=len(num)-1
# middle=(first+last)//2
# num[2]
# print(num[middle])
# # printing element at index five to eleven
# num[5]=11
# print(num)
# num[2]='student'
# num[1]='mother'
# print(num)
# # looping through indexes
# for x in range(len(num)):
#     print(x)
# # looping through elements
# for x in num:
#     print(x)
#     #  Write a Python program to create a tuple with different data types.
# items=("false",3.2,1,)
# print("items")
# # Given a tuple of lists, write a Python program t unpack the elements of the lists that are packed inside the given tuple.
# fruits=["apple","banana","watermelon","guava",]
# new_list=[]
# for x in fruits:
#     if "a" in x:
#      print(new_list.append(x))
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# newlist = [x for x in fruits if "a" in x]

# print(new_list)

# def num():
#     x=[1,2,3,4,5,6,7]
#     x.sort(reverse=True)
#     print(x)
# num() 
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)       





#  Write a Python program to slice a tuple.
tuplex=(29,7,4,2,20,31)
y=tuplex[3:5]
print(y)

#  Write a Python program to convert a tuple into a dictionary.
tup = ((11, "eleven"), (21, "mike"), (19, "dustin"))
dct = dict((y, x) for x, y in tup)
print(dct)
#  Write a Python program to print a tuple with string formatting.
t = (100, 200, 300)
print('This is a tuple {}'.format(t))

