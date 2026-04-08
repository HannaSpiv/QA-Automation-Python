"""
Homework (Lesson 5)
"""

"""1
Advanced sum.
The built-in sum() function in Python raises an error if one of the elements in the sequence is not a number, e.g. sum([1, 2, 'A']).
Write a function sum_ignore_non_numbers() that has one parameter items (list or tuple).
The function should return the sum of all numbers (int, float) in the passed sequence. All non-numeric values should be ignored.
If there are no numbers, the function should return 0.
If the function is called with the list [1, 2, 'Hey', None, 4.3], it should return 7.3"""

def sum_ignore_non_numbers(items):
    sum_ignore = 0

    for item in items:
        if isinstance(item, (int, float)):
            sum_ignore += item

    return sum_ignore

print(sum_ignore_non_numbers([1, 2, 'Hey', None, 4.3]))


"""2
Triangle.
A triangle is possible if the sum of any two sides is greater than the length of the third side.
Write a function is_triangle() that has 3 parameters - the lengths of the sides of a triangle.
The function should return True if a triangle with the given sides can exist, and False otherwise.
For is_triangle(2, 4, 9) the correct answer is False, for is_triangle(3, 4, 5) - True."""

def is_triangle(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False


print(is_triangle(2, 4, 9))  # False
print(is_triangle(3, 4, 5))  # True


"""3
Average value.
Write a function average() that takes an arbitrary number of positional arguments (any number of arguments can be passed).
The function should calculate the arithmetic mean of all passed numbers. (Assume that only numbers are passed to the function).
If no arguments are passed, the function should return 0.

A call like average(1, 2, 3, 4, 5, 6, 7, 8) should return 4.5"""

def average(*args):
    if not args:
        return 0
    return sum(args) / len(args)

print(average(1, 2, 3, 4, 5, 6, 7, 8))  # 4.5
print(average())


"""4
Common strings.
Write a function common_strings() that has 3 parameters: list1, list2 and ignore_case=True (default value).
The function should return a new list of values that appear in both lists.
If ignore_case is True, the function should ignore case and treat strings "string" and "STRING" as the same.
Otherwise, the function should take case into account and treat such strings as different.
All strings in the resulting list should be in lowercase.
For example, there are two lists:
fruits_1 = ['banana', 'APPLE', 'watermelon', 'cherry']
fruits_2 = ['Mango', 'apple', 'orange', 'cherry']
Then calling common_strings(fruits_1, fruits_2) should return ['apple', 'cherry']."""


def common_strings(list1, list2, ignore_case=True):
    result = []

    for i in list1:
        for j in list2:
            if ignore_case:
                if i.lower() == j.lower():
                    result.append(i.lower())
                    break
            else:
                if i == j:
                    result.append(i)
                    break

    unique_result = []
    for item in result:
        if item not in unique_result:
            unique_result.append(item)

    return unique_result


fruits_1 = ["banana", "APPLE", "watermelon", "cherry"]
fruits_2 = ["Mango", "apple", "orange", "cherry"]

print(common_strings(fruits_1, fruits_2))  # ['apple', 'cherry']
