'''error handling'''
#logical errors
divide_numbers=7/0
print(divide_numbers)

#built-in exceptions
print(dir(locals()["_builtins"]))

#catching specific exceptions in python
try:
    even_numbers=[2,4,6,8]
    print(even_numbers[8])
except ZeroDivisionError:
    print("Denominator cannot be 0")
except IndexError:
    print("Index out of Bound")

#python try with else clause
#program to print the reciprocal of even numbers
try:
    num=int(input("Enter a number:"))
    assert num%2==0
except:
    print("Not an even number:")
else:
    reciprocal=1/num
    print(reciprocal)

#syntax errors
#initialize the amount variable
amount=10000
#check that you are eligible to
#purchase DSA self pacedor not
if (amount>2999):
    print("you are eligible to purchase dsa set paced")

#try for unsafe code
try:
    amount=1999
    if amount<2999:
        #raise valueError
        raise ValueError("please add money in your access")
    else:
        print("you are eligible to purchase DSA self paced course")
 #if false the raise the value error
except ValueError as e:
    print(e)  

#try....finally
try:
    numerator=10
    denominator=0
    result=numerator/denominator
    print(result)
except:
    print("Error:Denominator cannot be 0")
finally:
    print("This is finally block") 

#Divisible by 0
try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("result:",a/b)
except:
    print("error occurred")    

try:
    a=int(input("Enter first number:"))
    b=int(input("Enter second number:"))
    print("result:",a/b)
except ZeroDivisionError:
    print("cannot be divided by zero")
except ValueError:
    print("alphabet cannot be entered")

# assertion(or)assert
#syntax error
a=10
if a==10:
    print(a)

#Runtime error
#Name error
print(a)

#Type error
x="100"
y=5
z=x+y

#index error
x=["sabeena","santhiya","suba"]
print(x[3])

#Attribute error
x="kayalvizhi"
x.reverse()

#Logical error
def fact(n):
    r=1
    for i in range(1,n+1):
        r=r*i
        return r
    print(fact(5))

#example
try:
    x=int(input("Enter a number:"))
    y=10/x
    print("The result is :",y)
except ValueError:
    print("you must enter fa valid integer")
except ZeroDivisionError:
    print("You cannot divide by zero")

#Assertion,attribute,floating point,import,index,
# memory,name,overflow,typeerror




































































































# #error handling
# divide_numbers=7/0
# print(divide_numbers)
# print(dir(locals()["_builtins"]))
# file=open("new.txt","a")
# file.write("\nemp name\tage\tsalary\tqualifi")
# file.write("\nanbu\t23\t2000\tdme")
# file.write("\nakash\t21\t3000\tb.sc")
# file.write("\nbijorn\t24\t4000\tdme")
# file.write("\nvishwa\t20\t1000\tdme")
# file.write("\najay\t21\t1200\tb.com")
# file.close()
# with open("new.txt","r") as file:
#     data=(file.read())
# print(data)
# class myclass():
#     x=5
# print(myclass)
# class name():
#     x=4
# ob=name()
# print(ob.x)
# class add():
#     a=5
#     b=4
#     c=a+b
# ob=add()
# print(ob.c)
# class sub():
#     x=int(input("enter a num:"))
#     y=int(input("enter b num:"))
#     z=x+y
# ob=sub()
# print(ob.z)
# class addition:
#     first=0
#     second=0
#     answer=0
#     def __init__(self,f,s):
#         self.first=f
#         self.second=s
#     def display(self):
#         print("first number="+str(self.first))
#         print("second number="+str(self.second))
#         print("addition of two numbers="+str(self.answer))
#     def calculate(self):
#         self.answer=self.first+self.second
# obj1=addition(100,200)
# obj2=addition(20,20)
# obj1.calculate()
# obj2.calculate()
# obj1.display()
# obj2.display()
# class mult():
#     x=10
#     y=2
#     z=x*y
# print(mult.z)
# class function():
#     x=int(input("enter a number:"))
#     y=int(input("enter b number:"))
#     z=x//y
# ob=function()
# print(ob.z)



# #exception handling
# try:
#     file1=open("newi.txt","r")
#     print(file1.read())
#     file1.close()
# except FileNotFoundError:
#     print("filenot found errorsuccessfully handled")
          
