'''
#Question -1
x1 = float(input("Enter the value of x1:"))
x2 = float(input("Enter the value of y1:"))
y1 = float(input("Enter the value of x2:"))
y2 = float(input("Enter the value of y2:"))
r = float(input("Enter the value fo radius :"))

if r<= 0:
    print("Invalid input")
    
distance= ((x2-x1)**2 +(y2-y1)**2)**1/2



if distance==r:
    print("Lies on boundary")
    
elif distance < r:
    print("Inside the circle")
        
else:
    print("Outside the circle")
'''
#Question -2
'''
import math

s= float(input("Enter the side of a regular pentagon : "))

if s <0:
    print ("Invalid side cannot be negative")
    
area = (5*s**2)/(4* math.tan(math.pi/5))

print(f"The area of pentagon is {area :.2f} :")

'''

#Question -3


'''Take 3 angles as input, and find whether they can form the angles of a triangle or not. If they can,
further classify the triangle as acute-angled, right-angled or obtuse-angled. Consider invalid cases
also'''


'''a1 = float(input("Enter first angle:  "))
a2 = float(input("Enter second angle: "))
a3 = float(input("Enter third angle:  "))

if a1 <= 0 or a2 <= 0 or a3 <= 0 or (a1 + a2 + a3 != 180):
    print("Invalid cases: These angles cannot form a triangle.")
else:
   
    if a1 < 90 and a2 < 90 and a3 < 90:
        print("It is an Acute-angled triangle.")
    elif a1 == 90 or a2 == 90 or a3 == 90:
        print("It is a Right-angled triangle.")
    else:
        print("It is an Obtuse-angled triangle.")
        
'''

#Question -4

''' Take a 4 digit number as input and find the sum of its first two digits and the sum of its last two
digits separately. Also, check if the two sums are equal or not.'''

'''num=int(input("ENTER THE NUMBER :"))

ones_digit= num%10
tens_digit= (num//10)%10
hundreds_digit= (num//100)%10
thousands_digit =( num//1000)

sum_first2 = hundreds_digit + thousands_digit
sum_last2= ones_digit+ tens_digit


print(f"the sum of first two digits are : {sum_first2}")
print(f"the sum of last two digits are : {sum_last2}")
 
if sum_first2==sum_last2:
    print("Both are equal")'''

#Question -5


''' Take a 5 digit number as input and print the largest digit of the number. Do not use any in-built
functions and do not use loops. Also print the position of that digit counted from the left. If the
largest digit occurs more than once, print the position of its first occurrence.'''



num= int(input("Enter the number : "))

#12345

d1= (num//10000)
d2= (num //1000)%10
d3= (num//100) %10
d4= (num//10)%10
d5= num % 10

'''
largest = d1
position =1

if d2>d1:
    print( f"2nd digit is largest that is {d2}")
    print( " postion = 2")

if d1>d2 and d1> d3 and d3'''









#Question -6
''' Rotate the values of three integer variables cyclically, so that the value of a moves to b, the value of
b moves to c, and the value of c moves to a, without using a fourth variable or multiple
assignment operation'''


a = int(input("Enter value for a: "))
b = int(input("Enter value for b: "))
c = int(input("Enter value for c: "))
print(f"Original values: a = {a}, b = {b}, c = {c}")

a = a + b + c   
b = a - b - c  
c = a - b - c   
a = a - b - c   
print(f"Rotated values: a = {a}, b = {b}, c = {c}")


''' a = 1 b = 2 c = 3 
 a = 6 
 b = 6 -2 - 3   = 1
 c = 6 -1-3  = 2 
 a = a - b -c = 3'''
