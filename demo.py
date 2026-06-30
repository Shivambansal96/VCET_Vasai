# # # print("Shivam","Bansal", end="---")
# # # print("Today is Day 1 of Python for Golden Batch.")

# # name = "Shivam"
# # print("a" in name)

# # # '''
# # # print("a" in name)
# # # print("a" in name)
# # # print("a" in name)
# # # print("a" in name)
# # # '''


# # name = "Shivam"
# # age = 27
# # city = "Hyd"

# # # print("My name is ", name , " I am ", age ," years old and I live in ", city, ".")
# # print(f"My name is {name}, I am {age} years old and I live in {city}.")



# # # print("35°F")

# # name = "Shivam"
# # lName = "Bansal"

# # print(name + " " + lName)


# # print(name[5::-1])
# # print(name[1:len(name) - 1])
# # print(name[len(name) - 2: 0 : -1])





# name = "               anamika  "
# # name = "SHivam"

# # print(name.capitalize())
# # print(name.count("a"))
# # print(name.endswith("vam."))
# # print(name.find("o"))
# # print(name.index("o"))
# # print(name)
# # print(name.lstrip())
# # print(name.swapcase())
# name = name.strip()
# print(name.replace("a", "b", 1))



# age = 97

# if(age >= 18 and age < 60):
#     print("Adult")
# elif(age >= 60 and age < 80):
#     print("Senior Citizen")
# elif(age >= 80):
#     print("Super Senior Citizen")
# else:
#     print("Minor")



# age = 5

# if(age >= 18):
#     if(age >= 60):
#         print("Senior Citizen")
#     else:
#         print("Adult")
# else:
#         print("Minor")


marks = 97

if(marks >= 90 and marks < 100):
    grade = "A"
if(marks >= 80):
    grade = "B"
if(marks >= 70):
    grade = "C"
else:
    grade = "F"

print(grade)