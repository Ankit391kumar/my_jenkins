# set is a un-ordered collection of unique hetrogeneous datatype elements while
# list and tuples is ordered collection
# in set if we have puplicate it will automatically remove this
 
'''countries_set = set() # for any empty data we need to pass like this
print(type(countries_set))'''


'''countries_set = {"IND", "USA","BAN", "SL", "USA", "UAE", "USA"} # if we have date in set we alwasys need to pass in {}.
# we have duplicate data in this 
print(countries_set)# when we print this it will remove the duplicate.
# at every trigger order of the data will suffle
print(countries(set[0]))# we can to access the element based on index in set bcoz of it is unordered collection of data

'''

# we have a list and want to convert into set and add an element in the set
'''countries = ["IND", "USA","BAN", "SL"]
countries_set = set(countries) # to convert list into set
countries_set.add("BHU") # to add an element in the set
print(countries_set)'''


# union operation for set
c1 = {'a', 'b', 'c', 'd'}
c2 = {'d', 'e', 'f', 'f'}
#out = c1.union(c2)# it is updated and store in new variable
#out = c2.intersection(c1) # to find common element from two diffrent set and store in diffrent variable
#c2.intersection_update(c1) # in this it is update the value in same variable
out = c2-c1 # used to check the diffrence between two sets
print(out)
print(c2)