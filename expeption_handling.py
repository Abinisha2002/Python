#exception handling
try:
    file1=open("new.txt","r")
# Reading from file     
    print(file1.read())
    file1.close()
except FileNotFoundError:
    print("filenot found errorsuccessfully handled")
          
