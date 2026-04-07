"""
Lesson 3: Conditionals and loops.
"""

# Task 1: Even or Odd
# Create a variable 'n' from user input (integer).
# If the number is even, print "even".
# If the number is odd, print "odd".

n = int(input("Enter a number: "))

if n % 2 == 0:
    print("even")
else:
    print("odd")


# Task 2: What Day Is It Today?
# Create a variable 'day' from user input (string).
# - If day is Saturday or Sunday → print "Today is a day off!"
# - If day is Wednesday → print "I have a dentist appointment today at 15:30"
# - Otherwise → print "Today is a regular day."

day = input("Enter day: ").lower()

if day in ("saturday", "sunday"):
    print("Today is a day off!")
elif day == "wednesday":
    print("I have a dentist appointment today at 15:30")
else:
    print("Today is a regular day.")


# Task 3: Echo
# Create variables:
# - 'n' (integer, number of repetitions)
# - 'text' (string)
# Print the string 'text' n times.

n = int(input("Enter number of repetitions: "))
text = input("Enter text: ")

for _ in range(n):
    print(text)


# Task 4: Count Vowels (Cyrillic)
# Create a variable 'message' from user input.
# Count the number of Cyrillic vowels:
# а, е, ё, и, о, у, ы, э, ю, я

message = input("Enter message: ").lower()
vowels = "аеёиоуыэюя"

count = 0

for char in message:
    if char in vowels:
        count += 1

print(count)


# Task 5: Sum of Numbers
# Ask the user to enter integers until a negative number is entered.
# Print the sum of all entered numbers (excluding the negative one).

total = 0

while True:
    num = int(input("Enter number: "))

    if num < 0:
        break

    total += num

print(total)
