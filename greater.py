# write the python program to find the greatest number of four number enter by user and store the data in list

li = set()
no1 = int(input("enter the first number : "))
li.add(no1)

no2 = int(input("enter the second number : "))
li.add(no2)

no3 = int(input("enter the third number : "))
li.add(no3)

no4 = int(input("enter the forth number : "))
li.add(no4)


print(li)

if(no1>no2 and no1>no3 and no1>no4):
  print("the gretest no is : ", no1)
elif(no2>no1 and no2>no3 and no2>no4):
    print("the gretest no is : ", no2)
elif(no3>no1 and no3>no2 and no3>no4):
    print("the gretest no is : ", no3)
elif(no4>no1 and no4>no2 and no4>no3):
    print("the gretest no is : ", no4)
