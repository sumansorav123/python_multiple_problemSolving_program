
''''import pyttsx3
engine = pyttsx3.init()
engine.say("hey suman sorav what are you doing")
engine.runAndWait()'''

'''# print the content directory of os module
import os

# Function to print the content of a directory
def print_directory_content(path):
    try:
        # List all the files and directories in the given path
        with os.scandir(path) as entries:
            for entry in entries:
                print(entry.name)
    except FileNotFoundError:
        print("The directory was not found.")
    except PermissionError:
        print("You do not have permission to access this directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
print_directory_content('.')  # Replace '.' with the path you want to inspect'''

''''a = 34
a = 3.5

# Convert float to integer
a = int(a)

# Print the type of the variable

print(a)  # Output: 34 (integer)
print(type(a))  # Output: <class 'int'>

a = "34"
print(a)
print(type(a))

b = True
print(b)
print(type(b))

b=int(b)
b=str(b)
b=float(b)

print(b)'''

''''import datetime

# Get current date and time

now = datetime.datetime.now()

# Print the current date and time

print("Current date and time:", now)'''
# input function

''''a = int(input("enter the number :  "))

b = int(input("enter the second no : "))


print(type(a))

print(type(b))
print((a+b)/2)'''

'''# list 
li = [2,3,34,1,56]
li.sort()
li.reverse()
li.insert(3,45)
li.remove(1)
li.pop(1)
li.append("last")
print(li)

inputs = []
f1 = input("enter the fruit name : ")
inputs.append(f1)

f2 = input("enter the fruit name : ")
inputs.append(f2)

f3 = input("enter the fruit name : ")
inputs.append(f3)

f4 = input("enter the fruit name : ")
inputs.append(f4)

print(inputs.sort())
print(inputs)

a =  (7,0,3,0,8,0 ,0 , 4)

print(a.count(0))'''

# d = { }
# name = input("enter your 1st friend name : ")
# lang = input("enter your 1st friend name language : ")
# d[name] = lang

# name = input("enter your 2nd friend name : ")
# lang = input("enter your 2nd friend name language : ")
# d[name] = lang

# name = input("enter your 3rd friend name : ")
# lang = input("enter your 3rd friend name language : ")
# d[name] = lang

# name = input("enter your 4th friend name : ")
# lang = input("enter your 4th friend name language : ")
# d[name] = lang
# print(d)

# find = input("enter your friend name to find the select language : ")
# if(find):
#   print("friend select language : ",d[find])
#   print("do you want find the more data than type 'yes' either type 'no' : ")
#   answer = input("type yes / no :  ")
#   if(answer == "yes"):
#     find = input("enter your friend name to find the select language : ")
#     print("friend select language :",d[find])
#     print("thank you for using this service")  
# else:
#     print("thank you for using this service")  

number = 27
power_of_two = 1

while power_of_two <= number:
    power_of_two *= 2

print(power_of_two)