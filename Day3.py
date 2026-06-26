#         Topic--> Loop and  pattern

# Ques-1
#- print 1 to 10

# for i in range(1,11):
#     print(i)


# Ques-2
# print 10 to 1

# for i in range(10,0,-1):
#     print(i)


# Ques-3
#- print Even number

# for i in range(0,10):
#     if i%2==0:

#          2nd method:-
# for i in range(0,10,2):     start:stop:step
#     print(i)


# Ques-4
#- print odd number

# for i in range(0,10):
#     if i%2 !=0:
#         print(i)


# Ques-5
# Sum of 1st N Numbers

# sum=0
# for i in range(1,11):
#     sum+=i
# print(sum)    


# Ques-6
# print 1 To N.

# i=0
# n=5
# while i<=n:
#    print(i) 
#    i=i+1      


# Ques-7
# Print 5 to 1 using while loop

# i=5
# n=1
# while i>=n:
#     print(i)
#     i=i-1


# Ques-8
# print multiplication table of 5

# i=1
# n=10
# while i<=10:
#     print("5*",i,"=",i*5)
#     i=i+1


# Ques-9
# Sum of digits

# i=1
# total=0
# while(i<=10):
#     total=total+i
#     i=i+1
# print(total)    


# Ques-10
# Reverse a number (palindrome no)

# nums=int(input("enter number"))

# reverse=0
# original=nums

# while nums >0:
#     digit=nums%10
#     reverse=reverse*10+digit
#     nums=nums//10
# if original==reverse:
#      print("palindrome")
# else:
#     print("not palindrome")


# Ques-11
# count Digits

# num=int(input("enter number"))

# count=0
# while num>0:
#     num=num//10
#     count=count+1

# print("total digit",count)  


# Ques-12
# write factorial value of 5.

# num=int(input("enter number"))
# fact=1
# while num>0:
#     fact=fact*num
#     num=num-1
# print("factorial value",fact)  


#  Ques -13
# Checking prime no.

# num=int(input("enter number"))

# count=0
# for i in range(1,num+1):
#     if num%i==0:
#         count=count+1

# if count==2:
#     print("prime number")
# else:
#     print("not prime")    

#    using while loop
# num=int(input("enter number"))
# count=0
# i=1
# while i<=num:
#     if num%i==0:
#         count=count+1
#     i=i+1

# if count==2:
#     print("prime")
# else:
#     print("not prime")   


# Ques-14
# Fibbonachi series 

# num=int(input("enter number"))

# a=0
# b=1
# i=1
# while i<=num:
#     print(a)
#     next_num=a+b
#     a=b
#     b=next_num

#     i=i+1

# Ques-15
#-Armstrong number

# num=int(input("enter number"))

# original=num
# total=0
# digit=len(str(num))

# while num>0:
#     last_digit=num%10
#     total=total+last_digit**digit
#     num=num//10

# if original==total:
#     print("armstrong") 
# else:
#     print("not armstrong") 


# Ques-16
# palindrome number

# num=int(input("enter number"))
# original=num
# reverse=0

# while num>0:
#     digit=num%10
#     reverse=reverse*10+digit
#     num=num//10

# if original==reverse:
#     print("palindrome")
# else:
#     print("not palindrome")    


# Ques no-17
# Greatest common divisor/ HCF(highest common factor)

# a=int(input("enter number"))
# b=int(input("enter number"))

# hcf=1

# for i in range(1,min(a,b)+1):
#     if a%i==0 and b%i==0:
#       hcf=i

# print("hcf=",hcf)    


# Ques-18
# LCM(LOWEST COMMON MULTIPLE)

# a=int(input("enter number"))
# b=int(input("enter number"))

# lcm=max(a,b)

# while lcm%a==0 and lcm%a==0:
#     print("LCM is",lcm)
#     break

# lcm=lcm+1



# Ques-19
# power of a number

# num=2
# power=3
# result=num**power

# print("result is",result)


# Ques no-20
# sum of even number

# total=0
# for i in range(1,10):
#     if i%2==0:
#         total=total+i

# print("Total is",total)        


# Ques no -21
# Sum of odd number

# total=0
# for i in range(1,10):
#     if i%2!=0:
#         total=total+i

# print("sum of odd no is ",total)        



        

