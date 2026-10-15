# Q1.
student = {"name": "Priyanka", "age": 21}

for key, value in student.items():
    print(key, ":", value)

# Q2.
Item={'fruit':10,'vegetable':5}
sum= 0
for key in Item:
    sum += Item.get(key)   

print("Sum =", sum)

# Q3.
data = {"a": 45, "b": 12, "c": 78, "d": 23}
values = data.values()

print("Maximum:", max(values))
print("Minimum:", min(values))

# Q4.
dict = {"Gfg": [5, 7, 7, 7, 7], "is": [6, 7, 7, 7], "Best": [9, 9, 6, 5, 5]}
max_count = 0
max_key = ""
for key in dict:
    count = len(set[int](dict[key]))
    if count > max_count:
        max_count = count
        max_key = key
print(f" Key with most unique values : {max_key}")

# Q5.
sentence = ["abhi","abhi","pycharm"]
words = set[str](sentence)
print(words)

# Q6.
import math
a=23
b=15
c=20
s=(a+b+c)/2
Area= ((s*(s-a)*(s-b)*(s-c))**(1/2))
print("Area of triangle:", Area)

# Q7.

def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return "Invalid triangle"

    elif a + b <= c or a + c <= b or b + c <= a:
        return "Invalid triangle"

    elif a == b == c:
        return "Equilateral triangle"

    elif a == b or b == c or a == c:
        return "Isosceles triangle"

    else:
        return "Scalene triangle"


print(triangle(5, 5, 5))
print(triangle(5, 5, 3))
print(triangle(4, 5, 6))

# Q8.
L = [23, 32, 33, 44, 'BDBH101', 'hello', 'python', 15, 1e-10, True, 'hit']
for i in range(0, len(L) - 1, 2):     
    L[i], L[i + 1] = L[i + 1], L[i]

print(L)

# Q9.
def extract_codons(sequence, start):
    codons = []

    for i in range(start, len(sequence) - 2, 3):  
        codons.append(sequence[i:i+3])  

    return codons
sequence  = "GTTTCGATTATAACG"

print(extract_codons(sequence,0))
print(extract_codons(sequence,3))

# Q10.
def nextPrime(n):
    n = n + 1          

    while True:        
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            return n

        n = n + 1

print(f"First prime number larger than {n} is", nextPrime(n))

# Q11.



