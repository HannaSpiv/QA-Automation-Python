"""
Homework (Lesson 6)
"""

"""1
Module.

- Move your functions from the previous homework to a separate file
and import them into the main (executable) file.
- Call each function one or more times in the executable file.
"""

import functions

print(functions.sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))

print(functions.is_triangle(2, 4, 9))  # False
print(functions.is_triangle(3, 4, 5))  # True

print(functions.average(1, 2, 3, 4, 5, 6, 7, 8))  # 4.5
print(functions.average())

fruits_1 = ["banana", "APPLE", "watermelon", "cherry"]
fruits_2 = ["Mango", "apple", "orange", "cherry"]

print(functions.common_strings(fruits_1, fruits_2))  # ['apple', 'cherry']


"""2
Anonymous function.

- Create an anonymous function pow that takes 2 arguments x and y.
The function should return x raised to the power of y.
"""

my_pow = lambda x, y: x ** y

print(my_pow(2, 2))


"""3
Snake.

- Create a function snake_talk that takes 1 argument text (string).
- The function should create a new string where all vowels
aeiouyAEIOUY in the text are duplicated.
- For example, snake_talk("Harry") should return "Haarryy".
"""

def snake_talk(text):
    result = ""
    for c in text:
        if c in "aeiouyAEIOUY":
            result += c * 2
        else:
            result += c
    return result


print(snake_talk("Harry"))  # Haarryy