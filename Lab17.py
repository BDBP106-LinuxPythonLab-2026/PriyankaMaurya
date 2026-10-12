# Q1.
B = input("Enter binary number: ")
Decimal = 0

for i in B:
    Decimal = Decimal * 2 + int(i)

print("Decimal number:", Decimal)

# Q2.
base = int(input("Enter base: "))
n = int(input("Enter power: "))
result = 1
for i in range(n):
    result = result * base
print("Result =", result)

# Q3. 
n = int(input("Enter number: "))
for i in range(2, n):
    if n % i == 0:
        print("Not Prime")
        break
else:
    print("Prime")

# Q4. 
n = input("Enter a number:")
for i in n:
    if i != "-":
        print(i)    

# Q5.
S = input("Enter a string: ")
middle = len(S)//2
print("First half:", S[:middle])

# Q6.
S = input("Enter a string: ")
print("Alternate characters:", S[::2])

# Q7.
S = input("Enter a string: ")
print(S.lstrip())

# Q8.
S= input("Enter a sentence: ")
Word = input("Enter a word: ")
print(S.count(Word))

# Q9.
s1=input("Enter a first string: ")
s2=input("Enter a second string: ")
if sorted(s1) == sorted(s2):
    print("It is Anagrams")
else:
    print("It is not an Anagrams")

# Q10.
L = [1,8,7,4,5,4]
for n in L:
    if n % 2 == 0:
        print(n)

# Q11.
L = [1, 2, 3, 2, 4, 1, 5, 2]

duplicates = []

for n in L:
    if L.count(n) > 1 and n not in duplicates:
        duplicates.append(n)

print("Duplicate elements:", duplicates)

# Q12.

a = [[4, 50, 6], [3, 445, 67]]
b = [[2, 6, 5], [1, 99, 5]]

c = []
d = []
e = [c, d]

for i in range(0, len(a)):
    for j in range(0, len(a[i])):
        e[i].append(a[i][j] - b[i][j])

print(str(a) + "-" + str(b) + "=" + str(e))

# Q13.
k=int(input("Enter a repeated number : "))
L=[2,2,4,4,4,5,5,5,5,6,7,8,8,8,8,8,8,8]
duplicates=[]
for i in L:
    if L.count(i) > k and i not in duplicates:
        duplicates.append(i)
print("duplicates: ",duplicates)

# Q14.
element=int(input("Enter a element to remove: "))
L=[1,2,8,8,8,4,6,5,6,7,7,7,8,5,5,2,2,2]

while element in L:
    L.remove(element)

print(L)

# Q15.

L = ["kajal", "king", "koli", "kitchen", "ball", "Pooja"]
k = input("Enter the starting character: ")

result = []

for word in L:
    if word.startswith(k):
        result.append(word)

print("Matching words:", result)



        
    