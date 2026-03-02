#QUESTION 11 :
'''Python program to create a menu with the following options 1. TO PERFORM ADDITITON 2. TO
PERFORM SUBTRACTION 3. TO PERFORM MULTIPICATION 4. TO PERFORM DIVISION Accepts users
input and perform the operation accordingly. Use functions with arguments.'''
def calculator(x , y , z):
  if z == 1:
    c = x + y
    return c
  elif z == 2 :
    c = x - y
    return c
  elif z == 3:
    c = x*y
    return c
  elif z == 4:
    c = x/y
    return c
  else :
    c = "invalid input"
    return c 
num1 = int(input("Enter number"))
num2 = int(input("Enter number"))
z = int(input(" Enter 1 for addition \n Enter 2 for substraction \n Enter 3 for mutiplication \n Enter 4 for division "))
Answer = calculator(num1 , num2 , z)
print (Answer)

#QUESTION 12 :Python program to check whether the given string is palindrome or not.
str = input("enter text : ")
m = len(str)
isPalindrome = 1
for i in range (m//2):
    if str[i] != str[m-i-1]:
       isPalindrome = 0 
       break
    else:
      isPalindrome = 1
if isPalindrome == 1 :
  print ("yes")
else:
  print("not")

