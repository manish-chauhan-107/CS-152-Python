#MY FRIST CODE IN PYTHON
print ("hello manish chauhan")

#SUM AND DIFFERENCE OF TWO NUMBER GIVEN BY USER
m = int(input("enter number"))
n = int(input("enter number"))
print ("sum is ", m+n )
print("difference is" , m-n)

#CODE TO FIND A NUMBER GIVEN BY USER IS ODD , EVEN , POSITIVE , NEGATIVE
Num = int(input("enter number "))
if Num < 0:
  print ("Negative number")
elif Num == 0:
  print ("ZERO nither positive nor negative")
else :
  print ("Positive number")
  if Num % 2 != 0 :
    print ("odd number")
  else :
    print ("even number")
print ("Thank you have a nice day")

#CHECK ELIGIBILITY FOR VOTE
name = input("enter name :")
age = int(input("enter age :"))
if age >= 18 :
  print (name ,"you are eligible for vote")
else :
    print (name, " you are a minor now ")
  
#TAKE A CHARACTER AS AN INPUT
character = (input("enter character"))
print (character * 10)

#list
#it can be change
flower = ['lotus' , 'rose' , 'lily']
print (flower[2])

#Tuple
#can not change
name = ('Manish chauhan' , 'ruhul amin' , 'vishnu kant rai')
print (name[0])

#simple calculator :
Num1 = (int(input("enter number")))
Num2 = (int(input("enter 2nd number")))
value = int(input("1 for addistion , 2 for substraction , \n ,3 for multiplicatioin , 4 for division "))
match value :
  case 1 :
    print (Num1 + Num2)
  case 2 :
    print (Num1 - Num2)
  case 3:
    print (Num1 * Num2)
  case 4 :
    print ( Num1/Num2)



