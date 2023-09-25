def admin_login(username, password):
    if (username == "admin" or username == "ADMIN") and password == "12345":
        return "Access granted"
    else:
        return "Access denied"

# Test cases
# result1 = admin_login("admin", "12345")
# result2 = admin_login("ADMIN", "password123")
# result3 = admin_login("user123", "12345")

# print(result1)  # Output: "Access granted"
# print(result2)  # Output: "Access denied"
# print(result3)  # Output: "Access denied"


def hows_the_weather(temperature):
    if temperature < 40:
        return "It's brisk out there!"
    elif 40 <= temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"

# # Test cases
# temperature1 = 35
# temperature2 = 50
# temperature3 = 90
# temperature4 = 70

# print(hows_the_weather(temperature1))  # Output: "It's brisk out there!"
# print(hows_the_weather(temperature2))  # Output: "It's a little chilly out there!"
# print(hows_the_weather(temperature3))  # Output: "It's too dang hot out there!"
# print(hows_the_weather(temperature4))  # Output: "It's perfect out there!"


def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# # Test cases
# for i in range(1, 101):  # Test numbers from 1 to 100
#     print(fizzbuzz(i))



import sys

def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            print("Invalid operation: Division by zero is not allowed!")
            return None
    else:
        print("Invalid operation: " + operation)
        return None

# # Test cases
# result1 = calculator('+', 5, 3)   # Addition: 5 + 3 = 8
# result2 = calculator('-', 10, 4)  # Subtraction: 10 - 4 = 6
# result3 = calculator('*', 6, 2)   # Multiplication: 6 * 2 = 12
# result4 = calculator('/', 8, 2)   # Division: 8 / 2 = 4
# result5 = calculator('^', 5, 3)   # Invalid operation!

# print(result1)  # Output: 8
# print(result2)  # Output: 6
# print(result3)  # Output: 12
# print(result4)  # Output: 4
# print(result5)  # Output: Invalid operation!
