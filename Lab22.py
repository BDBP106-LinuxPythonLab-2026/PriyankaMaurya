# Q1. Fill in the correct piece of code below to make this decorator called greet_decorator
# work. Show that it works by taking a screenshot of the code and its output.
def greet_decorator(func):
    def wrapper():
        func()
    return wrapper
@greet_decorator
def message():
    print("This is my first attempt at using decorator.")
message()

# Q2. # Fill in the correct piece of code below to create this decorator called before_after that
# prints "Function is starting...." before the function call and prints "Function has finished!"
# after the execution.
def before_after(func):
    def wrapper():
        print("Function is starting....")
        func()
        print("Function has finished!")
    return wrapper
@before_after
def calculate():
    print("Calculating...")
calculate()

# Q3. 
count = 0
def count_calls(func):
    def wrapper():
        global count
        count += 1
        func()
        print(f"Call count: {count}")
    return wrapper
@count_calls
def say_hi():
        print("Hi!")
say_hi()
say_hi()
say_hi()

# Q4.  Write a decorator called check_positive that checks whether the argument passed to
# a function is positive. If it is positive, execute the function; otherwise, print
# "Number must be positive".

def check_positive(func):
    def wrapper(num):
        if num > 0:
            return func(num)
        else:
            print("Number must be positive")
    return wrapper

@check_positive
def display_number(num):
    print("Number is:", num, "and it is positive")

display_number(5)   # Number is: 5
display_number(-3)  # Number must be positive

# Q5. # Write a decorator measure_time to calculate how long a function takes to run. Use it
# on a function that calculates the factorial of a number. Use a test case of calculating the
# factorial of 50
import time

def measure_time(func):
    def wrapper(n):
        start = time.time()
        result = func(n)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result

    return wrapper

@measure_time
def factorial(n):
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact

print("Factorial of 50:", factorial(50))


# Q6. # Write a function population_growth(initial,rate, time) that defines an inner func-
# tion exponential_growth() using the formula N(t) = N0 + exp(rate ∗ time) where N0
# represents the initial population and N(t) is population after time t. The inner function
# returns the population after time, and the outer function rounds and prints it (already
# done in Lab 21, copy code to Lab22 folder).

# import math
# def population_growth(initial,rate, time):
#     def exponential_growth():
#         return initial + math.exp(rate*time)
#     P=exponential_growth()
#     print(round(P))
# population_growth(100,1,10)

#OR

import math
def greet(func):
    def wrapper(initial,rate,time):
        result=round(func(initial,rate,time))
        return result
    return wrapper

@greet
def population_growth(initial,rate,time):
    return initial + math.exp(rate*time)

print(population_growth(100,0.5,10))

# Q7. # Use the decorator measure_time to calculate how long the above function calculating
# population growth that loops 1 million iterations.
import math
import time

def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("Execution time:", end - start, "seconds")
        return result
    return wrapper

@measure_time
def population_growth(initial, rate, t):
    def exponential_growth():
        P = initial   # Initialize population with the initial value
        for i in range(1000000):
            P = P + math.exp(rate * t)  #Update population by adding the growth amount
        return P

    P = exponential_growth()
    print(round(P))
    return P

population_growth(100, 1, 10)


# Q8. # Write a function analyse_dna(sequence) that defines an inner function gc_content()
# to calculate GC% . The outer function should print whether the given DNA is AT rich
# or GC rich sequence. (copy this code from Lab 21 to Lab 22 folder)

def analyse_dna_decorator(func):
    def wrapper(sequence):
        gc = sequence.count('G') + sequence.count('C')
        percentage = (gc / len(sequence)) * 100

        print(f"GC Content: {percentage}%")

        if percentage > 50:
            print("GC rich sequence")
        else:
            print("AT rich sequence")

        return func(sequence)
    return wrapper

@analyse_dna_decorator
def analyse_dna(sequence):
    return sequence

analyse_dna("ATGCGTACGTCA")


# Q9. # Write a decorator log_function_call that prints Running DNA analysis.... before
# and Analysis complete! after any function. Apply it to the above function that returns
# the GC % of a DNA sequence.

def log_function_call(func):
    def wrapper(sequence):
        print("Running DNA analysis....")
        result=func(sequence)
        print("Analysis complete!")
        return result   #To preserve the original function's return value

    return wrapper
@log_function_call
def analyse_dna(sequence):
    def GC_content():
        GC=sequence.count("G")+sequence.count("c")
        return (GC/len(sequence))*100      # returning this to use this in outer (main) function
    Percentage=GC_content()
    if Percentage > 50:
        print("GC rich sequence")
    else:
        print("AT rich sequence")
    print(f"GC% in a sequence is {GC_content()} that is less than 50")
(analyse_dna("ATGCATCG"))