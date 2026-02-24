#Implementation of function
'''def function_name(parameters):
      code block
    return value'''
#example
def add(a, b):
    return a + b

result = add(5, 3)
print(result)

#Question 8 : Python program to store N numbers in a list and count the total positive, negative, odd and even numbers [0<0<11]
nums = [] #difine a list for store numbers
negative = 0
positive = 0
even = 0
odd = 0
print("Number of input you want to check :")
N = int(input("ENTER "))
for i in range (0 , N):
  nums.append(int(input("Enter: ")))
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

#Question 7 : Python program to store ten numbers in a list and find the largest and smallest
number = [] #difine a list for store numbers
for i in range (0 , 10):
  number.append(int(input("Enter: ")))
print("You enter these numbers:")
print(number)
number.sort()
print("largest number is :",number[9])
print("smallest number is :",number[0])
