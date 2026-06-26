# Check number is even or odd.
# Ques-1
# num=int(input("enter number"))
# if num%2==0:
#     print("number is even")
# else:
#     print("odd")    

# Ques-2
# Check number is positive or negative.

# num=5
# if num>0:
#     print("number is positive")
# else:
#     print("negative")    


# Ques-3
# Largest of two number.

# a=int(input("enter 1st number"))
# b=int(input("enter 2nd number"))
# if a>b:
#     largest=a
# else:
#     largest=b
# print(f"the largest number is {largest}")    


# Ques-4
# Voting eligibility

# age=int(input("enter your age"))
# if age >= 18:
#     print("you are eligible to vote")
# else:
#     print("not eligible")    


# MEDIUM LEVEL:-

# Ques no-6
# Largest of three number.

# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# num3=int(input("enter 3rd number"))

# if (num1>num2) and (num1>num3):
#     largest=num1
# elif (num2>num3) and (num2>num1):
#     largest=num2
# else:
#     largest=num3
# print("largest number is :",largest)    
        
# 2nd method:-
# num1=int(input("enter 1st number"))
# num2=int(input("enter 2nd number"))
# num3=int(input("enter 3rd number"))

# # using built-in max() function
# largest=max(num1,num2,num3)
# print("largest number is :",largest)


# Ques-7
# Leap year check

# years=int(input("enter year"))
# if (years%4==0) or (years%400==0) or (years%100 !=0):
#     print(" leap years")
# else:
#     print("not leap year")   


# Ques-8
# Divisible by 5 or 11.

# nums=int(input("enter number"))
# if (nums%5==0) and (nums%11==0):
#     print("divisible by both")
# else:    
#     print("not divisible")


# Ques-9
# check pass or fail

# students_marks=75
# if students_marks >=85:
#     print("pass")
# else:
#     print("fail")    


# Ques-10
# Grade calculator

# marks=int(input("enter marks"))
# if marks >=90:
#     grade= "A"
# elif marks>= 80:
#     grade="B"
# elif marks>= 70:
#     grade="c"
# else:
#     grade="d"
# print("Grade is :",grade)               


# Deep coding session:--

# Ques-11
# find absolute value

# nums=int(input("enter number"))
# if nums<0:
#    num=-nums

# print("absolute value equal :",num) 


# ANOTHER METHOD:-
# X=-7
# print("absolute value:",abs(X))

 

# Ques-12
# Check profit and loss

# a_buy=12
# a_sell=15
# if a_buy<a_sell:
#     print("profit")
# else:
#     print("loss")   


# Ques-13
# Check character is vowel or constant

# char=input("enter character")
# if char in "aeiou":
#     print("vowel")
# else:
#     print('consonant')


# Ques-14 ( abhi problem h)
# Check alphabet or not

# char = input("enter a character")

# if char.isalpha():
#     print("alphabet")
# else:
#     print("not an alphabet")


# Ques-15
# Check number is multiple of 3

# nums=int(input("enter number"))
# if nums%3==0:
#     print("multiple of 3")
# else:
#     print("not multiple of 3")    


# Ques-1 LEETCODE ( Topic name-Palindrome number)
# check palindrome number

nums=int(input("enter number"))

original=nums
reverse=0

while nums>0:
    last_digit=nums%10
    reverse=reverse*10+last_digit
    nums=nums//10

if original==reverse:
    print("palindrome")
else:
    print("not palindrome")   



# Ques-2 (palindrome)
# nums=int(input("enter number"))

# if nums==nums[::-1]:
#     print("palindrome")
# else:
#     print("not palindrome")    