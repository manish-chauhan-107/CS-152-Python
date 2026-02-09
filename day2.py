#basic of division
#reminder is negative when denominator is negative
A , B , C = 5 , -2 ,2
d = A % B
e = A % C
print(d)
print(e)

#variable declaration is implicit in python
#unlike in C language we need to declarated the variable
age = 23
name = "Manish chauhan"
institute = "NIT Meghalaya"
print("Name of student : ",name ,"\n""Age of the student",age ,"\n""Institute name :", institute)

#greatest of 3 number
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))
greatest = num1
if num2 > num1:
  greatest = num2 
if num3 > num1:
  greatest = num3 
else:
  greatest = num1 
print ("the greatest number is ", greatest)


#greatest of 3 number
num1 = int(input("Enter number 1 :"))
num2 = int(input("Enter number 2 :"))
num3 = int(input("Enter number 3 :"))
greatest = num1
if num2 > num1 and num2 > num3 :
  greatest = num2
elif num3 > num1 :
  greatest = num3
else :
  greatest = num1 
print (greatest)


#equation
a = 4
b = 5
answer = (5*a+a*(pow(b,2))/pow((pow (a,2)+9) , 0.5))
print (answer)

#odd , even , positive , negative 
num = int(input("Enter number: "))
if num < 0:
  print ("Number is negative")
elif num == 0 :
  print ("Number is positive ")
else :
  if(num %2 == 0):
    print ("Number is positive and even")
  else :
    print ("Number is positive and odd ")
print ("Thank you")

#largest , second largest and smallest from 5 number
number = [ 98 , 99 , 8 , 7 , 67]
t = 0
for i in range (0 , 5):
 for j in range (0 , 5):
  if (number[i] > number[j]):
      t = number[i]
      number[i] = number[j]
      number[j] = t
print("largest number is : " ,number[0])
print("second largest number is : ", number[1])
print("smallest number is : " , number[4])

