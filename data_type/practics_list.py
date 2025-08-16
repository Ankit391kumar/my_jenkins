#list => it is a collection of hetrogeneous datatype of elements.
# in order to store multiple value in one variable we have "lists, touples and dictionaries"

# methods to use list

'''data = ["MR"]
data1 = list("ANKIT", 34)
data2 = "KUMAR".split()
print(data,data1,data2)'''

#List is muitable we can be perform several operation with list
   # create
   # Update
   # read
   # delete
  #update => suppose we have to variable and we want to add secont variable value in first veriable so we can easily perform this with the help of

'''countries1 = ["IND", "SL", "PAK"] # list1
countries2 = ["ENG", "USA", "AUS"] #list2

countries1.extend(countries2) # we appended contryes1 list wit contries2 list

print(countries1)'''


#if we and to add one element at a time 
'''data = ["ankit", "shlok", "Rajat"] # data list
data.append("akansh") # an element
print(data)'''

'''data = ["abc", "def",]
print(data)
print(id(data))
data1 = data

data.append("ghi")
print(data1)
print(id(data1))'''

# add an element at perticuler position in the existing list.
'''data = ["abc", "ghi", "jkl"]
data.insert(1"def")
print(data)'''

# print selected element from the list

'''countries = ["IND", "SL", "PAK","ENG", "USA", "AUS","CHI" ]
counteies2 = countries[:2] + countries[-2:]
#countries[:2] forto select starting index from the list
#countries[-2:] to ending index from list 
# output should be "['IND', 'SL', 'AUS', 'CHI']"
print(counteies2)'''

# we have 3 list about ankit now we want to combine them and want to print on the console\
#1 . Bowling from the skil and
#2 letter L from the bowling
"""personal_info = ["ankit", "kumar", 34, 5.9]#0
skill = ["batting", "bowling","filding"]#1
stats = [10, 3, 10]#2
ankit_profile = [personal_info, skill, stats]
#print(ankit_profile)
print(ankit_profile[1][2])# to print specific element from the combined list
print(ankit_profile[1][1][3])# to print letter word from the bowling

# NOW we want to add "keeping" skill the the ankit_profile. 
ankit_profile[1].append("allrounder") # to add element in the specific list of ankit_profile
print(ankit_profile)"""

# Remove an element from list
'''countries = ["IND", "SL", "PAK","ENG", "USA", "AUS","CHI" ]
#countries.remove("AUS") # it is oldmethod used to remove any specific element from the lit.

countries.pop()# it is used to remove element from last
countries.pop()
countries.pop()# how many element we want to remove from list we need to repate this step in the script.
countries.pop(1)# if we want to remove the specific element from the list we need to pass the argument
print(countries)'''

# we have list of countried and we want to add them toughter
'''asian_countries = ["IND", "SL", "PAK"]
other_countries = ["ENG", "USA", "AUS"]

world = [asian_countries, other_countries]
# print(world)
# Now from the world i want to remove "asian_countries" and atter that i need to add "INDIA" in the asian_countries
asian_countries.clear() #to delete all the elements from the list
world[0].append("IND") # to add "IND" in the asian_countries list
print(world)'''

# if we want to maintain the order of list we can simpally use sort method
countries = ["IND", "SL", "PAK","ENG", "USA", "AUS","CHI" ]
#countries.sort(reverse=True)
countries.sort()
# we cann't use sort function with hetrogenuous datatype element
print(countries)