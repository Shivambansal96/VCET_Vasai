
# # # # print("My name is Shivam Bansal", "SAME LINE", sep=" || ")
# # # # print("Today is Day 1 of Python")


# # # # name = "Shivam"

# # # # n = None

# # # # arr = [3, 5, 8, 9, 7]
# # # # print(8 in arr)

# # # # a = 5
# # # # a = a + 1
# # # # # a += 1
# # # # print(a)


# # # # print("---------------------")


# # # # # print(2 == 2 and 4 == 4 and 3 == 4)
# # # # print(2 == 2 or 4 == 4 and 3 == 4)
# # # # print(not (2 == 2 or 4 == 4) and 3 == 4)

# # # # a = 2
# # # # b = "4"
# # # # c = int(b)
# # # # print(a + c)


# # # name = input("Enter you name = ")
# # # marks = int(input("Enter your marks = "))

# # # print("Name =", name)
# # # print(type(name))
# # # print("------------")
# # # print("Marks =", marks)
# # # print(type(marks))

# # # print(f"My name is {name} and I got {marks} marks now.")
# # # print(f"My name is Shivam and I got 99 marks now.")



# # # # # # PRACTICE SET 2 # #  # # # #
# # # ============== SUM of 2 numbers ==================

# # a = int(input("Enter a number = "))
# # b = int(input("Enter another number = "))
# # print(f"Sum = {a + b}")

# # # ============== SUM of 2 numbers ==================
# # # ============== PRINT AREA ==================
# # side = int(input("Enter a side = "))

# # print("Area =",side ** 2)
# # # ============== PRINT AREA ==================
# # # ======= PRINT AVERAGE OF 2 FLOATING NUMS ==============
# # a = float(input("Enter a num: "))
# # b = float(input("Enter another num: "))

# # print("Average:", (a+b) / 2)
# # # ======= PRINT AVERAGE OF 2 FLOATING NUMS ==============
# # # ======= PRINT GREATER OF 2 ==============
# # a = int(input("Enter a num: "))
# # b = int(input("Enter another num: "))
# # print(a >= b)
# # # ======= PRINT GREATER OF 2 ==============

# # # ======= CONVERT CELSIUS TO FAHRENHEIT ==============
# # c = float(input("Enter the temperature: "))
# # f = (c * 9/5) + 32 
# # print(f"Temperature = {f}°F")
# # # ======= CONVERT CELSIUS TO FAHRENHEIT ==============


# a = "Shivam"
# b = "Bansal"

# print(a + " " + b)
# # print(len(a) + len(b))
# print(len(a + b))


# fName = input("Enter your first Name: ")

# print(f"Name = {fName}")
# print(f"length of {fName} = {len(fName)} characters.")

# a = input("Enter a String: ")
# print(a[0] == a[len(a) - 1])

# name = "Shivam"

# print(name[3:1:-1])
# print(name[::2])


# # # =========== PALINDROME =============
# original = "madam"
# dup = original[::-1]

# print(f"Palindrome = {original == dup}")
# # # =========== PALINDROME =============


# s = "    Shivam    "
# s = "ShiVaM Bansal Python"
# print(s[1:len(s) - 1])
# print(s[len(s) - 2: 0: -1])

# print(s.endswith("m"))
# print(s.capitalize())
# print(s.count("a"))
# print(s.find("z"))
# print(s.index("z"))
# print(s.strip())
# print(s.swapcase())
# print(s.replace("aM", "om"))
# print(s.split(" "))

# # # # #CONDITIONAL STATEMENTS # # # # # # # # #

# trafficLight = input("Enter color: ").lower()

# if(trafficLight == "red"):
#     print("STOP")
# elif(trafficLight == "green"):
#     print("GO")
# elif(trafficLight == "yellow"):
#     print("Ready TO GO")
# else:
#     print("Wrong Input")



# age = 88

# if(age >= 18 and age < 60):
#     print("Adult")
# elif(age >= 60 and age < 80):
#     print("Senior Citizen")
# elif(age >= 80):
#     print("Super Senior Citizen")
# else:
#     print("Minor")


# age = 80

# if(age >= 18):
#     if(age >= 60):
#         print("Senior Citizen")
#     else:
#         print("Adult")
# else:
#     print("Minor")


# marks = int(input("Enter marks = "))
# if(marks >= 90 and marks <= 100):
#     grade = "A"
# elif(marks >= 80 and marks < 90):
#     grade = "B"
# elif(marks >= 70 and marks < 80):
#     grade = "C"
# else:
#     grade = "F"
# print(grade)



# marks = int(input("Enter marks = "))
# if(marks >= 90):
#     grade = "A"
# if(marks >= 80):
#     grade = "B"
# if(marks >= 70):
#     grade = "C"
# else:
#     grade = "F"
# print(grade)



# num = int(input("Enter a num: "))

# if(num > 0):
#     print("Positive Number")
# elif(num < 0):
#     print("Negative Number")
# else:
#     print("Zero")


# # # # # Password Checker # # # #  # 

# password = "ShivamBansal96"
# upperCase = password.upper()
# lowerCase = password.lower()

# if(len(password) > 8):
#     if(password != upperCase and password != lowerCase):
#         print("Strong Pass")
#     else:
#         print("Weak Pass")
# else:
#     print("Weak Pass")


# # # # # EVEN OR ODD # # # #  # 

num = int(input("Enter a num: "))

if(num % 2 == 0):
    print(f"{num} is EVEN")
else:
    print(f"{num} is ODD")


# # # # # # MULTIPLE OF 7 # # # #  # 

# num = int(input("Enter a num: "))

# if(num % 7 == 0):
#     print(f"{num} is a multiple of 7")
# else:
#     print(f"{num} is NOT a multiple of 7")



# # # # # # GREATEST OF 3 # # # #  # 

# num1 = int(input("Enter a num1: "))
# num2 = int(input("Enter a num2: "))
# num3 = int(input("Enter a num3: "))

# if(num1 > num2 and num1 > num3):
#     print(f"{num1} is the greatest.")
# elif(num2 > num3):
#     print(f"{num2} is the greatest.")
# else:
#     print(f"{num3} is the greatest.")
