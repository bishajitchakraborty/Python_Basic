# If else using python

print("Enter Your Marks:")
marks=int(input())

if(marks>=90):
    print("Golden A+")
elif(marks>=80 and marks<90):
    print("A+")
elif(marks>=40 and marks<80):
    print("Average")
else:
    print("Fail")
