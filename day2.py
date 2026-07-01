# # arr = [1, 2, 3, 1, 2, 1]
# # arr2 = arr.copy()
# # arr2 = arr2[::-1]
# # print(f"Is palindrome? {arr == arr2}")

# # for i in range(3): # SE = 0, TC = 3,  US = 1
# # for i in range(1, 3, 2): # SE = 0, TC = 3,  US = 1
# #     print("Hello World")


# # a = 1
# # for i in range(3):
# #     print(a)
# #     a+= 1


# # for i in range(1, 3):
# #     print(i)


# # for i in range(1, 101):
#     # print(i, end=" ")

# # for i in range(100, -1, -1):
# #     print(i, end=" ")

# # for i in range(1, 6):

# #     if(i == 3):
# #         # break
# #         continue

# #     print(i)


# # n = int(input("Enter a num: "))
# # for i in range(1, 11):
# #     print(f"{n} x {i} = {n * i}")


# # n = 5
# # addition = 0
# # for i in range(n+1):
# #     addition += i

# # print(addition)


# # n = 5
# # factorial = 1
# # for i in range(1, n+1):
# #     factorial *= i

# # print(factorial)



# # arr = [("Shivam", 9), ("Alex", 98), ("Jane", 77)]
# # print(arr[1][0])
# # arr = (435, 63, 74)
# # print(arr.index(63))

# # a = (1, 2)
# # b = (3, 4)
# # c = a + b
# # print(min(c))
# # print(max(c))
# # print(c)

# # arr = list(c)
# # print(arr)



# # arr = [42, 6, 7, 8, 53, 23]

# # for i in range(len(arr)):
# #     arr[i] += 5

# # print(arr)

# # arr = [42, 6, 7, 8, 53, 23]
# # for i in arr:
# #     i += 5
# #     print(i, end=" ")

# # print(arr)


# # # ## # Linear Search # # # # # 
# # arr = [32, 4, 563, 7, 8, 24, 4]
# # target = 4
# # for i in range(len(arr)):
# #     if(arr[i] == target):
# #         print(f"Target found at index = {i}")
# #         break
# # else:
# #     print("Target NOT Found")


# # myDict = {
# #     'name': "Shivam",
# #     'age': 27,
# #     'isTeacher': True,
# #     'marks': {
# #         'python': 97,
# #         'webDev': 99,
# #         'java': 88
# #     }
# # }

# # # print(myDict['marks']['webDev'])

# # # myDict['emptyVar'] =  None

# # # print(myDict)
# # # print(myDict['name'])


# # # print(myDict['names'])
# # # print(myDict.get('names'))
# # # print(myDict.keys())
# # # print(myDict.items())
# # # print(myDict.values())

# # myDict.update({'secondEmptyVar': None})

# # print(myDict)



# # # Store the perfect squares of numbers 1- 10 in a dictionary

# # n = 10
# # myDict = {}
# # for i in range(1, n+1):
# #     myDict.update({i:i*i})

# # print(myDict)


# # setA = {53, 5, 1, 87, 54}
# # setB = {32, 5, 87, 33}

# # print(setA)
# # print(setA.pop())
# # print(setA)

# # print(setA.union(setB))
# # print(setA.intersection(setB))

# s = {9, 9.0}

# print(s)




# n = "5"
# n = int(n)


# def addition(a, b=10):
#     s = a + b
#     print(s)


# a = 5
# b = 10
# # addition(a, b)
# addition(5, 5)






# def listLen(newList):
#     print(len(newList))

#     for i in newList:
#         print(i, end=" ")

# arr = [21, 324, 5]

# listLen(arr)



# def printNto1(n):
#     print(n)

#     printNto1(n - 1)

# printNto1(3)



# def print1toN(i, n):

#     if(i >= n):
#         return

#     print(i)
#     print1toN(i + 1, n)

# n = 5
# print1toN(1, n)




# def learnStack(n):
#     if(n == 0):
#         return
    
#     print(f"INSIDE FN, BEFORE n = {n}")
#     learnStack(n - 1)
#     print(f"INSIDE FN, AFTER n = {n}")

# print("Code Starts")
# n = 3
# learnStack(n)
# print("Learning Recursion")



# def sumOfNaturalNos(n):
#     if(n == 0):
#         return 0
    
#     return n + sumOfNaturalNos(n - 1)

# n = 5
# res = sumOfNaturalNos(n)
# print(f"Sum of first {n} natural numbers: {res}")



# def factorial(n):
#     if(n == 0):
#         return 1
    
#     return n * factorial(n - 1)

# n = 5
# r = 3
# res = factorial(n)
# print(f"Factorial of {n}: {res}")


# def pORc(n , r):
#     userInput = int(input("What do you want to perform:\nPermutation - Type 1\nCombination - Type 2 = "))
#     if(userInput == 1):

#         num = factorial(n)
#         denom = factorial(n - r)

#         print(f"Permutation = {num/denom}")

#     else:

#         num = factorial(n)
#         denom = factorial(n - r) * factorial(r)

#         print(f"Combination = {num/denom}")

# pORc(n, r)



def fibonacci(n):
    if(n == 0):
        return 0
    
    if(n == 1):
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

n = 6
res = fibonacci(n)
print(res)