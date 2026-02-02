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
