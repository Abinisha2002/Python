'''string operator'''

x="abi"
print(x)


'''place'''
a="hello,world"
b="abi"
print(b[2])

'''looping string'''
a=("apple","mango")
for a in "mango":
    print(a)



'''length'''
p="abinisha" 
print(len(p))   


'''check'''
print("abi in p")
'''(or)'''
a="abinisha"
print("nisha" in a)
print("h" in a)



'''replace'''
a="abinisha"
b=a.replace("i","e")
print(b)



'''upper'''
a="abinisha"
b=a.isupper()
print(b)

'''lower'''
a="Abinisha"
b=a.islower()
print(b)

'''modify string'''
a="worldcup"
print(a.upper())
print(a.swapcase())
print(a.capitalize())
print(a.replace("d","h"))
print(a.split("o","u"))


'''concatenate'''
a="bye"
v="hiii"
c=a+v
print(c)



'''format string''' 
a="the value is upper"
b="the value is lower between{}"
print(b.format(a))

quantity=3
price=4
itemno=8
myorder="i want {} price and {} pieces,{} itemno"
print(myorder.format(price,itemno,quantity))

#modify string
text="HELLO PHYTHON"
print(text)

#upper()
print("\n the text is:")
print(text.upper())

#lower()
print("\n the text is:")
print(text.lower())

#title()#..OPPOSITE WORD
print("\n the name is:")
print(name.swapcase())

# capitalize
print("\n the text is: ")
print("capitalize")

a="myvalue"
name="abinisha"
course="python"
hrs="sixty"
details=(
    f"{a},"
    f"{name},"
    f"{course},"
    f"{hrs},"
    )
print(details)

#slice
string="helloworld"
a=slice(3)
b=slice(1,5,6)
c=slice(-1,-3,-5)
print(string[a])
print(string[b])
print(string[c])


b="helloo python"
print(b[3:8])


b="helloo python"
print(b[-4:-1])


string="livewire"
print(string[:6])


string="livewire"
print(string[3:])

'''Negative index'''
string="livewire"
print(string[-5:-2])

'''Reverse'''
name="abinisha"
value="livewire"
print(name[::-1])
print(value[::-1])  


name="abinisha"
print(name[::-1])

'''split'''
name="r-o-s-e-b-e-s-t"
print(name.split('*'))


'''replace (or) remove word'''
a="is-a-word-to-string"
b=a.replace("_"," ")
print(b)


'''replace with count'''
txt="one one was a race horse,two two was on too"
x=txt.replace("one","three")
print(x)

'''Join'''
myvalues=("john","peter","vicky")
x="@".join(myvalues)
print(x)

a="the paragraph is a paragraph"
b=a.count("paragraph")
print(b)



'''Count'''
a="I Love apple,apple are my favourite fruit"
b=a.count("love")
print(b)
a="the paragraph is a paragraph"
b=a.count("paragraph")
print(b)


'''Strip'''
text1="   my name is python"
text2="*** my name is python***"
text3=",, my name is python"
text1=text1.strip()
text2=text2.strip("*")
text3=text3.strip(",")
print(text1)
print(text2)
print(text3)


a="**my name is python**"
a=a.strip("*")
print(a)
b="  it is an apple  "
b=b.strip()
print(b)

'''
if x>=90:
    print("you got an A!congrats!")
elif x>=50:
    print("you got an B!well done!")
elif x>50:
    print("you got an c!poor!")
elif x==50:
    print("you got a D!. but you can do!")
else:
    print("you did not pass")

'''
'''
#list items
thislist=["apple","banana","cherry"]
print(thislist)
'''
'''
#listlength
a=["list","banana","cherry"]
print(len(a))
'''
'''
#list items
list1=["apple","banana","cherry"]
list2=[1,2,3,4]
list3=["true","false","false"]
print(list1)
print(list2)
print(list3)
'''
'''
a=["std",234,"true",40,"made"]
print(a)
'''
'''
#access list items
a=["tamil","english","maths"]
print(a)


#negative indexing
y=["app","donut","straw"]
print(y[-1])
'''

#ranges of indexes:
x=["apple","banana"]





