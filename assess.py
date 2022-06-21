# write a python function that takes one argument as a list a=[2,4,6,8]
#  and the second last item from that list and returns the whole list without the removed item

a=[2,4,6,8]
def remove_list(a):
    a.pop(2)
    print(a) 
remove_list([2,4,6,8])
# write a python  program that has a list days=["Monday","Tuesday","Friday","Monday"]
days=["Monday","Tuesday","Friday","Monday"]
a="Monday"
print(days.count(a))
# write a Python function named smallest that accepts a list of unsorted integers and returns the smallest number in the list.Example:
# a.smallest([3,6,8,2,4,1,5,7])
def smallest(a):
    a.sort()
    print(a[0])
smallest([3,6,8,2,4,5,7])

 # wite a function named divisible_by _seven that;using the range function and a for loop returns a list containing all the numbers  between 100 and 200 that are divisible by 7
def divisible_by_seven():
       y=[]
       for n in range(100,200):
             if n%7==0:
                   y.append(n)
                   print(y)
divisible_by_seven()                   
     

# write a python program that takes two inputs(as integers)from a user and adds the 2 numbers. checks if the sum i s greater than 10,less than 10 or equal 10 and prints a statement after each check
def sum():
 first=int(input("Enter first number:\n"))
 second=int(input("Enter second number:\n"))
 sum=first+second
 if sum>10:
    print("greater than 10")

 elif sum<10:
    print("less than 10")

 elif sum==10:
    print("equal to 10")
sum()


 # write a function that takes one argument which is a list, a=[1,2,3,4,5] and returns True if 4 is present in the list and False is 4 is not  in the list
a=[1,2,3,4,5]
def num(a):
    if 4 in a:
       print(True) 
    else:
        False
# write a function thta takes in one argument which is a list fruits=["apples","grapes","pineapple"] and removes the last fruit from list then returns  the list without the removed fruit
fruits=["apples","grapes","pineapple"]
def remove_list(fruits):
   fruits.pop()
print(fruits)
remove_list(["apples","grapes","pineapple"])
 # write a python program that takes in a list of cars ,cars=["Ford","Bmw","volovo"]
def sort(cars):
  cars=["Ford","BMW","Volvo"]
  cars.sort()
  print(cars)

sort(["Ford","BMW","Volvo"])






 
 
