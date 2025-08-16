#intiger datatype
'''number = 9
print(type(number))'''

#flots datatype
'''x = 13.4 
y = 12.3
z = (x + y)

print(z)
print(type(z))'''
#comples number

'''NUM = 20 + 12.5 + 2j
print(type(NUM))'''

#string datatype
'''str1 = ''
str2 = ""
str3 = ''''''
str4 = 123 # it is an intiger but we can convert this into str by using next step
str5 = str(123) # in the left side str is a function which convert number into string
print("The datatype of str1 is",type(str1))
print("The datatype of str2 is",type(str2))
print("The datatype of str3 is",type(str3))
print("The datatype of str4 is",type(str4))
print("The datatype of str5 is",type(str5))'''


# charactor lenth in the string

'''Name = "ankit" 
print(type(Name)) # to check type of string
print(len(Name)) # to count length of the string
print("the valye at 0 position is", Name[0])
print("the valye at 4 position is", Name[4])'''

# escape character
# in this \ is a escape char , this \ is used to escapint the ".
'''information = "We are using \"Terragrunt\" to manage reusable Terraform modules more efficiently."
print(information)'''

#single quote
'''information1 = "We are using 'Terragrunt' to manage reusable Terraform modules more efficiently."
print(information1)'''

#triple quote
'''information2 = 'We are using ''Terragrunt'' to manage reusable Terraform modules more efficiently.'
print(information2)'''

# multiple line string 
  # By using escape char at the end of each line
'''news = "From bureaucrats to businesses, there’s a broad consensus \
in India that the latest escalation from the U.S. is only a pressure tactic \
to fast-track trade talks. However, Indian Prime Minister \'Narendra Modi\' \
now has something he didn’t have, even a day earlier \
the support of the Indian opposition to push back. "
print(news)'''

   # By using single and double triple quote in the starting and at the end of line
# news1 = '''From bureaucrats to businesses, there’s a broad consensus \
# in India that the latest escalation from the U.S. is only a pressure tactic \
# to fast-track trade talks. However, Indian Prime Minister \'Narendra Modi\' \
# now has something he didn’t have, even a day earlier \
# the support of the Indian opposition to push back.'''
# print(news1)


### method to convert the file in upper and lower case
#below are buildin function by python for string
  #upper()
  #lower()
  #isupper() <to check all the case is upper or not>
  #islower() <to check all the case is lower or not>
'''file1 = 'Abc.exc'
file2 = 'abc.exc'
print(file1.upper() == file2.upper())
print(file1.lower() == file2.lower())
print(file1.isupper())
print(file1.islower()'''


### count no of space in a string or repeted words.
# news = '''there’s a broad consensus in India in in that the latest escalation from the U.S. is only a pressure tactic to fast-track trade talks'''
# print(news.count(''))
# print(news.count('in'))
# print(news.count('a'))


### string start or end with perticular words or not.
# news = '''there’s a broad consensus in India in in that the latest escalation from the U.S. is only a pressure tactic to fast-track trade talks'''
# print(news.endswith('talks'))
# print(type(news))

### dynamic content pass to the string
'''first_name = "Abhi" 
last_name = "jeet"

full_name = first_name + " " + last_name
full_name2 = "{0} {1}".format(first_name , last_name) # we are using format string function to add dynamic content


full_name3 = f"{first_name} {last_name}" # lates method to add dynamic content
           # f stands for formating
print(full_name)
print(full_name2)
print(full_name3)'''


# convert data into array
# split

# join string
'''data = {"india" "usa" "uk" "aus"}
out = ''.join(data)

print(out)'''

#strip string
'''data = "  ankit.exc"
print(data.strip() == "ankit.exc")''' # it is used to remove the unwanted space befor and after the string

### padding 
###to avoid the character conversion we are adding 0 in the given value to make similer count.
### suppose we have student1 2 3 rank is 1 13 23 so we need to add 0 to make the shar count same for all the strings.

'''student1 = "001"
student2 = "013"
student3 = "023"
print(student1 < student2)
print(student2 < student3)'''

###to make the equal no of element we are using 0fill method
'''data1 = "12"
date2 = "122"
data3 = "1"
print(data1.zfill(5)) # zfill(5) intention is make the length of the equal thenth of the strings.
print(data2.zfill(5))
print(data3.zfill(5))'''


# slicing=> in Python allows you to extract a portion (substring) of a string.
'''data = "ABCDEFGHIJ"
  # data[starting_index:ending_index:step]
  #     [0         :length of string:1] these are the default value of string
print(data[:]) # print complete string
print(data[0:3]) # print 0 to 2 not included 3
print(data[2:5]) # print fron 2nd index to 4 index 5 is excluded.
print(data[2:]) #from 2 to last of the string
print(data[2:-1])  #print fron 2nd index to length-1 .
print(data[::])
print(data[::2]) # step is basically used for escaping the letter.
     # "A B C D E F G H I J"
     # 1=> B
     # 2=> c
     # 3=> D'''
     
     
     
# reverse a string
'''data = "ABCDEFGH"
data1 = "NITIN"
print(data[::-1])''' # we can reverse the string through this
# write a program the given string is palindrom or not?
'''data1 = "NITIN" # palindron means same from both side
palindron = data1 == data1[::-1]

print(data1[::-1])
print(palindron)'''
