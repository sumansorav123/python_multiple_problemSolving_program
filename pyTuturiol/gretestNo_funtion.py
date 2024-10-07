# write a program using function to find the greatest of three no. 

# take the three number from user 
no1 = int(input("Enter first number: "))
no2 = int(input("Enter second number: "))
no3 = int(input("Enter third number: "))

# define the function to find the greatest number
def greatest():
    if(no1>no2 and no1>no3):
        print(f"greatest number is : {no1}")
    elif(no2>no1 and no2>no3):
        print(f"greatest number is : {no2}")
    elif(no3>no1 and no3>no2):
        print(f"greatest number is : {no2}")
    else:
        print("all number are equal")

# call the function

greatest()