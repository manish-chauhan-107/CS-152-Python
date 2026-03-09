#QUESTION 13:
''' Python program to find factorial of a given number using functions.'''
def fact(x):
  if x == 1 or x == 0:
      return 1
  else :
      ans = x * fact(x-1)
  return (ans)
num1 = int(input("enter number"))
Answer = fact(num1)
print(Answer)
