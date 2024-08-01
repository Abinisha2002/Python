'''FOR LOOP'''
a="Abinisha"
for i in a:
    print(i)


names=["k","h","f"]
for name in names:
   print(name)



'''Range in forloop'''    
for x in range(1,20,3):
    print(x)


for x in range(20):
   print(x)



'''List in forloop'''    
a=["happy",2,6]
for i in a:
    print(i)

    
list1=[1,2,3,4]
sum=0
for i in list1:
    sum=sum+i
    print("the total value is:",sum)
    print("Program terminated")


lists=[[1,2,3],[4,5,6],[7,8,9]]
for l in lists:
   for x in l:
      print(x)

   
'''Break'''
for x in range(9):
   if (x==20):
      break
   print(x)


'''Continue'''
for x in range(15):
   if(x==11):
      continue
   print(x)


'''Nested forloop'''
for x in range(5):
   for y in range(3):
      print(f"({x},{y})")


x=[1,2]
y=[4,5]
for i in x:
   for j in y:
      print(i,j)


adj=["red","big","tasty"]
fruits=["apple","banana","orange"]
for x in adj:
   for y in fruits:
      print(x,y)



'''Increase value in forloop'''
for x in range(2,30,5):
   print(x)


'''pass statement'''
for x in range(7):
   pass



'''for else'''
for x in range(3):
   print(x)
else:
   print("loop ended")


'''for using string'''
string="hanithra"
for x in string:
   print(x)

'''collections in forloop'''
collection=["hey",5,"d"]
for x in collection:
   print(x)

















