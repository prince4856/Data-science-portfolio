# ----------------FUNCTION------------------

#-> Ques-1
# Function to print your name

# def show_name():
#     print("prince kumar")

# show_name()    


#-> Ques-2
# Function to add two number.

# def add(a,b):
#     return a+b

# result=add(10,20)
# print(result)


#-> Ques-3
# Function to substract two number.

# def sub(a,b):
#     return a-b

# result=sub(50,10)
# print(result)


#-> Ques-4
# Function to multiply two number.

# def multiply(a,b):
#     return a*b

# result=multiply(10,50)
# print(result)


#-> Ques-5
# Function two divide two number.

# def divide(a,b):
#     return a/b

# result=divide(500,10)
# print(result)


#-> Ques no-6
# Function to find square of a number.

# def square(n):
#     return n**2

# result=square(9)
# print(result)


#-> Ques-7
# Function to find cube of a number.

# def cube(n):
#     return n**3

# result=cube(5)
# print(result)


#-> Ques-8
# Function to check even or odd.


# def check(num):  ------- #defining func, num is parameter
#     if num%2==0:
#         print("even number")
#     else:
#         print("odd number")  

# check(5)    ------------- #calling func,  5 is argument value      


#-> Ques no-9
# Function to find maximum of two number.

# def find_max(a,b):
#     if a>b:
#         return a
#     else:
#         return b   

# print(find_max(5,8))


#-> Ques-10
# Function to calculate area of rectangle.

# def area_of_rectangle(a,b):
#     return a*b

# print(area_of_rectangle(8,5))


#--------------- DEEP CODING SESSION-----------------

# Ques-11
# Factorial using function.

# def fact(n):
#     fact=1
    
#     for i in range(1,n+1):
#         fact=fact*i
#     return fact    

# print(fact(5))   


#-> Ques-12
# code for prime number using function.

# def prime_no(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count=count+1
        

#     if count==2:
#            return "prime no"
#     else:
#             return "non-prime"   

# print(prime_no(5))            


#-> Ques-13
# Fibonacci using function.
  
# def fibonacci_no(n):
#     a=0
#     b=1
#     i=1
#     while i<n:
#         print(a)
#         next_num=a+b
#         a=b
#         b=next_num

#         i=i+1

# fibonacci_no(10)      


#-> Ques-14
# Palindrome number checking using function

# def palindrome_no(n):
#     original=n
#     reverse=0

#     while n>0:
#        l_digit=n%10
#        reverse=reverse*10+l_digit
#        n=n//10

#     if original==reverse:
#         return "palindrome"
#     else:
#         return"not palindrome" 

# print(palindrome_no(121))    


#-> Ques-15
#-> Reverse a number using a function

# def reverse_no(n):
#     reverse=0

#     while n>0:
#         last_digit=n%10
#         reverse=reverse*10+last_digit
#         n=n//10
#     return reverse

# print(reverse_no(4321)) 


#-> Ques-16
# Sum of digits using function

# def total_sum(n):
#     total=0   ----box empty
#     i=1    ----- initial iteration
#     while i<=n:
#         total=total+i----   moving 1 by 1
#         i=i+1    ----update
#     return total 
   
# print(total_sum(10))  


#-> Ques-17
# Largest of three number using function

# def largest_no(a,b,c):
#     if a>b and a>c:
#         return a
#     elif b>c and b>a :
#         return b
#     else:
#         return c
    
# print(largest_no(12,13,14))    

        
    
# Ques-18
# Celsius to fahrenheit using function.

# def celsius_to_fahreinheit(celsius):

#     fahereinheit=(celsius*9/5)+32 ----- calculate
#     return fahereinheit  --------return
# print(celsius_to_fahreinheit(25))


# Ques-19
# Area of circle using function

# def area_of_circle(r):

#     area=3.14*r*r
#     return area

# print(area_of_circle(22))



# Ques->20
# Simple interest using function

# def simple_interest(p,r,t):

#     interest=p*r*t/100
#     return interest

# print(simple_interest(200,5,2))

       