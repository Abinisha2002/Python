#if statement
name=input("enter your name:")
age=input("enter your age:")
city=input("enter your city:")
std=int(input("enter your std:"))
school=input("enter your school:")
tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
total=tamil+english+maths
average=total/3
print(total)
print(average)
if total>250:
    print("you got a bio")
else:
    print("you got a com")



num=int(input("enter tour number"))
if num>30:
    print("good")



num=int(input("Enter your number: "))
if num > 0:
   print("The number is positive")
else:
    print("The if statement is easy")



# if else
num=int(input("enter tour number"))
if num>0:
    print("good")
else:
    print("bad")




age=int(input("enter your age:"))
if age<18:
    print("your are eligible to vote")
else:
    print("your are not eligible to vote")

    


age=int(input("enter your age:"))
if age>25:
    print("your are eligible to election:")
else:
    print("your are  not eligible to election:")


#if  else workout
age=int(input("enter your age:"))
if(age<30):
    print("you are eligible")
else:
    print("you are not eligible")    

#elif
num=int(input("enter your number:"))
if num>30:
     print("good")
elif num==30:
    print("this is equal")
else:
    print("bad")



x=int(input("what is your exam score?"))
if x>=85:
    print("you got an A!congrats")
elif x>=75:
    print("you got a B! well done!")
elif x>50:
    print("you got a C! well done!")
elif x==5:
    print("you got a D! well done!")
else:
    print("you diid not pass the exam")    


#nestedif
num=int(input("enter your number:"))
if num>=0:
 if num==0:
        print("this is equal to 0")
 else:
    print("this is positive number")
else:
    print("this is negative number")


#nested
username=input("enter your username:")
password=input("enter your password:")
if username=="abinisha":
  if password=="livewire":
    print("login a successful!welcome admin")
  elif password=="12345":
    print("weak password.please reset your password")
  else:
    print("incorrect password.please try again")
else:
        if username=="dd":
           if password=="jan":
             print("login successful welcome dd")
           else:
             print("incorrect password please try again")
        else:
               print("unknown user.please try again")




if num>=0:
    if num==0:
        print("this is eqal to0")
    else:
        print("this is positive number")    
else:
        print("this is negative number")                   












#workout
student=int(input("enter your number:"))
name=str(input("enter your name:"))
std=int(input("enter your std:"))
age=int(input("enter your age:"))
place=str(input("enter your place:"))
tamil=int(input("enter your tamil marks:"))
english=int(input("enter your english marks:"))
maths=int(input("enter your maths marks:"))
science=int(input("enter your science marks:"))
social=int(input("enter your social marks:"))
total=tamil+english+maths+science+social
print(total)
if (total>400)and(age>=15):
    print("the student is bio")
    print("there is a markstatement")
else:
    print("the student is com")
    print("there is not markstatement")






















































































# '''#if statement
# num=int(input("Enter your number: "))
# if num > 0:
    
#     print("The number is positive")

# else:
#     print("negative number")
# '''



# '''age=int(input("enter your age:"))
# if age<18:
#     print("your are eligible to vote")

# else:
#     print("your are not eligible to vote")'''
    
# '''

# age=int(input("enter your age:"))
# if age>25:
#     print("your are eligible to election:")
# else:
#     print("your are  not eligible to election:")


# student=int(input("enter your number:"))
# name=str(input("enter your name:"))
# std=int(input("enter your std:"))
# age=int(input("enter your age:"))
# place=str(input("enter your place:"))
# tamil=int(input("enter your tamil marks:"))
# english=int(input("enter your english marks:"))
# maths=int(input("enter your maths marks:"))
# science=int(input("enter your science marks:"))
# social=int(input("enter your social marks:"))
# total=tamil+english+maths+science+social
# print(total)
# if (total>400)and(age>=15):
#     print("the student is bio")
#     print("there is a markstatement")
# else:
#     print("the student is com")
#     print("there is not markstatement")

    
# ["apple","mango"]
# b=["apple","mango"]
# print(a is  b)
# x=4
# y=7
# print((x>2)and(y>5))'''

# num=int(input("enter your number:"))
# if num>30:
#      print("good")
# elif num==30:
#     print("this is equal")
# else:
#     print("bad")

# num=int(input("enter your number:"))
# if num>=0:
#  if num==0:
#         print("this is equal to 0")
#  else:
#     print("this is positive number")
# else:
#     print("this is negative number")



# a=90
# b=89
# print(a>90)and(b<90)
# print(not(a>89 and b>78))
# age=int(input("enter your age:"))
# if(age<30):
#     print("you are eligible")
# else:
#     print("you are not eligible")




# # nested if statement
# username=input("enter your username:")
# password=input("enter your password:")
# if username=="bhavya":
#   if password=="livewire":
#     print("login a successful!welcome admin")
#   elif password=="12345":
#     print("weak password.please reset your password")
#   else:
#     print("incorrect password.please try again")
# else:
#         if username=="dd":
#            if password=="jan":
#              print("login successful welcome dd")
#            else:
#              print("incorrect password please try again")
#         else:
#                print("unknown user.please try again")



# def myfunction(*kids):
#   print(kids[0])
# myfunction("emil","hani","linus")
# def my_function(**kid):
#   print("his last name is"+kid["fname"]+kid["lname"])
# my_function(fname="nitharshan",lname="hani")
# def my_function(country="norway"):
#   print("I am from"+country)
# my_function("sweden")
# my_function()
# my_function("india")



# gift=lambda person:print("abinisha",person)
# gift("watch")
# x=lambda a,b:a*b
# print(x(4,7))
# def myfun(n):
#   return lambda a:a*n
# m=myfun(2)
# print(m(11))
# print(m(45))
# data=[1,2,3,4,5,6,7,8,9]
# result1=map(lambda x:x*2,data)
# print(list(result1))
# print(result1)
# result2=filter(lambda x:x%2==0,data)
# print(list(result2))
# print(result2)
 


# def employee(name,age):
#     print("my details" ,name,age)
   
# person1={
#     "name":"abi",
#     "age":22
# }


# def value(name):
#     print("hello",name)
# def sum(a,b):
#     print(a-b)