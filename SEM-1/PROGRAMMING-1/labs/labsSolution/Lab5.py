a= int(input("Enter num a:"))
b= int(input("Enter num b:"))
c= int(input("Enter num c:"))

if (a<0 or b<0 or c<0):
    print("invalid input please enter positive integers")
    
if(a>b and a>c):
    print("a is largest")
elif(a==b or b==c or a==c) :
       print("Equal numbers")

if(b>a and b>c):
    print("b is largest  here ")
    
elif(c>a and c>b):
    print("c is largest")