Strings in Python

# Strings: Sequences of characters used to represent text.

# Immutability: Once created, a string cannot be changed.

# String Methods: Various methods for case conversion, stripping, splitting, joining, finding, and replacing text.

# Formatting: Methods to combine and format strings dynamically.

# Indexing and Slicing: Techniques to access specific characters or substrings.

# Escape Characters: Special characters used for control purposes within strings.

# Multiline Strings: Strings that span multiple lines using triple quotes.


# Slicing in Python allows you to extract a portion (substring) of a string using the syntax:

# string[start:stop:step]

# 	•	start → index to start the slice (inclusive)
# 	•	stop → index to end the slice (exclusive)
# 	•	step → interval between characters (optional)
# Notes:
# Indexing starts at 0.

# Negative indexes start from the end: -1 is the last character.

# If step is negative, slicing moves right to left (reverse).

# ###########################################################################


 Lists in Python are ordered collections of items.


# They are mutable, meaning you can change their contents after creation.

# Lists are defined by enclosing comma-separated values within square brackets [ ].

# They support indexing and slicing operations, allowing you to access individual elements or a subset of elements.

# Common operations on lists include appending, inserting, deleting, and updating elements.


Tuple

# Tuples are similar to lists but with one crucial difference: they are immutable.
# Once created, you cannot change the contents of a tuple.
# Tuples are defined by enclosing comma-separated values within parentheses ( ).
# They are often used to represent fixed collections of items, such as coordinates, database records, or function arguments.
# Tuples support indexing and slicing like lists but lack methods for modification.


Sets

# A set is an unordered collection of unique items.

# It is used when you want to store multiple values but don’t want any duplicates.

# Sets are mutable, meaning you can add or remove items.

# Since they are unordered, they do not maintain any index or position.

# Useful for operations like union, intersection, and difference.

Dictionary:

# Dictionaries are unordered collections of key-value pairs.

# Each key in a dictionary must be unique and immutable (such as a string, number, or tuple).

# Values in a dictionary can be of any data type and can be mutable or immutable.

# Dictionaries are defined by enclosing comma-separated key-value pairs within curly braces { }, with keys and values separated by colons :. For example, {key1: value1, key2: value2}.

# They are commonly used for fast lookups and mappings between related pieces of information.

# Dictionaries support operations to add, remove, and modify key-value pairs, as well as methods to access keys, values, or key-value pairs.