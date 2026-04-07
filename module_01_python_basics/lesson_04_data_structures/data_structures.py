"""
Homework (Lesson 4)
"""

"""1 Special Numbers.
Generate a list 'numbers' consisting of numbers in the range from 0 to 100 inclusive that are divisible by both 2 and 3.
Print the 'numbers' list to the screen.
Answer: [0, 6, 12, 18, 24, 30, 36, 42, 48, 54, 60, 66, 72, 78, 84, 90, 96]"""

# attempt 1

numbers = []
for i in range(101):
    if not i % 2 and not i % 3:
        numbers.append(i)
print(numbers)


numbers_2 = [i for i in range(101) if not i % 2 and not i % 3]
print(numbers_2)


# attempt 2

numbers = []
n = 0
while n < 101:
    if n % 2 == 0 and n % 3 == 0:
        numbers.append(n)
    n += 1
print(numbers)


"""2 Filter.
There is a list: items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]
Create a new list 'numbers' that contains only integers (int) and floats (float) from the 'items' list.
Print the sum of the numbers in 'numbers'.
Answer: 291.52"""

items = [1.2, 3, None, 100, {'info': 'bla-bla'}, 44, 'Hi!', 99, 44.32, None]

numbers = []
for item in items:
    if isinstance(item, (int, float)):
        numbers.append(item)

total = sum(numbers)
print(total)


"""3 Message History.
Create a list 'messages' to store "messages".
The program should continuously ask the user to enter a message (string) from the keyboard and save it to the 'messages' list.
The program should remember no more than the last 5 messages. If the length of 'messages' exceeds 5, the first message should be removed.
If the user enters "Bye", the program should print "Alright, bye!" and the list of last messages.

Example: if the user enters the following messages: "Hello!", "How are you?", "How's your mood?", "Blah-blah-blah", "What's new?", "Sorry I'm busy", "Bye"
The program should output:
Alright, bye!
['How's your mood?', 'Blah-blah-blah', 'What's new?', 'Sorry I'm busy', 'Bye']"""

last_msgs = []

while True:
    messages = input("Enter a message: ")

    if messages.lower() == "bye":
        print("Alright, bye!")
        print(last_msgs)
        break

    last_msgs.append(messages)

    if len(last_msgs) > 5:
        last_msgs.pop(0)


"""4 Shop.

There is a dictionary with products:
products = {
"apple": {"quantity": 10, "price": 100},
"banana": {"quantity": 20, "price": 50},
"orange": {"quantity": 15, "price": 80},
"grape": {"quantity": 8, "price": 120},
"milk": {"quantity": 12, "price": 90},
"bread": {"quantity": 30, "price": 40}
}
- Increase the price of all products by 20 percent.
- Delete the product "milk".
- Add the product "Salt" with quantity 7 and price 12.
- Print the total cost of all products in the store.
Answer: 6516.0"""

products = {
    "apple": {"quantity": 10, "price": 100},
    "banana": {"quantity": 20, "price": 50},
    "orange": {"quantity": 15, "price": 80},
    "grape": {"quantity": 8, "price": 120},
    "milk": {"quantity": 12, "price": 90},
    "bread": {"quantity": 30, "price": 40}
}

for item in products:
    products[item]["price"] = products[item]["price"] * (1 + 20 / 100)

del products["milk"]

products["Salt"] = {"quantity": 7, "price": 12}

products_sum = 0
for item in products:
    products_sum += products[item]["price"] * products[item]["quantity"]

print(products_sum)


"""5 Alice.
There are two lists of equal length:
keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education', 'company', 'salary']
values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890', 'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

- Create a dictionary 'info' from the 'keys' and 'values' lists. (Each value occupies the same position as the key in the other list)
- Print the 'info' dictionary to the screen."""

keys = ['name', 'age', 'city', 'occupation', 'email', 'phone', 'hobby', 'education',
'company', 'salary']

values = ['Alice', 30, 'New York', 'Engineer', 'alice@example.com', '+1234567890',
'Reading', 'Masters in Computer Science', 'TechCorp', 90000]

info = {}

for i in range(len(keys)):
    info[keys[i]] = values[i]

print(info)


"""6 Cipher.

There is a message (string):
"Qxx7M!rrLLL#9Afxыыf2Z#gA%rL1xgQaT@HппnL0LJK3Pgn^8$Mxяя@DD^$YHZ@CC--"
And a cipher key where each letter should be replaced with its value in the dictionary:
cipher = {'1': 'a', 'Q': 'h', 'x': 't', '7': 'p', 'M': 's', '!': ':', 'r': '/', 'L': 'w', '#': '.', '9': 'y', 'A': 'o', 'f': 'u', '2': 'b', 'Z': 'e', 'g': 'c', '%': 'm', 'T': 'v', '@': '=', 'H': 'd', 'n': 'Q', '0': '4', 'K': 'W', '3': 'g', 'P': 'X', '8': 'l', '$': 'i', 'Y': 'n', 'C': '5', 'D': 'L', '^': '&', 'V': '6', 'B': '7', 'E': '8', 'J': '9', 'S': '0', 'U': '1', 'I': '2', 'O': '3', 'a': '?', 'd': 'k', 'q': 'z'}

- Decrypt the secret message using the cipher key. Garbage values (not in the dictionary) should be skipped and not added to the result.
- Print the result to the screen.
- Bonus: Write a program that takes a string from keyboard input and "sends" an encrypted response to the agent."""

cipher = {'1': 'a', 'Q': 'h', 'x': 't', '7': 'p', 'M': 's', '!': ':', 'r': '/', 'L': 'w', '#': '.', '9': 'y', 'A': 'o', 'f': 'u', '2': 'b', 'Z': 'e', 'g': 'c', '%': 'm', 'T': 'v', '@': '=', 'H': 'd', 'n': 'Q', '0': '4', 'K': 'W', '3': 'g', 'P': 'X', '8': 'l', '$': 'i', 'Y': 'n', 'C': '5', 'D': 'L', '^': '&', 'V': '6', 'B': '7', 'E': '8', 'J': '9', 'S': '0', 'U': '1', 'I': '2', 'O': '3', 'a': '?', 'd': 'k', 'q': 'z'}

# Decryption
s = "Qxx7M!rrLLL#9Afxыыf2Z#gA%rL1xgQaT@HппnL0LJK3Pgn^8$Mxяя@DD^$YHZ@CC--"
s_new = ""
for i in s:
    if i in cipher:
        s_new += cipher[i]
print(s_new)

# Encryption (Bonus)
reverse_cipher = {v: k for k, v in cipher.items()}

s_decode = input("Enter a string to encrypt: ")
s_code = ""

for char in s_decode:
    if char in reverse_cipher:
        s_code += reverse_cipher[char]
    else:
        s_code += char

print(s_code)
