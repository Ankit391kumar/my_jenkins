
# dif function() #it is a calling function
# dif ===> is key keyword
# conactenate ===> is a kind of function 
# () use to pass the argument



# def greeting(cls_name): # cls_name is a variable, we store variable here and pass dynamic value to the function insteed of hardcoaded.
#     #class_name = cls_name
    
#     print(f"it is a {cls_name} class")
    
#     print("\n\n")

# greeting("Docker") # we are passing value dynamically using this block

# greeting("K*S")
##################################

# def add2Numbers(num1, num2):
#     output = num1 + num2
    
#     return output

    
# sum_of_numbers = add2Numbers(10, 20)
# print(sum_of_numbers)
# print("\n\n")


# sum_of_numbers = add2Numbers(123, 321)
# print(sum_of_numbers)


#######################################
# def conactenate(str1, str2):
#     print(f"{str1} {str2}")
#     name = f'{str1} {str2}'
    
#     return name  # in real time we are performing sone operations

# first_name = "ankit"
# last_name = "kumar"
# out = conactenate(first_name, last_name)
# print(out) # in real time senerio we never use print statement
# # this print statement we are using only debuging purpose

################################
# move some file from one loction to another location


# import shutil
# def move_a_file(source, destination):
#     shutil.move(source, destination)
    
    
#     return "file movement is done"
    
    
# result =move_a_file('C:/Users/admin/Desktop/python_ankit/ankt.txt',  'C:/Users/admin/Desktop/anjul')
# print(result)


#####################
# def add2Numbers(num1, num2):
#     sum = num1 + num2
#     return sum

# # now i want to double of sum and tripple od sum
# doubled = add2Numbers(10, 20) * 2
# trippled = add2Numbers(10, 20) * 3

# sum_number = add2Numbers(10, 20)
# print(doubled)
# print(trippled)
# print(sum_number)


################################## 
# if we want to write multiple values we can use list or tuples
# we can use any list, tuples dict
# wap to perform multiple operation by using line
def maths(num1, num2): # we invoked this "maths" function in this code only one time as in line 87
    return (num1 + num2, num1 * num2, num1 - num2, num1 / num2,) # return multiples values

add, mul, sub, dvi = maths(200, 50) # use to unpaking or capture multiple values
print(add)
print(mul)
print(sub)
print(dvi)