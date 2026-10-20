# Q1. List Comprehension
# (i) print("i)Create a list spanning 1 to 50 using list comprehension method. Call this list a.")
a=[i for i in range(1,51)]    #The first i tells Python Put the current value of i into the new list(a)
print(a)

print("ii)Slicing with positive step:")
#a
print("(a) output :", a[1:5])
#b
print("(b) output :", a[3:20:2])
#c
print("(c) output :", a[::2])
#d
print("(d) output :", a[::])
#e
print("(e) output :", a[10::2])
#f
print("(f) output :", a[1:1:1])
#g
print("(g) output :", a[:0:])
#h
print("(h) output :", a[-7::1])
#i
print("(i) output :", a[-6:])
#j
print("(j) output :", a[-10:-4])

print("(iii) Slicing with negative step:")
#a
print("(a) output :", a[::-1])  # to reverse the integer or string
#b
print("(b) output :", a[::-3])
#c
print("(c) output :", a[:1:-2])
#d
print("(d) output :", a[-1:-1:-1])
#e
print("e) output :", a[:-5:-1])
#f
print("f) output :", a[:0:-1])
#g
print("g) output :", a[:-1:-1])
#h
print("h) output :", a[0:-5:-1])
#i
print("i) output :", a[-1:5:-1])
#j
print("j) output :", a[2:2:-1])
#k
print("k) output :", a[2:1:-1])
#l
print("l) output :", a[0:-5])

print("iv) Modification of lists using list slicing:")

print("(a) Create a list of even numbers from a using list slicing technique.")
print(a[1::2])

print("(b) Create a new list from a by choosing the first 10 numbers, then the even numbers from 35-50.")
L= a[:10] + a[35:50:2]
print(L)

# Q2.
#i) Using a simple do loop structure or list comprehension, find the sum of elements in the above list a.
a=[i for i in range(1,51)]
total=0
for i in a:
    total=total+i
print(total)

#ii)Define another list b (using list comprehension again!) containing prime numbers from 1 to 50.
b = [i for i in range(2, 51) if all(i % j != 0 for j in range(2, i))]
print(b)

#iii)
c = []
i = 0
while i < len(a):
    if a[i] in b:
        c.append(a[i])
    i = i + 1
print(c)

# Q3. List comprehension with strings Use list comprehension technique you learnt in class to do the following
#(i) Using the join method.
#(a) Create a string by joining the numbers in the above list a using the comma.
#(b) Create a string by joining the numbers in the above list a using the period.
#(c) Create a string by joining the numbers in the above list a using the ‘—’.
#i)
a = ','.join([str(i) for i in range(1,51)])
print(a)

#(ii)
a = '.'.join([str(i) for i in range(1,51)])
print(a)

#(iii)
a = '_'.join([str(i) for i in range(1,51)])
print(a)

#(iv)
a = [i for i in range(1,51)]
b=[]
for i in a:
     b.append(i**2)
new = '\n'.join([str(i) + ' ' + str(i**2) for i in a])
print(new)





#a 
a=[i for i in range(1,51)]
x=",".join([str(i) for i in a])
print(x)

#b
a=[i for i in range(1,51)]
x=".".join([str(i) for i in a])
print(x)

#c
a=[i for i in range(1,51)]
x="_".join([str(i) for i in a])
print(x)
#d
a=[i for i in range(1,51)]
x=[ str(i)+ " " + str(i*i) for i in a]
print("\n".join(x))

#ii) Make a list of 10 people you know, and do the following:
#(a) Convert each element in the list to upper case using list comprehension
#(b) Swap the first name and surname of each element in the list
#(c) Join the first name and surname in each element as ’First.Last’. Note that the first letter of the first name and first letter of the surname should be upper case.
#a
p = ["kajal gupta","aman yadav","rohit yadav","priya maurya"]
P= [ i.upper() for i in p]
print(P)

#b
P2=[' '.join([i.split()[1],i.split()[0]])for i in p]
print(P2)

#c
P = [i.title().replace(' ', '.') for i in p]
print(P)

#iii) Find the longest word in this sentence using list comprehension: ”She sells sea shells that she collects from the sea floor”.
s= "She sells sea shells that she collects from the sea floor"
w= s.split()
longests = [i for i in w if len(i) == max([len(j) for j in w])]
print(longests)

#iv) Create a list of the words that are repeated in the above sentence.
s= "She sells sea shells that she collects from the sea floor"
w= s.lower().split()
duplicate = [i for i in w if w.count(i) > 1]
print(set(duplicate))


