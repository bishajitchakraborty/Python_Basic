print("Enter you number:")
number=int(input())

a=0
b=1
count=0
while(count<number):
    print(a)
    c=a+b
    a=b
    b=c
    count=count+1