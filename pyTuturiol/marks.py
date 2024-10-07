m1 = int(input("enter the marsk : "))
m2 = int(input("enter the marsk : "))
m3 = int(input("enter the marsk : "))
total_makrs = m1+m2+m3
percentage =   (100*(total_makrs)/300)

print(percentage)
if(percentage>=40 and m1 >= 33 and m2 >= 33 and m3 >= 33):
    print("student grade : pass")
else:
    print("student grade : fail")