# Decorator is a fucnction that accept another function as an argument.
# So we can perform any action before and after iour function 

import time



def time_deco(fun):
    def wrapper(*arg):
        start_time = time.time()
        fun(*arg)
        end_time = time.time()
        
        print(f"time taken for execution is {end_time - start_time} seconds")
    return wrapper 

@time_deco
def fact (num):
    fact = 1
    while num:
        fact *= num
        num -= 1
    print(fact)
    
fact(2)
    



# def isLoogedin(func):
#     def wrapper():
#         print("checking authintacation")
#         func()
#         print("Execution completed")
#     return wrapper

#@isLoogedin
# def checkWishlist():
#     print("This is my check list")
    
#@isLoogedin
# def checkOrders():
#     print("This is my order list")
    
# checkWishlist()
# checkOrders()

    