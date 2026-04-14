"""
Homework (Lesson 9)
"""

"""
Registration (Part 1)

1. Write a function registration() that takes 2 arguments -
username (string) and password (string)
2. The function must check the username, specifically:
   a. username is a string.
   b. The length of this string is at least 4 characters and at most 15.
   c. username consists only of letters.
3. If the username is invalid, the function should raise a ValueError exception.
4. The function must check the password, specifically:
   a. password is a string.
   b. The length of this string is at least 8 characters and at most 45.
   c. password consists only of letters and digits.
5. If the password is invalid, the function should raise a ValueError exception.
6. If "registration" is successful, the function should return True."""



def registration(username: str, password: str):
    # Username validation
    if not isinstance(username, str):
        raise ValueError("Username must be a string")
    if len(username) < 4 or len(username) > 15:
        raise ValueError("Username must be between 4 and 15 characters")
    if not username.isalpha():
        raise ValueError("Username must contain only letters")

    # Password validation
    if not isinstance(password, str):
        raise ValueError("Password must be a string")
    if len(password) < 8 or len(password) > 45:
        raise ValueError("Password must be between 8 and 45 characters")
    if not password.isalnum():
        raise ValueError("Password must contain only letters and digits")

    return True


"""Bonus: create your own exception type RegistrationError and use
it instead of ValueError."""

class RegistrationError(Exception):
    pass

def registration_2(username: str, password: str):
    if not isinstance(username, str):
        raise RegistrationError("Username must be a string")
    if len(username) < 4 or len(username) > 15:
        raise RegistrationError("Username must be between 4 and 15 characters")
    if not username.isalpha():
        raise RegistrationError("Username must contain only letters")

    if not isinstance(password, str):
        raise RegistrationError("Password must be a string")
    if len(password) < 8 or len(password) > 45:
        raise RegistrationError("Password must be between 8 and 45 characters")
    if not password.isalnum():
        raise RegistrationError("Password must contain only letters and digits")

    return True