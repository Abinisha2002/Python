'''DICTIONARY'''
##creating a dictionary
country_capitals={
    "united states":"washington",
    "italy":"rome",
    "england":"london"
    }
#printing the dictionary
print(len(country_capitals))


##python dictionary length
country_capitals={
    "united states":"washington",
    "italy":"rome",
    "england":"london"
    }
#get dictionary length
print(len(country_capitals))



##access dictionary items
country_capitals={
    "united states":"washington",
    "italy":"nepals",
    "england":"london"
    }
print(country_capitals["united states"])
print(country_capitals["england"])



#change the value of "Italy" key to "Rome"
country_capitals={
    "united states":"washington D.C.,"
    "italy":"naples,"
    "england":"london"
}
country_capitals["italy"]="rome"
print(country_capitals)



##add items to a dictionary
country_capitals={
    "united states":"washington",
    "italy":"nepals"
    }
country_capitals["germany"]="berlin"
print(country_capitals)



# Remove Dictionary items
country_capitals={
    "united states":"washington",
    "italy":"nepals"
    }
country_capitals["germany"]="berlin"
print(country_capitals)
person={"name":"phil","age":22,"salary":3500.0}
result=person.popitem()



#delete item having"united states" key
del country_capitals["united states"]
print(country_capitals)
person={"name":"phil","age":22,"salary":3500.0}
print("person=",person)
person["profession"]="plumber"
result=person.popitem()
print("return value=",result)
print("person=",person)
fruits_name={"apple","banana","cherry"}
fruits_name.popitem()
print("fruits=",fruits_name)