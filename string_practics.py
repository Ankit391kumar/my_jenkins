# capilatize==> to convert first letter of the word in upper case in the string.
test = "hello word. ankit kumar"
capitalized_test = test.capitalize()
print("capitalize():", capitalized_test)

#lower'
text = "HELLO"
lower_text = text.lower()
print("lower():", lower_text)
#upper
text = "hello"
UPPER_text = text.upper()
print("upper():", UPPER_text)
#count
text = "hello ankit ror"
count_e = text.count('a')
print("count():", count_e)
#startswith
text = "hello ankit ror"
startswith_ankit = text.startswith('hello')
print("startswith():", startswith_ankit)
#endswith
text = "hello ankit ror"
endswith_ror = text.endswith('boy')
print("endswith():", endswith_ror)
#find 
text = "hello ankit ror how are you you"
#find_word = text.find('ankit')
index_of_ankit = text.find('l')
print("find():", index_of_ankit)
#format
name = "ankit"
age = 34
native = "SRE"
message = "hello i am {} {} years old and i am from {}".format(name, age, native)
print("format():", message)
#index
text = "hello ankit ror how are you you"
index_x = text.index('i')
print("index():", index_x)

#join
words = ["Windows", "Error", "found"]
joined_word = ''.join(words)
print("join():", joined_word)
#replace
text = "   Ankit    Ror    "
replaced_word = text.replace("Ror", "Kumar")
print("replace():", replaced_word)

#strip
text = "   Ankit Ror    "
strip_word = text.strip()
print("strip():", strip_word)
#split
text = "ankit kumar ror from saharanpur"
split_text = text.split() # split whole string
#split_text = text.split(" ", 2) # split only first to char
print("split():", split_text)
#zfill
num = "123"
zfill_num = num.zfill(5)
print("zfill:", zfill_num)

#slicing

text = "abcdefghijklmnopqrstuvwxyz"
print(text[0:25:3]) # 0 first letter of string
# 25 total length of string
#2 jump in between




