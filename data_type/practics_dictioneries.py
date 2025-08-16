#dictonires is basically a set of  ordered collection of kay and values in {}
# we can convert an list into dict if we have 2 values in the list or tuple


# .key "we get output as dict_keys"
# .values " we get output as dict_values"
# .items "we get list of touples individual key and value in seperate ()"
# .get
# .update  if we want to add or update multiple key value pair in the dict.
# .pop to remove any key value pair from the dict. we need to paas key
# .popitem "to remove last item from the dict"
# .clear " to clear the dict"
'''lst1 = ['name', 'ankit']
lst2 = [('name', 'ankit'), ('from', 'SRE')] # in each list or tuple we need 2 values only like key and value pait
print(lst1)
print(lst2)'''

'''Ankit_profile = {
"name": "ankit",
"age": 34,
"avg": 54.5,
"skill": ["betting", "bowling"]
}
print(Ankit_profile)# we get output as key value pair
print(Ankit_profile.keys())# we gat output as dict_keys
print(Ankit_profile.values())# we gat output as dict_keys
print(list(Ankit_profile.keys()))# to print list of keys
print(list(Ankit_profile.values())) # pt print list of values
print(list(Ankit_profile.items())) # to get list of tuples, individual key and value in seperate ()
print(Ankit_profile["name"]) # to print the value of a perticuler key'''




Ankit_profile = {
"name": "ankit",
"age": 34,
"avg": 54.5,
"skill": ["betting", "bowling"]
}
#Ankit_profile["Nike_name"] = "akki" # to create a key value pair in the dict.
#Ankit_profile["name"] = "Rahul" # to update existing value for the key

#Ankit_profile.update({ # if we want to add or update multiple key value pair in the dict.
# "hight":5.9,
# "eye_colour":"broun"
# })
#Ankit_profile.pop("name") #to remove any key value pair from the dict. we need to paas key
Ankit_profile.popitem() #to remove last item from the dict
print(Ankit_profile)
