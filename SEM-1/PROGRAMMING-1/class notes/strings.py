# why strings is immutable in python
# because strings are immutable in Python,
# it means that once a string is created,
# it cannot be changed. Any operation that modifies a string will create
# a new string instead of modifying the original one. This immutability is due to
# the way strings are stored in memory and helps with performance optimization and security.
# in place modification of strings is not allowed, and any attempt to change a string will result in the creation of a new string object.
# This behavior ensures that strings can be safely shared and used in different parts of a program without the risk of unintended side effects.

# strings are iterable in python for example we can use for loop to iterate over the characters of a string.

# index error in python is raised when we try to access an index that is out of bounds for the string.
# always use len() function to check the length of the string before accessing an index to avoid index error.
# we cannot use len with int function as it is not iterable, it will raise a type error.
# we only use len with iterable objects like strings, lists, tuples, etc which are iterable objects.

# [11: means after 11th index, :11 means before 11th index, [11:20]
# means from 11th index to 20th index, [:20] means from start to 20th index,
# [11:] means from 11th index to end of string, [-1] means last character of string, [-2] means second last character of string,
# [-3:-1] means from third last character to second last character of string]

# [ 0:26:2] means from 0th index to 26th index with a step of 2, [::-1] means reverse the string,
# a.isalnum() method returns True if all characters in the string are alphanumeric (letters and numbers) and there is at least one character, otherwise it returns False.
a = "5rs"
print(a.isalnum())

# difference between .isdecimal() and .isdigit() methods in python
# isdecimal() method returns True if all characters in the string are decimal characters (0-9) and there is at least one character, otherwise it returns False.
# isdigit() method returns True if all characters in the string are digits (0-9, superscripts, subscripts, etc.) and there is at least one character, otherwise it returns False.
# isdecimal() method is more strict than isdigit() method, as it only considers decimal characters, while isdigit() method considers a wider range of digit characters.
# basically isdecimal() method is a subset of isdigit() method, as all decimal characters are also considered digits, but not all digit characters are considered decimal characters.
# isnumeric() method returns True if all characters in the string are numeric characters (0-9, superscripts, subscripts, fractions, etc.) and there is at least one character, otherwise it returns False.
# floating values are very dangerous in python as they are not precise and can lead to unexpected results, so it is better to avoid using floating values in python.
#  imp isidentifier() method returns True if the string is a valid identifier (a name that can be used to identify a variable, function, class, etc.) and there is at least one character, otherwise it returns False.
print(a.isidentifier())
# here a was false beacause it starts with a number which is not allowed in identifiers in python.
# the rules for valid identifiers in python are:
# 1. An identifier can only contain letters (a-z, A-Z), digits (0-9), and underscores (_).
# 2. An identifier cannot start with a digit.
# 3. An identifier cannot be a reserved keyword in Python (like if, else, while, etc.).
# 4. An identifier can be of any length, but it is recommended to keep it concise and meaningful.
# 5. Identifiers are case-sensitive, meaning that "myVariable" and "myvariable" would be considered different identifiers.


# difference betwen isdecimal(), isdigit(), and isnumeric() methods in python
# isdecimal() method returns True if all characters in the string are decimal characters (0-9) and there is at least one character, otherwise it returns False.
# isdigit() method returns True if all characters in the string are digits (0-9, superscripts, subscripts, etc.) and there is at least one character, otherwise it returns False.
# isnumeric() method returns True if all characters in the string are numeric characters ( 0-9, superscripts, subscripts, fractions, etc.) and there is at least one character, otherwise it returns False.
# negative numbers are not considered as numeric characters, so isdecimal(), isdigit(), and isnumeric() methods will return False for negative numbers.
# floating numbers are not considered as numeric characters, so isdecimal(), isdigit(), and isnumeric() methods will return False for floating numbers.
# isdecimal < isdigit < isnumeric

# string modification in python is not allowed as strings are immutable in python, so any operation that modifies a string will create a new string instead of modifying the original one.
# some methods that modify a string and return a new string are:
# 1. upper() method returns a new string with all characters in uppercase.
# 2. lower() method returns a new string with all characters in lowercase.
# 3. capitalize() method returns a new string with the first character in uppercase and the rest in lowercase.
# 4. title() method returns a new string with the first character of each word in uppercase and the rest in lowercase.
# 5. strip() method returns a new string with leading and trailing whitespace removed.
# 6. replace() method returns a new string with all occurrences of a specified substring replaced with another substring.
# 7. join() method returns a new string that is the concatenation of the elements of an iterable, separated by a specified separator.
# 8. split() method returns a list of substrings that are separated by a specified separator.
# 9. format() method returns a new string that is formatted according to a specified format string and arguments.
# 10. f-strings (formatted string literals) return a new string that is formatted according to a specified format string and expressions.
# 11 .find() method returns the index of the first occurrence of a specified substring in a string, or -1 if the substring is not found.


# it gives position of first character of substring in string, if substring is not found it returns -1.

# you can do concatanation of strings using + operator, but it is not recommended
# as it creates a new string every time, which can be inefficient for large strings or in loops.
# Instead, use join() method or f-strings for better performance and readability.
# lexicographic comparison of strings in python is done using comparison operators like <, >, <=, >=, ==, !=. The comparison is done based on the Unicode code points of the characters in the strings.
# The comparison is case-sensitive, meaning that uppercase letters are considered less than lowercase letters. For example, "A" < "a" is True because the Unicode code point of "A" (65) is less than that of "a" (97).
# x<5<x*10<100 , for this evaluation python will first evaluate x<5, if it is True then it will evaluate x*10<100, if it is also True then the whole expression will be True, otherwise it will be False.
# associativibiity in python is left to right for comparison operators, meaning that if there are multiple comparison operators in an expression, they will be evaluated from left to right. For example, in the expression x < 5 < x * 10 < 100, Python will first evaluate x < 5, then x * 10 < 100,
# and finally combine the results to determine the overall truth value of the expression.
# except exponents operators, which have right-to-left associativity. For example, in the expression 2 ** 3 ** 2, Python will first evaluate 3 ** 2, then raise 2 to that power, resulting in 512.
