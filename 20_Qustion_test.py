# Print all even numbers between two user inputs (inclusive).
def even_odd():
    start = int(input("enter the first number: "))
    End = int(input("enter the end number: "))
    for i in range(start, End+1):
        if i % 2 == 0:
            print(i, end=" ")
# print(even_odd())            

# Count and print how many vowels appear in a user-given string.
def vowels():
    string = input("enter ur string: ")
    count =0
    Vowels = "AIEOUaieou"

    for char in string:
        if char in Vowels:
            count+=1
    
    return count

# print(vowels())

# Continuously take integer inputs and sum them until the user enters 0.
def zero_sum():
    total = 0
    while True:
        num = int(input("Enter a number where u wont: "))
        if num == 0:
            break
        total += num
    print(f"the total number where input is 0: {total}")
# print(zero_sum())

# Generate a multiplication table (up to 10) for a given number.
def maltiply_table():
    num = int(input("Enter a number: "))
    for i in range(0,11):
        print(f"{num} X {i} = {num*i}")
    
# print(maltiply_table())

# Check if a given number is prime using a loop.
def prime_num():                   
    num = int(input("Enter a number: "))

    if num > 1:
        is_prime = True
        for i in range(2,num):
            if num%2 ==0:
                is_prime = False
                break
        if is_prime:
            print(f"{num} is prime number")
        else:
            print(f"{num} not a prime number")
    else:
        print("Enter a Greater number")

# print(prime_num())

# FizzBuzz Variation
'''
Print numbers from 1 to n, but:
“Fizz” if divisible by 3
“Buzz” if divisible by 5
“FizzBuzz” if divisible by both
'''
def FizzBuzz():
    num= int(input("Enter a number"))
    for i in range(1,num+1):
        if i % 3 == 0 and i % 5 ==0:
            print("fizzBuzz")
        elif i %3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

# print(FizzBuzz())

# Calculate factorial using only loops.
def factorial(num):
    calculate = 1
    for i in range(2,num+1):
        calculate *=i

    return calculate

# print(factorial(5))
# Reverse a given string without using slicing ([::-1]).
def Reverse_String():
    text = input("Enter the strings: ")
    
    reversed_text = ""

# Loop through each character
    for char in text:
        reversed_text = char + reversed_text   # prepend character
    
    return reversed_text

# print(f'reverse the string: {Reverse_String()}')

# Check if a password is at least 8 chars long, contains a digit, uppercase, lowercase, and special character.
def passwordChaker(password):
    length = len(password)
    digit = any(ch.isdigit() for ch in password)
    upper = any(ch.isupper() for ch in password)
    lower = any(ch.islower() for ch in password)

    if all([length,digit, upper, lower]):
        return 'stronge password'
    else:
        return 'weak password'

# pwd = input("enter ur password")
# passwordChaker(pwd)

# Randomly generate a number (1–100) and let the user guess until they get it right.
import random
def Randamly_Genrate():
    n=random.randint(1,1000)
    a=-1
    gasess=0
    while(a!= n):
        gasess+=1
        a= int(input("Gass the number: "))
        if(a>n):
            print("Lower Number Please ")
        else:
            print("Higher Number Please ")

    print(f"Your gassed the number currectly in {gasess} attempt")

# Randamly_Genrate()

# Find the Greatest Common Divisor (GCD) of two numbers without using built-in functions.
def GCD(x,y):
    res = min(x,y)

    while res>1:
        if x %res==0 & y% res==0:
            break
        res-=1
    
    return 1

# print(GCD(3,4))

# Create a pyramid pattern of numbers up to n rows.
def pyramid(n):
    for i in range(n):
        print(" " * (n-i) + "*" * (2*i-1))

print(" pyramid triangle pattern: ")
pyramid(5)

# Input two numbers and print all prime numbers between them.
def prime_number():
    pass

# Remove duplicates from a list while keeping the original order.
def Remove_duplicate():
    pass

# For a given number, print the Collatz sequence until it reaches 1.
def Collatz_Sequence():
    pass

# Find all palindrome numbers between 1 and 1000.
def palindrome():
    pass

# Print all Armstrong numbers between 1 and 1000.
def All_Armstrong():
    pass

# Count frequency of each character in a string using loops only.
def frequency():
    pass

# For a square matrix (list of lists), calculate the sum of both diagonals.
def Square_matrix():
    pass

# Create a right triangle star pattern, but skip printing a star if both row and column are even.
def triangel_right():
    pass
