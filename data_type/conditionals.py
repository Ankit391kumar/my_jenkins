# # weather = "raining"
# if weather == "raining":
#     print("go by car")
# elif weather == "hot":
#     print("go by bike")
# else:
#     print("go by walk")

marks = "asdasdsd"

if isinstance(marks, int): # is used to check the valid datatype is passed or not for a given senerio
    if marks > 80:
        print("section A")
        if marks < 90:
            print("sub_section a2")
        else:
            print("sub_section a1")
    elif marks > 60:
        print("section B")
        if marks < 50:
            print("sub_section B2")
        else:
            print("sub_section B1")
    elif marks < 40:
        print("section c")
        if marks < 30:
            print("sub_section c2")
        else:
            print("sub_section c1")
else:
    print("pass a vaslid value")


