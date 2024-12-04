
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

 

#Fibonacci series

# def fib(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     x = fib (n - 1)
#     y = fib (n - 1)
#     return x + y
# print(fib(5))
     

# A = [2, 4, 5, 12, 34, 55, 64]

# for i in range(1, 101):
#     if i not in A:
#         print(i)



# A = [88, 43, -33, 99, 32, 65, 43, 12]

# def min_number(A):
#      i = 0
#      sz = len(A)
#      m = A[0]
#      idx = 0
#      while i < sz:
#         if m > A[i]:
#           m = A[i]
#           idx = i
#         i += 1
#      return m, idx

# def min_sort(A):
#     i = 0 
#     sz = len(A)
#     B = []
#     while i < sz:
#         m, idx = min_number(A)
#         B.append(m)
#         A.pop(idx)
#         i += 1
#     return B
# print(min_sort(A))



# def max_number(A):
#     i = 0
#     sz = len(A)
#     m = A[0]
#     idx = 0
#     while i <sz:
#         if m < A[i]:
#             m = A[i]
#             idx = i
#         i += 1
#     return m, idx

# def max_sort(A):
#     i = 0
#     sz = len(A)
#     B = []
#     while i < sz:
#         m, idx = max_number(A)
#         B.append(m)
#         A.pop(idx)
#         i += 1
#     return B
# print(max_sort([34, 534, -33, 54, 23, 534, 633, 23]))


# A = [22, 54, 88, 44, 44, 54, 66, 122, 122, 344, 344, 500, 500, 500]
# cheched = []
# i = 0
# while i < 501:
#     cheched.append(False)
#     i += 1

# for n in A:
#     if cheched[n] is False:
#      print(n)
#      cheched [n] = True

# A = [22, 54, 88, 44, 44, 54, 66, 122, 122, 344, 344, 500, 500, 500]
# cheched = []
# i = 0
# while i < 501:
#     cheched.append(False)
#     i += 1
# def counter(n):

#    for n in A:
#        counter[n] = counter[n] + 1
#    for n in A:
#     print(n, ":", counter[n])
    
A = [22, 54, 88, 44, 44, 54, 66, 122, 122, 344, 344, 500, 500, 500]
checked = [False] * 501  # Pre-initialize a list for tracking up to 500

def count_occurrences(lst):
    # Create a list initialized to zero for counting occurrences
    counts = [0] * 501  # Counts for numbers 0 to 500

    # Count each number in the list
    for n in lst:
        counts[n] += 1

    # Print the count of each number
    for n in lst:
        if not checked[n]:  # To avoid duplicate printing
            print(f"{n} : {counts[n]}")
            checked[n] = True

count_occurrences(A)


