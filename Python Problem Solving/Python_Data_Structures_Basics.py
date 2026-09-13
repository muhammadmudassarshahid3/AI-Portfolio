# Part A — Python Lists (10 Beginner Questions) 

# 1. Create a list nums = [3, 1, 4, 1, 5] and print the first and last elements. 
# Tip: Use nums[0] and nums[-1]. 
 
# Solution:

# nums = [3,1,4,1,5]
# print(nums[0])
# print(nums[-1])
# print("...............")


# 2. Find the length of the list colors = ['red', 'blue', 'green']. 
# Tip: Use len(colors). 

# Solution:

# colors = ['red', 'blue', 'green']
# c = len(colors)
# print(c)
# print("...............")


# 3. Append 'yellow' to the list colors = ['red', 'blue']. 
# Tip: Use append().

# Solution:

# colors = ['red', 'blue']
# colors.append("yellow")
# print(colors)
# print("...............")


# 4. Insert 'orange' at index 1 in fruits = ['apple', 'banana']. 
# Tip: Use insert(index, value). 

# Solution:

# fruits = ['apple', 'banana']
# fruits.insert(1,"orange")
# print(fruits)
# print("...............")


# 5. Remove 'banana' from fruits = ['apple', 'banana', 'grapes']. 
# Tip: Use remove(value).

# Solution:

# fruits = ['apple', 'banana', 'grapes']
# fruits.remove("banana")
# print(fruits)
# print("...............")


# 6. Pop the last element from items = [10, 20, 30] and print the popped value. 
# Tip: Call items.pop(). 

# Solution:

# items = [10, 20, 30]
# c = items.pop(2)
# print(c)
# print(items)
# print("...............")


# 7. Check if 3 is in the list nums = [1, 2, 3, 4]. 
# Tip: Use the in operator. 

# Solution:

# nums = [1, 2, 3, 4]
# print(3 in nums)
# print("...............")


# 8. Print the slice [2, 3] from the list [0, 1, 2, 3, 4]. 
# Tip: Use slicing: a[2:4]

# Solution:

# list = [0, 1, 2, 3, 4]
# print(list[2:4])
# print("...............")


# 9. Replace the element at index 1 in a = [5, 10, 15] with 12. 
# Tip: Use assignment: a[1] = 12.

# Solution:

# a = [5, 10, 15]
# a[1] = 12
# print(a)
# print("...............")


# 10. Count how many times 2 appears in [1, 2, 2, 3, 2]. 
# Tip: Use list.count(value).

# Solution:

# List = [1, 2, 2, 3, 2]
# c = List.count(2)
# print(c)
# print("...............")


# Part B — Python Tuples (10 Beginner Questions) 
# 1. Create a tuple t = (10, 20, 30) and print the second element. 
# Tip: Tuples use indexing: t[1]. 

# Solution:

# t = (10, 20, 30)
# print(t[1])
# print("...............")


# 2. Find the length of tuple ('a', 'b', 'c'). 
# Tip: Use len().

# Solution:

# tuple = ('a', 'b', 'c')
# print(len(tuple))
# print("...............")


# 3. Unpack the tuple (4, 5) into variables x and y. 
# Tip: x, y = (4, 5). 

# Solution:

# tuple = (4, 5)
# x,y = (4, 5)
# print(x,y)
# print("...............")


# 4. Check if 'b' is in the tuple ('a', 'b', 'c'). 
# Tip: Use 'b' in tuple.

# Solution:

# tuple = ('a', 'b', 'c')
# print("b" in tuple)
# print("...............")


# 5. Create an empty tuple and print its type. 
# Tip: Empty tuple is (). 

# Solution:

# tuple = ()
# print(type(tuple))
# print("...............") 


# 6. Concatenate (1, 2) and (3, 4) into a new tuple. 
# Tip: Use + operator. 

# Solution:

# T1 = (1, 2)
# T2 = (3, 4)
# print("T3:",T1+T2)
# print("...............") 


# 7. Repeat (7,) three times. 
# Tip: Use tuple * number.

# Solution:

# Tuples = (7,)*3
# print(Tuples)
# print("...............") 


# 8. Find the index of 2 in (1, 2, 3, 2). 
# Tip: Use index() method.

# Solution:

# Tuple = (1, 2, 3, 2)
# T = Tuple.index(2)
# print("INDEX:",T)
# print("...............")


# 9. Count how many times 2 appears in (1, 2, 3, 2). 
# Tip: Use count() method. 

# Solution:

# Tu = (1, 2, 3, 2)
# print(Tu.count(2))
# print("...............")


# 10. Create a single‑element tuple containing the value 5. 
# Tip: Remember to use a comma: (5,).

# Solution:

# Tuple = (5,)
# print(Tuple)
# print("...............")


# Part C — Python Sets (10 Beginner Questions)

# 1. Create a set from [1, 2, 2, 3] and print it. 
# Tip: Use set(list).

# Solution:
# list = [1, 2, 2, 3]
# print(set(list))
# print("...............")


# 2. Add element 4 to the set {1, 2, 3}. 
# Tip: Use add().

# Solution:

# set = {1, 2, 3}
# set.add(4)
# print(set)
# print("...............")


# 3. Remove element 2 from the set {1, 2, 3}. 
# Tip: Use remove().

# Solution:

# set = {1, 2, 3}
# set.discard(2)
# print(set)
# print("...............")


# 4. Check if 5 is in the set {1, 3, 5}. 
# Tip: Use in operator. 

# Solution:

# set = {1, 3, 5}
# print(5 in set)
# print("...............")


# 5. Find the length of set {10, 20, 30}. 
# Tip: Use len().

# Solution:

# set = {10, 20, 30}
# c = len(set)
# print("The Length Of Set:",c)
# print("...............")


# 6. Clear all elements from the set {1, 2, 3}. 
# Tip: Use clear(). 

# Solution:

# set = {1, 2, 3}
# set.clear()
# print(set)
# print("...............")


# 7. Create a set {'a', 'b'} and add 'c' only if it’s missing. 
# Tip: Check membership first: if 'c' not in s:. 

# Solution:

# myset = {'a', 'b'}
# print("c" in myset)
# myset.add("c")
# print(myset)
# print("...............")


# 8. Convert list ['a', 'a', 'b'] into a set to remove duplicates. 
# Tip: Casting removes duplicates automatically. 

# Solution:

# list1 = ['a', 'a', 'b']
# print(set(list1))
# print("...............")


# 9. Create two sets and print their union. 
# Tip: Use set1 | set2.

# Solution:

# Set1 = {1,2,3}
# Set2 = {3,5,6}
# Set3 = Set1|Set2
# print(Set3)
# print("...............")


# 10. Create two sets and print their intersection. 
# Tip: Use set1 & set2. 

# Solution:

# Set1 = {1,9,3}
# Set2 = {3,8,6}
# Set3 = Set1&Set2
# print(Set3)
# print("...............")


# Part D — Python Dictionaries (10 Beginner Questions) 

# 1. Create a dictionary {'name': 'Ali', 'age': 25} and print the name. 
# Tip: Use d['name'].

# Solution:

# dictionary1 = {'name': 'Ali', 'age': 25}
# print(dictionary1['name'])
# print("...............")


# 2. Add key 'city': 'Lahore' to a dictionary. 
# Tip: Use assignment: d['city'] = 'Lahore'.

# Solution:

# dictionary1 = {'name': 'Ali', 'age': 25}
# dictionary1['city'] = 'Lahore'
# print(dictionary1)
# print("...............")


# 3. Change 'age' in {'name': 'Ali', 'age': 25} to 30. 
# Tip: Assign a new value: d['age'] = 30.

# Solution:

# dictionary1 = {'name': 'Ali', 'age': 25}
# dictionary1['age'] = 30
# print(dictionary1)
# print("...............")


# 4. Delete key 'age' from a dictionary. 
# Tip: Use del d['age']. 

# Solution:

# dictionary1 = {'name': 'Ali', 'age': 25}
# del dictionary1['age']
# print(dictionary1)
# print("...............")


# 5. Check if key 'salary' exists in a dictionary. 
# Tip: Use in operator.

# Solution:

# dictionary1 = {'name': 'Ali', 'age': 25}
# print('salary' in dictionary1)
# print("...............")


# 6. Print all keys from {'a': 1, 'b': 2}. 
# Tip: Use d.keys(). 

# Solution:

# dic = {'a': 1, 'b': 2}
# c = (dic.keys())
# print(c)
# print("...............")


# 7. Print all values from a dictionary. 
# Tip: Use d.values().

# Solution:

# dic = {'a': 1, 'b': 2}
# d = (dic.values())
# print(d)
# print("...............")


# 8. Iterate and print key‑value pairs from {'x': 10, 'y': 20}. 
# Tip: Use for k, v in d.items(). 

# Solution:

# c = {'x': 10, 'y': 20}
# for k,v in c.items():
#     print(k,",",v)
# print("...............")


# 9. Use get() to safely read key 'score' from an empty dictionary. 
# Tip: Use d.get('score', default_value).

# Solution:

# c = {}
# r = c.get('score', 0)
# print(r)
# print("...............")


# 10. Create a dictionary from two lists: keys = ['a','b'], values = [1,2]. 
# Tip: Use dict(zip(keys, values)). 

# Solution:

# keys = ['a','b']
# values = [1,2]
# c = dict(zip(keys,values))
# print(c)
# print("...............")
