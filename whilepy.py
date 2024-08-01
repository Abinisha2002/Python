'''while loop'''
i=3
n=5
while i<n:
   print(i)
   i=i+1


'''Infinite loop'''
age=45
while age>18:
   print(age)

   
counter=int(input("enter your number:"))
while counter<3:
   print("inside loop")
   counter=counter+1
   print("counter")
else:
 print("inside statement")

 

 x=10
 while(x>=10) and (x<=20):
    print(x)
    x+=2
    print("end")



'''Nested while''' 
i=2
j=5
while i<=4:
    while j<8:
        print(i,",",j)
        j=j+1
        i=i+1

'''Multiplication'''
i=1
while i<=5:
    j=2
    while j<=5:
        print(i,"*",j,"=",i*j)
        i=i+1
        print("\n") 



total=3        
number=int(input("Enter the number:"))
while number!=0:
   total+=number
   number=int(input("Enter the number:"))
print("total=",total)



a="bhavya"
for i in a:
    print(i)
for x in range(1,20,3):
    print(x)
a=["happy",2,6]
for i in a:
    print(i)
list1=[1,2,3,4]
sum=0
for i in list1:
    sum=sum+i
    print("the total value is:",sum)
   
i=3
n=5
while i<n:
   print(i)
   i=i+1
counter=int(input("enter your number:"))
while counter<3:
   print("inside loop")
   counter=counter+1
   print("counter")
else:
   print("inside statement")

def myfunction():
   print("hello world")
myfunction()
def addnum(num1,num2):
   print(num1+num2)
addnum(2,3)
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
i=1
while i<=10:
  j=2
  while j<=2:
     print(i,"*",j,"=",i*j)
     i+=1
     j+=1
     print("\n")
