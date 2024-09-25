# write the program in python to find the friend selected langauge enter  the four friend name and language name by the user
# and then find the friend who selected the language which is most frequently selected by the friends
# and print the name of the language and the name of the friend who selected the language most frequently

# Solution 1: using dictionary

d = { }
name = input("enter your 1st friend name : ")
lang = input("enter your 1st friend name language : ")
d[name] = lang

name = input("enter your 2nd friend name : ")
lang = input("enter your 2nd friend name language : ")
d[name] = lang

name = input("enter your 3rd friend name : ")
lang = input("enter your 3rd friend name language : ")
d[name] = lang

name = input("enter your 4th friend name : ")
lang = input("enter your 4th friend name language : ")
d[name] = lang
print(d)

find = input("enter your friend name to find the select language : ")
if(find == True):
  print("friend select language : ",d[find])
  print("do you want find the more data than type 'yes' either type 'no' : ")
  answer = input("type yes / no :  ")
  if(answer == "yes"):
    find = input("enter your friend name to find the select language : ")
    print("friend select language :",d[find])
    print("thank you for using this service")  
  else:
    print("thank you for using this service")  
else:
  print("friend not found in the list")
