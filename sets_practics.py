set1 = {1, 2, 3}
set1.add(4)

print(set1)

set1.remove(1)
print(set1)

# union ====> it removes duplicate valuse from both the lists and print the unique value
set1 = {1, 2, 3}
set2 = {1, 2, 4, 5}
union_set = set1.union(set2)
print("unio_set is:", union_set)

# intersection==> it print only the common values from both the lists
set1 = {1, 2, 3}
set2 = {1, 2, 4, 5}
intersection_set = set1.intersection(set2)
print("intersection_set is:", intersection_set)

#diffrence==>
set1 = {1, 2, 3, 5, 6, 7}
set2 = {1, 2, 4}
diff_set = set1.difference(set2) # it print only the values which is diffrent from set2
print("diffrencr_set is:", diff_set)

#symmetric_diffrence====> it takes the unique value from both the list and print
set1 = {1, 2, 3, 5, 10, 12, 6, 7}
set2 = {1, 2, 4, 10, 11, 12}
symm_diff_set = set1.symmetric_difference(set2)
print("symmetric_diffrence:",   symm_diff_set)

# membership testing====> to check the given value is a part of the given set or not
set1 = {1, 2, 3, 5, 10, 12, 6, 7}
set2 = {1, 2, 4, 10, 11, 12}
print(2 in set1)
print(4 in set1)
print(23 in set2)
print(4 in set2)


#subset or superset testing
set1 = {1, 2, 3, 5,}
set2 = {1, 2, 4, 10}
print({1, 2}.issubset(set1))
print({4, 10}.issuperset(set2))


#copy
set1 = {1, 2, 3, 5,}
print(len(set1))
set2 = {1, 2, 4, 10}
copy_set = set1.copy()
print(copy_set)
set1.clear()
print(set1)



