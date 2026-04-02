"""
Lesson 2: Variables, input, print, and type conversion.
"""

# Task 1: Fix variable names
# 1num = 100          # cannot start with a number
# имя = "Алексей"     # allowed, but not recommended (non-English)
# First_Number = 1    # valid, but not snake_case
# "Мой текст" = text  # cannot assign to a string literal
# phone_number = "Hi!"  # name doesn't match value

# Corrected version:
first_num = 100
name = "Alexey"
first_number = 1
text = "Мой текст"
phone_number = "3823456789"
greeting = "Hi!"


# Task 2: Create a variable named 'name' with a string value representing your name.
# Then display the string as follows: 'Hi, my name is <your name>.'
name = input("Enter your name: ")
print(f"Hi, my name is {name}.")


# Task 3: Create variables 'first_name' and 'surname' from user input.
# Display: 'Hello, my name is <First Name> <Surname>.'
# Input values should be formatted to proper case.
# Example: Input "hAnNa" and "spivACHUK" -> Output "Hello, my name is Hanna Spivachuk."
first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
print(f"Hello, my name is {first_name.title()} {surname.title()}.")


# Task 4: Create variables 'a' and 'b' from user input (numbers).
# Display the sum of the two numbers.
# Example: a = 123, b = 431 -> Output: 554
a = input("Enter number a: ")
b = input("Enter number b: ")
print(int(a) + int(b))
