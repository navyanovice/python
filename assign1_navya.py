# Add three variables and print
a, b, c = 1, 2, 3
print(a + b + c)

# Divide and multiply 3 different numbers
print( a * b * c)
print( a / b / c)

# Write a program to accept two numbers from the user and calculate multiplication
d = int(input("enter d: "))
e = int(input("enter e: "))
print( d*e )
# Print both number and statement in one line
print("The number is: ",d*e)

# Print different data types in one line
print(f"printing different data types in one line: " + " this is a int {a}" + "this is 'float' type {a/b}" + "This is a Boolean {True}")

# Solve simple equations or operations like multiple 3 numbers in python
f = a*b*c
g = (a**2 + b**2 + c**2)

# Change the content of the variable thrice and print. 
h = 9
h = 10
h = 11
print(h)

# Accept name, age, salary of two users and print .
user1 = input("enter your name age and salary followed by space after each entry: ")
user2 = input("enter your name age and salary followed by space after each entry: ")
user1_details = user1.split()
user2_details = user2.split()
print("User1 name age and salary are", user1_details)
print("User2 name age and salary are", user2_details)



# Calculate the average salary of two user named john and anna and print.
john = 50000
anna = 80000
avg_salary = (john + anna)/2
print(avg_salary)
