
# # Write a Python program to print all prime numbers between 1 and 100.

# # def is_prime(num):
# #     if num < 2:
# #         return False
# #     for i in range(2, int(num**.5)+ 1):
# #         if num % i == 0:
# #             return False
    
# #     return True

# # for num in range(1, 100):
# #     if is_prime(num):
# #         print(num, end=" ")


# #Create a simple calculator that can add, subtract, multiply, or divide two numbers based on user input.

# # def add(a, b):
# #     return a + b

# # def subtract(a, b):
# #     return a - b

# # def multiply(a, b):
# #     return a * b

# # def divide(a, b):
# #     if b == 0:
# #         return "error! for zero"
# #     return a / b

# # print("select operationL:")
# # print("1. Add")
# # print("2. Subtract")
# # print("3. multiply")
# # print("4. divide")

# # choice = input("Enter choice (1/2/3/4): ")

# # if choice in ["1", "2", "3", "4"]:
# #     num1 = float(input("Enter first number:"))
# #     num2 = float(input("Enter second number:"))

# #     if choice == "1":
# #         print(f"the result is: {add(num1, num2)}")

# #     if choice == "2":
# #         print(f"the result is: {subtract(num1, num2)}")

# #     if choice == "3":
# #         print(f"the result is: {multiply(num1, num2)}")

# #     if choice == "4":
# #         print(f"the result is: {divide(num1, num2)}")

# # else:
#     # print("Invalid input")    

 

# #Fibonacci series

# # def fib(n):
# #     if n == 0:
# #         return 0
# #     if n == 1:
# #         return 1
# #     x = fib (n - 1)
# #     y = fib (n - 1)
# #     return x + y
# # print(fib(5))
     

# # A = [2, 4, 5, 12, 34, 55, 64]

# # for i in range(1, 101):
# #     if i not in A:
# #         print(i)



# # A = [88, 43, -33, 99, 32, 65, 43, 12]

# # def min_number(A):
# #      i = 0
# #      sz = len(A)
# #      m = A[0]
# #      idx = 0
# #      while i < sz:
# #         if m > A[i]:
# #           m = A[i]
# #           idx = i
# #         i += 1
# #      return m, idx

# # def min_sort(A):
# #     i = 0 
# #     sz = len(A)
# #     B = []
# #     while i < sz:
# #         m, idx = min_number(A)
# #         B.append(m)
# #         A.pop(idx)
# #         i += 1
# #     return B
# # print(min_sort(A))



# # def max_number(A):
# #     i = 0
# #     sz = len(A)
# #     m = A[0]
# #     idx = 0
# #     while i <sz:
# #         if m < A[i]:
# #             m = A[i]
# #             idx = i
# #         i += 1
# #     return m, idx

# # def max_sort(A):
# #     i = 0
# #     sz = len(A)
# #     B = []
# #     while i < sz:
# #         m, idx = max_number(A)
# #         B.append(m)
# #         A.pop(idx)
# #         i += 1
# #     return B
# # print(max_sort([34, 534, -33, 54, 23, 534, 633, 23]))


# # A = [22, 54, 88, 44, 44, 54, 66, 122, 122, 344, 344, 500, 500, 500]
# # cheched = []
# # i = 0
# # while i < 501:
# #     cheched.append(False)
# #     i += 1

# # for n in A:
# #     if cheched[n] is False:
# #      print(n)
# #      cheched [n] = True

# # A = [22, 54, 88, 44, 44, 54, 66, 122, 122, 344, 344, 500, 500, 500]
# # cheched = []
# # i = 0
# # while i < 501:
# #     cheched.append(False)
# #     i += 1


# # for i in A:
# #     counter[i] = counter[i] + 1
# # for i in A:
# #    print(i, ":", counter[i])
    
# # A = [22, 54, 88, 44, 44, 54, 66, 122, 122, 344, 344, 500, 500, 500]
# # checked = [False] * 501  

# # def count_occurrences(A):
  
# #     counts = [0] * 501 

   
# #     for n in A:
# #         counts[n] += 1


# #     for n in A:
# #         if not checked[n]:
# #             print(f"{n} : {counts[n]}")
# #             checked[n] = True

# # count_occurrences(A)


# #palindrom

# # def is_palindrom(A):
# #     flag = True
# #     sz = len(A)
# #     i = 0
# #     while i < sz:
# #         if A[i] != A[sz - 1 - i]:
# #             flag = False
# #             break
# #         i += 1
# #     return flag
# # print(is_palindrom("maam"))

# #small to big
# # A = [1, 3, 42, 11, 6, 23, 54, -65, 99]
# # B = []
# # def min_no(A):
# #     sz = len(A)
# #     i = 0
# #     m = A[0]
# #     idx = 0
# #     while i < sz:
# #         if m > A[i]:
# #             m = A[i]
# #             idx = i
# #         i += 1
# #     return m, idx
# # def min_sort(A):
# #     i = 0
# #     sz = len(A)
# #     B = []
# #     while i < sz:
# #         m, idx = min_no(A)
# #         B.append(m)
# #         A.pop(idx)
# #         i += 1
# #     return B

# # print(min_sort(A))


# #what no is missing in 1 to 100

# # A = [3, 5, 6, 7, 3, 22, 45, 65, 43]

# # for i in range(1, 101):
# #     if i not in A:
# #         print(i)

# #PRIME NUMBER PRINT USE CHECKER BOARD




# #A list where a no have what time

# # A = [2, 2, 2, 2, 4, 5, 4, 5, 7, 8, 8, 9, 9, 97, 9, 500, 500, 43, 43]
# # checked = {}
# # i = 0
# # for number in A:
# #     if number in checked:
# #         checked[number] += 1
# #     else:
# #         checked[number] = 1
# # for number, cnt in checked.items():
# #     print(number, ":", checked[number])

# #fib series

# # def fib(n):
# #     if n == 0:
# #         return 0
# #     if n == 1:
# #         return 1
# #     x = fib(n - 1)
# #     y = fib(n - 2)

# #     return x+y
# # print(fib(7))


# #Fandamental Therim Arithmetic - FTA

# def find_all_factors(n):
#     factors = []
#     i = 1
#     while i <= n:
#         if n % i == 0:
#             factors.append(i)
#         i += 1
#     return factors

# def is_prime(n):
#     factors = find_all_factors(n)
#     if len(factors) == 2:
#         return True
#     else:
#         return False

# def prime_expo(n, a):
#     cnt = 0
#     while True:
#         if n%a == 0:
#             cnt += 1
#             n = n//a 
#         else:
#             break
#     return cnt

# def prime_factorization(n):
#     factors = find_all_factors(n)
#     pf = []
#     i = 0
#     s = len(factors)
#     while i < s:
#         if is_prime(factors[i]):
#             pf.append(factors[i])
#         i += 1
#     prime_factor = {}
#     s = len(pf)
#     i = 0
#     while i<s:
#         U = pf[i]
#         prime_factor[U] = prime_expo(n, U)
#         i += 1
#     return prime_factor

# print(prime_factorization(12))

# nums = [4,5]
# def twoSum(self, nums: int, target: int) -> int:
#     for i in range(len(nums)):
#         for j in range(i + 1, len(nums)):
#             if nums[j] == target - nums[i]:
#                 return [i, j]
#         # Return an empty list if no solution is found
#     return []

nums = [2,7,4,3]
i = 0
target = 9
A = len(nums)
for i in range (len(nums)):
    if A[i]==target:
        print(i)
    else:
        print("not found")
        
