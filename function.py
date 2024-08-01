'''FUNCTION'''
#basic
def myfunction():
   print("hello world")
myfunction()

#arguments
def addnum(num1,num2):
   print(num1+num2)
addnum(2,3)



def myfunction(value,price):
  print(value,price)
myfunction(25,150)


#return keyword
def function(name,age):
   print(name,age)
function("livewire",23)


def multiplynum(num1):
 return num1*7
result=multiplynum(8)
print(result)

#recursion
def factorial(x): 
   if x==1:
     return 1
   else:
     return (x*factorial(x-1))
num=5
print("the factorial of",num,"is",factorial(num))





'''LAMBDA'''
'''(syntax)
functionname=lambda arg:exp
functionname()'''


gift=lambda person:print("abi","person") 
gift("watch")


x=lambda a:a+10
print(x(5))


x=lambda a,b:a*b
print(x(5,6))


x=lambda a,b,c:a+b+c
print(x(5,3,4))


def function(n):
  return lambda a:a*n
m=function(2)
print(m(11))
print(m(45))   



'''using string'''
string1="learning python"
upper=lambda string:string.upper()
print(upper(string1))


x="hello world"
name=lambda x:name()
print(name(x))


def cube(y):
  return y*y*y
print("normal function,cube:",cube(5))
lambda cube=lambda y:y*y*y
print("using lambda function,cube:",lambda cube(5))



#arbitrary(*,**)
def myfunction(*kids):
  print(kids[0])
myfunction("email","abis","linux")
def my_function(**kid):
  print("his last name is"+kid["fname"]+kid["lname"])
my_function(fname="devi",lname="abis")




#mapping
data=[1,2,3,4,5,6,7,8,9]
result1=map(lambda x:x*2,data)
print(list(result1))
print(result1)

#filtering
data=[1,2,3,4,5,6,7,8,9]
result2=filter(lambda x:x%2==0,data)
print(list(result2))



#task
def my_function(country="norway"):
  print("I am from"+country)
my_function("sweden")
my_function()
my_function("india")


#task
x=lambda a,b:a*b
print(x(4,7))
def myfun(n):
  return lambda a:a*n
m=myfun(2)
print(m(11))
print(m(45))





































































































# def myfunction():
#    print("hello world")
# myfunction()
# def addnum(num1,num2):
#    print(num1+num2)
# addnum(2,3)
# def function(name,age):
#    print(name,age)
# function("livewire",23)
# def multiplynum(num1):
#  return num1*7
# result=multiplynum(8)
# print(result)
# #recursion

# def factorial(x): 
#    if x==1:
#     return 1
#    else:
#     return (x*factorial(x-1))
# num=5
# print("the factorial of",num,"is",factorial(num))
# i=1
# while i<=10:
#   j=2
  while j<=2:
     print(i,"*",j,"=",i*j)
     i+=1
     j+=1
     print("\n")
