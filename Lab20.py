#Q1. Ask the user for an integer. Print whether it is positive, negative or zero. If it is non-zero,
# also print whether it is even or odd. If it is divisible by both 3 and 5, print "FizzBuzz number!".

x = int(input("Enter a number: "))
if x > 0:
    print("Positive")
    if x % 2 == 0:
        print("Even")
    else:
        print("odd")

elif x < 0:
    print("Negative")
    if x % 2 == 0:
        print("Even")
    else:
        print("odd")

else: print("Zero")

if x % 3 == 0 and x % 5 == 0:
    print("Fizzbuzz number")
else:
    print("Not divisible")

#Q2. Read a sentence. Count the vowels, consonants, digits and spaces. Ignore case and punctuation.
# Enter text: Hello World 2026!

text = input("Enter a sentence: ")
T = text.lower()
vowels = 0
consonants = 0
digits = 0
spaces = 0
for x in T:
    if x in "aeiou":
        vowels += 1
    elif x.isalpha():
        consonants += 1
    elif x.isdigit():
        digits += 1
    elif x==" ":
        spaces += 1
    else:
        print("END")
        print(f"Vowels:{vowels},Consonats:{consonants},Digits:{digits},Spaces:{spaces}")

# Q3. Store a secret number between 1 and 50. Keep asking the user to guess until they get it
# right. After each wrong guess, print "Too high" or "Too low". When they get it, print how
# many attempts it took. As a bonus, stop after 7 attempts and reveal the number.

x = 15
y = int(input("Guess the number: "))
count = 0

while True:
    if y > x:
        print("Too High")
        print("Guess again")
        count +=1
        y = int(input("Guess the number: "))

    elif y < x:
        print("Too Low")
        print("Guess again")
        count += 1
        y = int(input("Guess the number: "))

    else:
        print("FOUND")
        count += 1
        print("total number of attempts count to match the final answer:", count)
        break
    if count == 7:
        print("Stop more than 7 attempts")
        print("Number is:", x)
        break


#Q4. Ask for a number n. Print an n × n multiplication table with neatly aligned columns and a header row.
n = int(input("Enter a number: "))
print(n)
for row in range (1, n+1):
 for col in range (1, n+1):
     result = row * col
     result = str(result)
     "result.r.just()"

     print(n)

# Q5.
items = []                                      

while True:                                     
    print("\n1.Add item  2.Remove item  3.View item  4.Sort item  5.Quit")
    choice = input("Enter choice: ")             
    if choice == "1":
        item = input("Enter item: ")           
        if item.lower() in [x.lower() for x in items]:
            print("Item already exists!")
        else:
            items.append(item)                  
    elif choice == "2":
        item = input("Enter item: ")           
        for x in items:                         
            if x.lower() == item.lower():       
                items.remove(x)                 
                break
        else:
            print("Item not found!")            
    elif choice == "3":
        print(items)
    elif choice == "4":
        items.sort()                            
        print("List sorted!")
    elif choice == "5":
        break                                   
    else:
        print("Invalid choice!")

# Q6. Student Grade Report
# Concepts: list of tuples, tuple unpacking, for, if/elif grading, max/min by manual tracking
# Start with:
# students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
# Print each student's letter grade (A ≥ 90, B ≥ 80, C ≥ 70, D ≥ 60, otherwise F). Then print
# the class average and the top and bottom scorers. Find the top and bottom scorers with
# a loop, not with max() and a key.

students = [("Asha", 88), ("Ravi", 72), ("Meera", 95), ("Karan", 59), ("Divya", 81)]
total=0
Top=students[0]
Bottom=students[0]

for name,marks in students:
    total=total+marks
    if marks>=90:
        grade="A"
    elif marks>=80:
        grade="B"
    elif marks>=70:
        grade="C"
    elif marks>=60:
        grade="D"
    else:
        grade="F"
    print(name,marks,grade)
    if marks>Top[1]:
        Top=(name,marks)
    if marks<Bottom[1]:
        Bottom=(name,marks)
Average=total/len(students)
print("Average:",Average)
print("Top Scorer:",Top)
print("Bottom Scorer:",Bottom)


# Q7. Word Frequency Counter
# Concepts: dictionaries, split(), strip(), lower(), get(), items()
# Read a paragraph. Count how often each word appears, ignoring case and stripping
# surrounding punctuation (.,!?;:). Print the words alphabetically with their counts.
P=input("Enter a paragraph:",)
words=P.split()
count={}
for word in words:
    word=word.strip(".,!?;:").lower()
    if word!="":
        count[word]=count.get(word,0)+1
for word,n in sorted(count.items()):
    print(word,n)
highest=0
for word,n in count.items():
    if n>highest:
        highest=n
print("Most frequent word:",)
for word,n in count.items():
    if n==highest:
        print(word)

# Q8. 
# 8. Course Enrollment Analysis
# Concepts: sets, set operations, converting lists to sets, len()
# python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
# java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
# Remove the duplicates, then print:
# • students taking both courses
# • students taking only Python
# • students taking exactly one course
# • every unique student, in sorted order
# Finally, ask for a name and say which course(s) that student is enrolled in.
python_class = ["Anil", "Bina", "Chetan", "Deepa", "Anil", "Esha"]
java_class = ["Chetan", "Farhan", "Deepa", "Gita", "Bina"]
PS=set(python_class)
JS=set(java_class)

print("Both courses students:", sorted(PS & JS))
print("Only Python courses students:", sorted(PS - JS))
print("One courses students:", sorted(PS ^ JS))
print("Every students:", sorted(PS | JS))
n= input("Enter a name:",)
if n in PS and JS:
    print("Both Python and Java")
elif n in PS:
    print("Only Python")
elif n in JS:
    print("Only java")
else:
    print("Not Enrolled")


# Q9.
# 9. Password Validator
# Concepts: "until" loop, for over characters, isupper()/islower()/isdigit(), a set of special
# characters, flags
# Keep asking for a password until it meets all of these rules:
# • at least 8 characters
# • at least one uppercase letter, one lowercase letter and one digit
# • at least one special character from {"!", "@", "#", "$", "%", "&", "*"}
# • no spaces
# • doesn't contain the word "password" in any case
# After each failed attempt, list every rule that was broken, not just the first one.
Special_ch={"!","@","$","^","%","&","*"}
while True:
    error=[]
    P=input("Enter Password:",)
    if len(P)<8:
        error.append("At least 8 characters password is required")
    u=False
    l=False
    digit=False
    special=False
    for i in P:
        if i.isupper():
            u=True
        if i.islower():
            l=True
        if i.isdigit():
            digit=True
        if i in Special_ch:
            special=True
    if u==False:
        error.append("Missing Uppercase Letter")
    if l==False:
        error.append("Missing Lowercase Letter")
    if digit==False:
        error.append("Missing Digit")
    if special==False:
        error.append("Missing Special Characters")
    if " " in P:
        error.append("No Space Allowed")
    if "password" in P:
        error.append("It cannot contain 'password'")
    if len(error)==0:
        print("Valid Password")
        break
    else:
        print("Invalid Password")
        for i in error:
            print(i)


inventory = {
"pen": (10.0, 50), # (price, quantity in stock)
"notebook": (45.0, 20),
"eraser": (5.0, 100),
"marker": (30.0, 15),
}
print(inventory)
entry=""
cart={}

while entry!="done":
    entry=input("Enter your order:<item> <quantity>")
    if entry=="done":
        pass
    else:
        order=entry.split()
        if order[0] in inventory.keys() and order[1].isdigit():
            if int(order[1])<=inventory[order[0]][1]:
                if order[0] in cart.keys():
                    cart[order[0]]=(inventory[order[0]][0],int(order[1])+int(cart[order[0]][1]))
                else:
                    cart[order[0]]=(inventory[order[0]][0],order[1])
                inventory[order[0]]=(inventory[order[0]][0],(inventory[order[0]][1]-int(order[1])))
            else:
                print("ERROR:insufficient stock")
        else:
            print("ERROR:invalid order")

item=list(cart.keys())
quantity=list(cart.values())
print("item".ljust(10),"Quantity".ljust(10),"Unit_price".ljust(10))
total=0
for i in range(0,len(item)):
    print(item[i].ljust(10),str(quantity[i][1]).ljust(10),str(quantity[i][0]).ljust(10))
    total+=float(quantity[i][1])*quantity[i][0]

print("Total :",total)
if total>500:
    print("Yay! you got a !0 % discount!")
    total=total*0.9
    print("Your new total is :",total)

print("Current inventory: ",inventory)

inv=list(inventory.items())
for i in range(0,len(inv)):
    if inv[i][1][1]<10:
        print("LOW STOCK : ",inv[i][0])            
                


        

