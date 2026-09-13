# Part A — Python Lists (10 Intermediate-Level Questions) 

# 1. Create a list comprehension that returns the squares of only the even numbers 
# from 0–20.

# Solution:

# square = [x**2 for x in range(21) if x%2 == 0]
# print(square)
# print("...............")


# 2. Given nums = [3, 1, 4, 1, 5, 9], sort the list without modifying the original. 
# Tip: Use sorted() instead of .sort(). 

# Solution:

# nums = [3, 1, 4, 1, 5, 9]
# new_nums = sorted(nums)
# print(new_nums)
# print("...............")


# 3. Remove duplicates from a list while preserving the original order. 
# Tip: Track seen values in a new list. 

# Solution:

# nums = [3, 1, 4, 1, 5, 9]
# list = []
# for x in nums:
#     if x not in list:
#         list.append(x)
# print(list)
# print("...............")


# 4. Flatten the nested list [[1, 2], [3, 4], [5]] into a single list using a list comprehension. 
# Tip: Use a nested loop inside the comprehension.

# Solution:

# nested = [[1, 2], [3, 4], [5]]
# flat = []
# for sublist in nested:
#     for x in sublist:
#      flat.append(x)
# print(flat)
# print("...............")


# 5. Given names = ['alice', 'Bob', 'charlie', 'DAVID'], sort them alphabetically but ignore 
# case. 

# Solution:

# names = ['alice', 'charle', 'Bob', 'DAVID']
# sorted_list = sorted(names, key=str.lower)
# print(sorted_list)
# print("...............")


# 6. Replace items from index 2–4 in a list with [100, 200] using slice assignment. 
# Tip: Use a[2:5] = [...]. 

# Solution:

# a = [10,20,30,40,50,60,70]
# a[2:4] = [100, 200]
# print(a)
# print("...............")


# 7. Write a program to find all indices of a value in a list (e.g., all indices of 7). 
# Tip: Use enumerate.

# Solution:

# a = [0,7,2,3,7,5,7]
# for i, x in enumerate(a):
#     if x == 7:
#         print(i)
# print("...............")


# 8. Create a new list containing only elements that appear exactly once in the original 
# list. 
# Tip: Use list.count() inside a comprehension.

# Solution:

# my_list = [1,3,1,4,2,3,5]
# result = [x for x in my_list if my_list.count(x) == 1]
# print(result)
# print("...............")
        

# 9. Rotate a list right by one position (e.g., [1,2,3,4] → [4,1,2,3]). 
# Tip: Use slicing: lst[-1:] + lst[:-1].

# Solution:

# my_list = [1,2,3,4]
# slicing = my_list[-1:] + my_list[:-1]
# print(slicing)
# print("...............")


# 10. Split a list into two lists: one with even numbers, one with odd numbers. 
# Tip: Create two comprehensions. 

# Solution:

# my_list = [1,2,3,4,5,6,7,8]
# my_odd  = [x for x in my_list if x%2 !=0]
# my_even = [x for x in my_list if x%2 ==0]
# print(my_odd,my_even)
# print("...............")


# Part B — Python Tuples (10 Intermediate-Level 
# Questions) 


# 1. Convert the list [1, 2, 3, 4] into a tuple and then unpack it into four variables. 
# Tip: Use tuple() and simple unpacking. 

# Solution:

# my_list = [1, 2, 3, 4]
# print(tuple(my_list))
# print("...............")


# 2. Given t = (('a', 1), ('b', 2), ('c', 3)), create a list of all second elements. 
# Tip: Use a comprehension: x[1]. 

# Solution:

# t = (('a', 1), ('b', 2), ('c', 3))
# c = [x for subtupple in t for x in subtupple]
# print(c[1::2])
# print("...............")


# 3. Given a sentence, return all unique words in lowercase. 
# Tip: Split the string → lowercase → convert to set. 

# Solution:

# my_string = input("Enter the Sentence:")
# c = set(my_string.lower().split(" "))
# print(c)
# print("...............")


# 4. Convert a list with duplicates into a set, then back to a sorted list. 
# Tip: Use sorted(set(list)).

# Solution:

# my_list = [1,4,2,2,3,6,5,3,7,6,8,9,10]
# my_set = set(my_list)
# result = sorted(my_set)
# print(result)
# print("...............")


# 5. Check if one set is a strict subset of another. 
# Tip: Use < operator.

# Solution:


# A = {1, 2}
# B = {1, 2, 3}

# if A < B:
#     print("A is a strict subset of B")
# else:
#     print("A is not a strict subset of B")
# print("...............")


# 6. Use a set comprehension to collect all squares of numbers from 1–15 that are 
# divisible by 3. 
# Tip: Write {x*x for x in ... if x % 3 == 0}. 

# Solution:

# my_set = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15}
# result = {x*x for x in my_set if x % 3 == 0}
# print(result)
# print("...............")


# 7. Count how many duplicate values exist in a list using sets. 
# Tip: Compare lengths: len(list) - len(set(list)).

# Solution:

# my_list = [1,4,2,2,3,6,5,3,7,6,8,9,10]
# Length = (len(my_list)-len(set(my_list)))
# print("Dublicate Values:",Length)
# print("...............")


# 8. Write a program to remove all vowels from a string using a set. 
# Tip: Use a vowel set and filter characters. 

# Solution:

# my_string = input("Enter the String:")
# my_vovels = {"a","e","i","o","u"}
# for x in my_string:
#     if x.lower() in my_vovels:
#         continue
#     print(x,end="")
# print("...............")


# 9. Find the symmetric difference between two sets. 
# Tip: Use the ^ operator.

# Solution:

# A = {1,2,3,4}
# B = {3,4,5,6}
# c = A^B
# print(c)
# print("...............")


# 10. Check if two strings are anagrams using set comparison (unique characters only). 
# Tip: Compare set(str1) with set(str2). 

# Solution:

# str1 = input("Enter the String:")
# str2 = input("Enter the String:")
# c = str1.lower()
# d = str2.lower()
# if set(c) == set(d):
#     print("String1 and String2 are Anagrams")
# else:
#     print("They are not Anagrams")
# print("...............")


# Part D — Python Dictionaries (10 Intermediate-Level 
# Questions) 


# 1. Count word frequencies in a sentence and store the results in a dictionary. 
# Tip: Use d[word] = d.get(word, 0) + 1. 

# Solution:

# sentence = "I like AI and I like Python"

# words = sentence.split()

# d = {}

# for word in words:
#     d[word] = d.get(word, 0) + 1

# print(d)
# print("...............")


# 2. Invert a dictionary where all values are unique. 
# Tip: Swap key and value in a loop. 

# Solution:

# d = {"Pakistan": "Islamabad","France": "Paris","Italy": "Rome"}
# inverted = {}

# for key, value in d.items():
#     inverted[value] = key

# print(inverted)
# print("...............")


# 3. Merge two dictionaries where second dictionary overrides first. 
# Tip: Use {**dict1, **dict2} or dict1 | dict2 (Python 3.9+).

# Solution:

# dict1 = {"name": "Ali","age": 20}
# dict2 = {"name": "Ali","age": 25}
# c = dict1 | dict2
# print(c)
# print("...............")


# 4. Group words by their first letter into a dictionary of lists. 
# Tip: Use setdefault. 

# Solution:

# words = ["apple", "ant", "banana", "ball", "cat", "car"]

# result = {}

# for word in words:
#     first = word[0]
#     result.setdefault(first, []).append(word)

# print(result)
# print("...............")


# 5. Filter a dictionary to keep only entries with values greater than 50. 
# Tip: Use a dictionary comprehension.

# Solution:

# words = {"a":20,"b":30,"c":60,"d":50,"e":30}
# XY = {key: value for key,value in words.items() if value > 50}
# print(XY)
# print("...............")


# 6. Given a nested dictionary, safely access a deeply nested key. 
# Tip: Chain .get() calls with default {}.

# Solution:

# A = {"Name":"Mudassar","details":{"Age":20}}
# x = {A.get("details","unknown").get("Age","unknown")}
# print(x)
# print("...............")


# 7. Write a dictionary comprehension that maps numbers 1–10 to their cubes. 
# Tip: {x: x**3 for x in range(1,11)}. 

# Solution:

# c = {x: x**3 for x in range(1,11)}
# print(c)
# print("...............")


# 8. Find the key with the highest value in a dictionary. 
# Tip: Use max(d, key=d.get).

# Solution:

# words = {"a":20,"b":30,"c":60,"d":50,"e":30}
# ZX = max(words,key=words.get)
# print(ZX)
# print("...............")


# 9. Combine two lists into a dictionary (keys from first list, values from second). 
# Tip: Use zip(). 

# Solution:

# A = ["name", "age", "gender", "class"]
# B = ["mudassar",18,"man","12th"]
# c = zip(A , B)
# print(dict(c))
# print("...............")


# 10. Remove all keys from a dictionary whose values are None. 
# Tip: Check value before adding to new dict.

# Solution:

# C = {'name': 'mudassar', 'age': None, 'gender': 'man', 'class': '12th'}
# D = {key: value for key, value in C.items() if value is not None}
# print(D)
# print("...............")
