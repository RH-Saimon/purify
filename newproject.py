
# Write a Python program to print all prime numbers between 1 and 100.

# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**.5)+ 1):
#         if num % i == 0:
#             return False
    
#     return True

# for num in range(1, 100):
#     if is_prime(num):
#         print(num, end=" ")


#Create a simple calculator that can add, subtract, multiply, or divide two numbers based on user input.

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "error! for zero"
#     return a / b

# print("select operationL:")
# print("1. Add")
# print("2. Subtract")
# print("3. multiply")
# print("4. divide")

# choice = input("Enter choice (1/2/3/4): ")

# if choice in ["1", "2", "3", "4"]:
#     num1 = float(input("Enter first number:"))
#     num2 = float(input("Enter second number:"))

#     if choice == "1":
#         print(f"the result is: {add(num1, num2)}")

#     if choice == "2":
#         print(f"the result is: {subtract(num1, num2)}")

#     if choice == "3":
#         print(f"the result is: {multiply(num1, num2)}")

#     if choice == "4":
#         print(f"the result is: {divide(num1, num2)}")

# else:
    # print("Invalid input")