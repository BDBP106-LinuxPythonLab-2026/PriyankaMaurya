# Q1. Print a string in title case
a = input("Enter a string: ")
b = a.title()
print("Title case:", b)

# Q2.
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest in %: "))
t = float(input("Enter time in years: "))
si = (p*r*t) / 100
total_amount = p + si
print("Simple Interest:", si)
print("Total Amount:", total_amount)

# Q3.
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")

# Q4.
import math
angle = float(input("Enter angle in degrees: "))
radians = math.radians(angle)

# 6 trignometric funtions are:
sin= math.sin(radians)
cos= math.cos(radians)
tan= math.tan(radians)
cosec = 1 / sin
sec = 1 / cos
cot = 1 / tan
print("sin =", sin)
print("cos =", cos)
print("tan =", tan)
print("cosec =", cosec)
print("sec =", sec)
print("cot =", cot)

# Q5.
import math
a=float(input("Enter a value: "))
b=float(input("Enter b value: "))
c=float(input("Enter c value: "))

d = b**2-4*a*c
if a==0:
    print("The equation is undefined")
elif d > 0:
    root1=(-b+math.sqrt(d))/(2*a)
    root2=(-b-math.sqrt(d))/(2*a)
    print("Root1=",root1)
    print("Root2=",root2)

elif d == 0:
    root = -b / (2*a)
    print("Both roots are equal:", root)
else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-d) / (2 * a)
    print("Root1 =", real, "+", imaginary,"i")
    print("Root2 =", real, "-", imaginary,"i")

# Q6.
n = int(input("Enter a number: "))
sum = 0

while n > 0:
    digit = n % 10    
    sum += digit        
    n //= 10          

print("Sum of digits =", sum)

# Q7.
n = int(input("Enter a number: "))
original = n
reversed = 0

while n > 0:
    digit = n % 10
    reversed = reversed * 10 + digit
    n //= 10

if original == reversed:
    print("Yes, it is a palindrome.")
else:
    print("No, it is not a palindrome.")

# Q8.
x = float(input("Enter x-coordinate: "))
y = float(input("Enter y-coordinate: "))

if x > 0 and y > 0:
    print("The point lies in the First Quadrant")
elif x < 0 and y > 0:
    print("The point lies in the Second Quadrant")
elif x < 0 and y < 0:
    print("The point lies in the Third Quadrant")
elif x > 0 and y < 0:
    print("The point lies in the Fourth Quadrant")
else:
    print("The point lies on an axis")

# Q9.
n = int(input("Enter a number: "))

reversed = 0

while n > 0:
    digit = n % 10
    reversed = reversed * 10 + digit
    n //= 10

print("Reversed number =", reversed)    

# Q10.
n=int(input("Enter a number: "))
if n % 2 == 0:
    print("Even number")
else:
    print("Odd number")

# Q11.
letter = input("Enter a letter: ")
alphabet = letter.lower()

if alphabet in "aeiou":
    print("Vowel")
else:
    print("Consonant")    

# Q12.
str = input("Enter a string: ")
str = str.lower().replace(" ", "")
reverse = str[::-1]
if str == reverse:
    print("Yes, it is palindrome string")
else: 
    print("No. it is not a palindrome string")

# Q13.
n = int(input("Enter a number: "))
fact = 1

while n > 0:
    fact = fact * n
    n = n - 1

print(f"The factorial of {n} is {fact}") 

# Q14.
f0 = 0
f1 = 1

print(f0)
print(f1)

for i in range(2, 26):
    f2 = f0 + f1
    print(f2)

    f0 = f1
    f1 = f2

# Q15.
import math

x1 = float(input("Enter x-coordinate of first point (x1): "))
y1 = float(input("Enter y-coordinate of first point (y1): "))
x2 = float(input("Enter x-coordinate of second point (x2): "))
y2 = float(input("Enter y-coordinate of second point (y2): "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
print(f"The distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance}")

# Q16.
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))

if a == b and b == c and c == a:
    print("Equilatoral triangle")
elif a == b or b == c or c == a:
    print(" Isosceles triangle")
else:
    print("Scalene triangle")

    



