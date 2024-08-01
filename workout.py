#fibonacci series
num=int(input("enter the value:"))
a=0
b=1
for i in range(num):
    a=(a)
    c=(a)
    a=b
    b=c+b
print(b)
a=int(input("enter the value:"))
f1,f2=0,1 
f3=f1+f2
print("fibonacci no",a)
print(f1)
print(f2)
for i in range(5):
    print(f3)
    f1=f2
    f2=f3
    f3=f1+f2
#factorial
# sum=int(input("enter the number"))
def fact(sum):
    fact=1
    sum=int(input("enter the number"))
    for i in range(1,sum+1):
      fact=fact*i
    return fact
print("factorial value",fact(sum))
# num=int(input("enter a number:"))
fact=1
if num<0:
    print("factorial does not exist for negative")
elif num==0:
    print("the factorial of o is 1")
else:
    for i in range(1,num+1):
        fact=fact*i
        print("the facorial of",num,fact)
def pali(c):
    a=int(input("enter the value:"))
    b=a*a
    while(b>0):
        r=b%10
        c=(c*10)+r
        b=b//1
        print(c)
        print(b)
    if c==b:
        print("it is adam number")
    else:
        print("it is not adam number")
def amstrong(b):
    num=a
    b=num*num*num
    print(b)
    num=c
    d=0
    while(num>0):
        r=num%10
        d=d+(r**3)
        num=num//10
        print(d)
    if d==c:
        print("amstrong number")
    else:
        print("not aamstrong number")
def palindrome(c):
    b=a
    c=0
    while (b>0):
        r=b%10
        c=(c*10)+r
        b=b//10
        print(c)
    if a==c:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
def fibonacci(c):
    f1,f2=0,1 
    f3=f1+f2
    print("fibonacci no",a)
    print(f1)
    print(f2)
    for i in range(5):
        print(f3)
        f1=f2
        f2=f3
        f3=f1+f2
def fact(c):
    for i in range(1):
      fact=fact*i
    return fact
print("factorial value",fact(c))
def palin(c):
    b=a[::-1]
    if a==b:
        print("it is a palindrome")
    else:
        print("it is not a palindrome")
n=int(input("enter your choice1.adam\n2.amstrong\n,3.palindrome\n4.fibonacci\n5.factorial\n6.palin"))
c=int(input("enter your number"))
if n==1:
    adam(c)
elif n==2:
    amstrong(c)
elif n==3:
    palindrome(c)
elif n==4:
    fibonacci(c)
elif n==5:
    fact(c)
elif n==6:
    palin(c)
else:
    print("please enter the correct input")

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a/b)
def mod(a,b):
    print(a%b)
c=1
while(c==1):
    n=int(input("enter your choice1.add\n2.sub\n3.mul\n4.div\n5.mod"))
    a=int(input("enter the first value:"))
    b=int(input("enter the second value:"))
    if (n==1):
        add(a,b)
    elif (n==2):
        sub(a,b)
    elif (n==3):
        mul(a,b)
    elif (n==4):
        div(a,b)
    elif (n==5):
        mod(a,b)
    else:
        print("enter correct value")
    c=int(input("if you want continue,please enter 1?"))
def adam(a):
    dup=a 
    squ1=dup*dup
    firstvalue=0
    while(squ1>0):
       r=squ1%10
       firstvalue=(firstvalue*10)+r
       squ1=squ1//10
    temp=0
    while(dup>0):
       r=dup%10
       temp=(temp*10)+r
       dup=dup//10
       secondvalue=temp*temp
       print(temp)
def amstrong(a):
    num=a
    d=0 
    while(num>0):
       r=num%10
       d=d+(r**3)
       num=num//10
       print(d)
def fact(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    return fact
c=1
while(c==1):
    n=int(input("enter the choice\n1.adam\n2.amstrong\n3.fact"))
    a=int(input("enter the value"))
    if (n==1):
        adam(a)
        print("it is adam number")
    elif (n==2):
        amstrong(a)
        print("it is amstrong number")
    elif (n==3):
        fact(a)
        print("it is factorial",fact(a))
    else:
# #         print("please enter correct value")
     string=input("enter the string")
number=string[2]
if (number=="a"):
    a=int(input("enter the value"))
    if a%2==0:
        print("even number")
    else:
        print("odd number")
elif (string[0]=="b"):
    from  kk import*
    if adam(val(a)==val(adam(a))):
        print("it is adam number")
    else:
        print("it is not adam number")
else:
    print("it is not a")
string=input("enter the string:")
if (string=="bhavyadharshini"):
    b=string[3:9].upper()

    print(b[0:2],b[2:4],b[4:7],sep='***')
else:
#     print("does not correct value")
   string="pythonprogramming"
freq={}
for char in string:
    if char in freq:
        freq[char]+=1
    else:
        freq[char]=1
print(freq)
least_freq=[]
for i in freq:
    if freq[i]==1:
        least_freq.append(i)
print(least_freq)
n=int(input("enter your value:"))
count=0
for i in range(1,n):
    if n%i==0:
        count=count+1
if count==1:
    print("prime")
else:
    print("not")
# ascending order
list=[2,6,5,9,4,1,6,0]
list.sort()
print(list)
list.sort(reverse=True)
print(list)
value=int(input("enter your value:"))
while value<5:
    value=value+1
    val=(value**3)-1
    print(val)
list1=[0,1,2,3,4,5]
b=list1.copy()
b.sort()
if list1==b:
    x=map(lambda a:a*2,list1)
    print(list(x))
else:
#     print("does not ascending")
      rows=int(input("enter the value"))
for i in range(1,rows+1):
    for j in range(i,i+1):
        print("*"*i)
x=1
for i in range(9):
    if i<4:
        print("*"*x)
        x+=1
    elif i>3:
        print("*"*x)
        x=x-1
value="bhavya"
for i in range(6):
    if i<5:
        print(value)
        value+=value
n=int(input("enter no:"))
for i in range(n,0-1):
    for j in range(i):
        print("*",end="")
    print()
