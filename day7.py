#QUESTION 14 :
'''Python function that takes two lists and returns True if they are equal otherwise false'''
LIST1 = []
LIST2 = []
isEqual = 1
print("Enter element of 1 list")
for i in range (0 , 5):
  LIST1.append(input("Enter: "))
print("Enter element of 2 list")
for i in range (0 , 5):
  LIST2.append(input("Enter: "))
for i in range (0 , 5):
  if LIST1[i] != LIST2[i]:
    isEqual = 0
  else :
    isEqual = 1
if isEqual == 1 :
  print ("Yes equal")
else:
  print("Not equal")


#QUESTION 15 :
''' Python program to open and write “hello world” into a file.'''
f = open("m.py")   # m.py is the file which we are going to read 
data = f.read()
print(data)
print(type(data))
f.close()
