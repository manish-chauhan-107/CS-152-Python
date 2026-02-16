#Python program to print first N numbers of Fibonacci series.
#series is like 1 ,1 , 2, 3, 5 .. (next term is sum of two previous term)
num1 = int(input("enter number"))
a = 0
b = 0
c = 1
for n in range (1 , num1+1):
  print(c)
  a = b
  b = c
  c = c + a

#Finding GCD and LCM with use of library function
import math
num1 = int(input("enter number"))
num2 = int(input("enter number"))
GCD = math.gcd(num1 , num2)
LCM = (num1*num2)//GCD
print("LCM is equal to ",LCM)
print("GCD is equal to ",GCD)

#Find the gcd and lcm of two number
num1 = int(input("enter number"))
num2 = int(input("enter number"))
if num1 > num2:
  lcm = num1
else:
   lcm = num2
while(True    ):
  if lcm % num1 == 0 and lcm % num2 == 0:
     print("LCM is equal to ",lcm)
     break
  else:
     lcm = lcm + 1
gcd = (num1*num2)//lcm
print ("GCD is equal to ",gcd)

num = int(input("Enter number: "))
isPrime = 0
if num == 2 or num == 3:
    isPrime = 1
else:
  for i in range (2 , int(num//2 + 1)):
     if num % i != 0:
       isPrime = 1
     else:
      isPrime = 0
      break
if isPrime == 1:
  print("Prime number")
else:
  print("Not a prime number")

#Python program to store N numbers in a list and count the total positive, negative, odd and even numbers [0<0<11]
nums = [] #difine a list for store numbers
negative = 0
positive = 0
even = 0
odd = 0
print("Number of input you want to check :")
N = int(input("ENTER "))
for i in range (0 , N):
  print ("Enter number",i+1 )
  nums.append(input("Enter: "))
for i in range (0 , N):
  if int(nums[i]) < 0 :
    negative = negative + 1
  elif int(nums[i]) == 0:
    positive = positive + 1
  else :
    if int(nums[i]) % 2 == 0:
      positive = positive + 1
      even = even + 1
    else:
      positive = positive + 1
      odd = odd + 1
print ("count of negative number = ",negative)
print ("count of positive number = ",positive)
print ("count of even number = ",even)
print ("count of odd number = ",odd)

#Take ten number from user in a list and and print largest and second
number = [] #difine a list for store numbers
for i in range (0 , 10):
  print ("Enter number",i+1 )
  number.append(input("Enter: "))
print("You enter these numbers:")
print(number)
number.sort(reverse=True)
print("largest number is :",number[0])
print("smallest number is :",number[-1])

#Take five number from user and and print second largest and second smallest
number = [] #difine a list for store numbers
for i in range (0 , 5):
  print ("Enter number",i+1 )
  number.append(input("Enter: "))
print("You enter these numbers:")
print(number)
number.sort(reverse=True)
print("second largest number is :",number[1])
print("second smallest number is :",number[-2])

#list method
#| No. | Method             | Purpose                                     | Example              |
#| --- | ------------------ | ------------------------------------------- | -------------------- |
#| 1   | append(x)          | Adds one element at the end of the list     | a.append(5)          |
#| 2   | extend(iterable)   | Adds multiple elements to the list          | a.extend([3,4])      |
#| 3   | insert(i, x)       | Inserts element at given index              | a.insert(1, 10)      |
#| 4   | remove(x)          | Removes first occurrence of value           | a.remove(10)         |
#| 5   | pop(i)             | Removes element at index (last if no index) | a.pop()              |
#| 6   | clear()            | Removes all elements from list              | a.clear()            |
#| 7   | index(x)           | Returns index of first occurrence           | a.index(20)          |
#| 8   | count(x)           | Counts number of occurrences                | a.count(2)           |
#| 9   | sort()             | Sorts list in ascending order               | a.sort()             |
#| 10  | sort(reverse=True) | Sorts list in descending order              | a.sort(reverse=True) |
#| 11  | reverse()          | Reverses the order of list                  | a.reverse()          |
#| 12  | copy()             | Creates a copy of the list                  | b = a.copy()         |

#use of reverse , sort and sort(reverse=True)
number = [12,13,14,45,67,54,34,23,78,87,67,76,69,97,89,45,65,78,60,41,21,26]
number.reverse()
print(number)
number.sort()
print(number)
number.sort(reverse=True)
print(number)

#use of append and count
number = [12,13,14,45,67,54,34,23,78,45,67,76,69,97,89,45,65,78,60,41,21,26]
print(number.count(45))
number.append(45)
print(number)
print(number.count(45))

#List slicing
#take a part from the middle of list
#syntex :
# list_name[starting_index : ending_index] (ending index is not include)
marks = [12,13,14,15,18,17,1,19,20,16,15,10]
print()
print(marks[6:11])
print(marks[ : 8])
print(marks[6 : ])
print (marks[-1])
print(type(marks))

#List in python
#A built-in data type that store set of value. it can store different data type
#syntex :
# variable name = [value , value1 , .....]
marks = [10,8,9,5,3]
print(marks)
print(type(marks))
print(len(marks))
