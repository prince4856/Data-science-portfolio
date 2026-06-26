# Ques-1
# Make variable and print name.

# var_1= "prince kumar"
# print(var_1)


# Ques-2
# Make age variable and print

# age=18
# print(age)


# Ques no-3
# Take variable as name, college, semester and print all.

# name="prince kumar"
# college="IIT PATNA"
# semester="5^th"
# print(name,college,semester)


# Ques-4
# Make integer variable and print its type.

# roll_no=10
# print(type(roll_no))


# Ques-5
# Make float variable and print its type.

# value=10.5
# print(type(value))


#Ques-6
# Make string variable and print its type.

# city="Bikramganj"
# print(type(city))


# Ques-7
# Make boolean variable and print its type.

# val=True
# print(type(val))


#Ques-8
# Take input as name from user and print Hello prince.

# student=input("enter name:")
# print("Hello",student)
# print(f"Hello {student}")   using f-string function


# Ques-9
# Take input as age from user and print your age is 20.

# age=input("enter your age")
# print("your age is:",age)


# Ques-10
# Take two input from the user and print its sum.

# a=int(input("enter 1st no"))
# b=int(input("enter 2nd no"))
# sum=a+b
# print("sum=",sum)


# Ques-11
# Take input as length and Breadth and find its area.

# length=int(input("enter length"))
# breadth=int(input("enter breadth"))
# area=length* breadth
# print(area)


# Ques-12
# Take input as radius and find area of circle.

# radius=int(input("enter radius"))
# area_of_circle=3.14*radius*radius
# print(area_of_circle)

# Ques-13
# Take input as celsius and convert into fahrenheit.

# c=int(input("enter celsius temperature"))
# f=(c*9/5)+32
# print("value of f: ",f)


# LEVEL-3
# Ques no-14
# Take input as Name,Age,college from the user and print all at once.

# Name=input("enter name")
# Age=int(input("enter age"))
# college=input("enter college name")
# print("Name :",Name)
# print("Age  :",Age)
# print("college:",college)


# Ques-15
# Take two number as input and print addition,substraction,multiplication , division.

# a=int(input("enter 1st no"))
# b=int(input("enter 2nd no"))
# sum=a+b
# substraction=a-b
# multiplication=a*b
# division=a/b
# print(sum)
# print(substraction)
# print(multiplication)
# print(division)


# Ques-16
# Takes marks of 5 subjects from users and find avg.

# math=int(input("enter marks of math"))
# physics=int(input("enter the marks of physics"))
# chemistry=int(input("enter the marks of chemistry"))
# biology=int(input("enter the marks of biology"))
# hindi=int(input("enter the marks of hindi"))
# avg=(math+physics+chemistry+biology+hindi)/5
# print(avg)


# Ques-17
# Take salary from user and find annual salary.

# Monthly_salary=int(input("enter salary"))
# annual_salary= Monthly_salary*12
# print(annual_salary)


# Ques-18
# Take 1st name and last name from the user and print full name.

# first_name=input("enter 1st name")
# last_name=input("enter last name")
# full_name=first_name +last_name
# print(full_name)

# Ques-19
# Take input as number from the user and print squre and cube.

# num=int(input("enter number"))
# square=num**2
# cube= num**3
# print(square)
# print(cube)


# Timing :- 10-12pm (Deep coding)

# Ques-1
# Take 4 input from user and print in good format.
 
# name=input("enter name :")
# age=int(input("enter age :"))
# college=input("enter college name :")
# branch= input("enter branch name :")
# print("\n===== STUDENT PROFILE =====\n")
# print("name: ",name)
# print("age:  ",age)
# print("college:  ",college)
# print("branch:",branch)


# Ques-2
# if any value is taking as input from the user then print its type.

# x=input("enter any value")
# print(type(x))

##---> NOTE -input() always give string type


# Ques-3
# Mini Bio Generator and take input as name, age city, favourite language.

# name=input("enter name")
# age=int(input("enter age"))
# city=input("enter city")
# favourite_lang= input("enter language")
# print("Hello, my name is",name)
# print(f"I am {age} years old")
# print("I live in",city)
# print("my favourite language is",favourite_lang)


# Ques-4
# Salary report




# Question of leetcode --> TWO SUM
# nums=[2,7,11,15] , Target=9 (meaning - adding any two number which gives 9).

# nums=[2,7,11,15]
# target=9

# for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#         if nums[i]+nums[j]==target:
#             print(i,j)


#  Ques-2 (LEETCODE)
# nums=[1,2,3,4,5]  , target=8

# nums=[1,2,3,4,5]
# target=8

# def twosum(nums,target):
#     for i in range(len(nums)):
#        for j in range(i+1,len(nums)):
#          if nums[i]+nums[j]==target:
#             return[i,j]
    
# print(twosum(nums,target))
