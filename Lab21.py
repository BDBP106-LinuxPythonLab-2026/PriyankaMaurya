# Q1. Write a program to convert temperature in Celsius to Fahrenheit using map() function.
def convert(c):
    return(c*9/5)+32
celsius=[10,20,30,40]
fahrenheit=list(map(convert,celsius))
print(fahrenheit)


# Q2. # Write the above program using lambda expression.
celsius=[10,20,30,40]
fahrenheit=list(map(lambda c:(c*9/5)+32,celsius))
print(fahrenheit)

# Q3. # Write a program to convert a tuple of angles into a list of tuples with each tuple containing the sine and cosine of an angle.
import math
angles=(0,30,45,60,90)
result=list(map(lambda x:(round(math.sin(math.radians(x)),2),round(math.cos(math.radians(x)),2)),angles))
print(result)

# Q4. #Write a program to filter out the odd elements of the Fibonacci series for the first n terms.
n=int(input("Enter a number:",))
a,b=0,1
fib=[]
for i in range(n):
    fib.append(a)
    a,b=b,a+b
odd=list(filter(lambda x: x%2!=0,fib))
print("Fibonacci Series:",fib)
print("Odd elements of Fibonacci Series:",odd)


# Q5. Write a program to find the sum of all the elements in a list using lambda and reduce functions
from functools import reduce
E=[23,2,34,45]
sum=reduce(lambda x,y:x+y,E)
print(sum)


# Q6. # #Write a function called cell_metabolism that takes the number of glucose and oxy-
# gen molcules, that contains an inner function energy_output() to calculate ATP yield
# (assume 1 glucose+6 oxygen gives 38 ATP). The function should return the total ATP
# produced.

def cell_metabolism(glucose,oxygen):
    def energy_output():
        if glucose<oxygen//6:
            return glucose*38
        else:
            (oxygen//6)*38
    return energy_output()
print(cell_metabolism(2,24))

# Q7. # #Write a function analyse_dna(sequence) that defines an inner function gc_content()
# to calculate GC% . The outer function should print whether the given DNA is AT rich
# or GC rich sequence.

def analyse_dna(sequence):
    def GC_content():
        GC=sequence.count("G")+sequence.count("c")
        return (GC/len(sequence))*100
    Percentage=GC_content()
    if Percentage > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")
    print(f"GC% in a sequence is {GC_content()} that is less than 50")
(analyse_dna("ATGCATCG"))


# Q8. # Write a function protein_energy_temp() with an inner function
# calculate_free_energy(enthalpy, entropy) that computes ∆G = ∆H − T ∆S. Use
# random or user-input ∆H, ∆S and return stability (”stable’ if ∆G < 0).
def protein_energy_temp():
    H = float(input("Enter a Enthalpy of rxn:", ))
    T = float(input("Enter a Time in Kelvin:", ))
    S = float(input("Enter Entropy of rxn:", ))

    def calculate_free_energy(H,T,S):
        return H-T*S
    G=calculate_free_energy(H,T,S)
    if G>0:
        return "stable"
    else:
        return "unstable"
print(protein_energy_temp())


# Q9. # Write a function population_growth(initial,rate, time) that defines an inner func-
# tion exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0
# represents the initial population and N(t) is population after time t. The inner function
# returns the population after time, and the outer function rounds and prints it.
import math
def population_growth(initial,rate, time):
    def exponential_growth():
        return initial + math.exp(rate*time)
    P=exponential_growth()
    print(round(P))
population_growth(100,1,10)


# Q10. #Write a program to extract all vowels in a given string using list comprehension.
s=input("Enter a string:",)
V=[i for i in s if i.lower() in "aeiou"]
print(V)

# Q11.
# Write a program to concatenate a list of strings to make a sentence using reduce function.
from functools import reduce
w=["Have","a","nice","day"]
S=reduce(lambda x,y:x+" "+y,w)
print(S)