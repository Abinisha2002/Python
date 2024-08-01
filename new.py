a=8
print(a)
print(type(a))


y="abi"
print(y)


a=5
b=5
print(a+b)




a="it-is-an-apple"
b=a.replace("-"," ")
print(b)
a="i@have@an@doubt"
print(a.split("@"))
a="i want apple and the apple is sweet"
b=a.count("apple","mango")
print(b)
x="ilikeapple"
print(x[::-1])
myvalues="what","is","your","name"
x="and".join(myvalues)
print(x)
a="abinisha"
print(a[::-1].upper())
a="abinisha"
b="ahsiniba"
name="this is {}, my name {}"
print(name.format(a,b))

ages=[13,23,34]
print(ages)
#store duplicate elements
list1=[1,"hello",3]
list1=[1,"hello",3,"hello",1]
list3=[list1]
print(list3)
#access list elements
languages=["python","swift","java"]
print(languages[0])
#negative indexing in python
languages=["python","swift","c++"]
print(languages[-2])
#insert
fruits=["apple","banana","cherry"]
fruits.insert(2,"orange")
print(fruits)
#index
num=[4,55,66,77,67]
x=num.index(66)
print(x)
#reverse
animals=["cat","dog","elephant","thangam"]
animals.reverse()
print(animals)
#list slicing in python
name=["p","y","t","h","o","n","b","n"]
print(name[2:5])
print(name[5:])
print(name[:])
#add elements
numbers=[12,34,56,78,89]
numbers.append(90)
print(numbers)
#extend add
numbers=[12,34,56]
even_numbers=[2,4,6]
numbers.extend(even_numbers)
print(numbers)
#join lists
list1=["apple","mango","cherry"]
list2=["banana","grapes"]
for x in list2:
    list1.append(x)
print(list1)
#using insert
foods=["pizza","burger","sweets"]
foods.insert(0,20)
print(foods)
#change list items
languages=["python","java","jscript"]
languages[2]="c"
del languages[1]
del languages[-1]
print(languages)
#remove
animals=["cat","dog","elephant"]
animals.remove("cat")
print(animals)
#list pop
prime_numbers=[2,3,4,5]
removed_elements=prime_numbers.pop(2)
print(removed_elements)

#employee list
employee=["shiva","anbu","sai","vishwa"]
employee.insert(1,"mathan")
print(employee)





number=0
x=1
num=number+x

number=x
x=num
num+=1
print(x)

















