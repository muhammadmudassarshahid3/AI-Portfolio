# Beginner Level (Strings Fundamentals) 
# 1. Length of a String 
# Write a program that reads a string and prints its length. 
# o Input: "hello world" → Output: 11 
# Hint: Use len(s). 

#  Solution:

# s = input("Enter a string: ")

# print("Length:", len(s))


# 2. Uppercase & Lowercase 
# Convert the input string to uppercase and lowercase. 
# o Input: "Python3" → Output: "PYTHON3", "python3" 
# Hint: Methods: s.upper(), s.lower().

# Solution:

# s = input("Enter a string: ")

# print("Uppercase:", s.upper())
# print("Lowercase:", s.lower())


# 3. Count a Character 
# Count how many times a given character appears in a string (case-sensitive). 
# o Input: "banana", "a" → Output: 3 
# Hint: Use s.count(ch).

# Solution:

# s = input("Enter a string: ")
# ch = input("Enter character to count: ")

# print("Count:", s.count(ch))


# 4. First & Last Character 
# Print the first and last character of a string; handle empty input. 
# o Input: "drawer" → Output: First: d, Last: r 
# Hint: Check empty with if not s; index via s[0] and s[-1]. 

# Solution:

# s = input("Enter a string: ")

# if not s:
#     print("String is empty")
# else:
#     print("First:", s[0])
#     print("Last:", s[-1])


# 5. Check Substring Presence 
# Check if a substring exists in a string. 
# o Input: "data science", "science" → Output: True 
# Hint: Use the in operator: sub in s.

# Solution:

# s = input("Enter main string: ")
# sub = input("Enter substring: ")

# print(sub in s)


# 6. Slice a String 
# Print a substring from index start to end (exclusive). 
# o Input: "programming", 3, 8 → Output: "gramm" 
# Hint: Use slicing: s[start:end].

# Solution:

# s = input("Enter a string: ")
# start = int(input("Enter start index: "))
# end = int(input("Enter end index: "))
# print(s[start:end])


# 7. Reverse a String 
# Reverse the string. 
# o Input: "Python" → Output: "nohtyP" 
# Hint: Slicing trick: s[::-1]. 

# Solution:

# s = input("Enter a string: ")

# print("Reversed:", s[::-1])


# 8. Replace Substring 
# Replace all occurrences of a word with another (case-sensitive). 
# o Input: "I love apples. Apples are great!", "apples", "oranges" 
# o Output: "I love oranges. Apples are great!" 
# Hint: s.replace(old, new) replaces exactly matching cases

# Solution:

# s = input("Enter a string: ")
# old = input("Enter word to replace: ")
# new = input("Enter replacement: ")

# result = s.replace(old, new)

# print(result)


# 9. Split and Join 
# Split a sentence on spaces and join with -. 
# o Input: "split this sentence" → Output: "split-this-sentence" 
# Hint: s.split() then "-".join(words).

# Solution:

# s = input("Enter a sentence: ")

# words = s.split()
# result = "-".join(words)

# print(result)


# 10. Strip Whitespace 
# Remove leading and trailing spaces. 
# o Input: "   padded text  " → Output: "padded text" 
# Hint: Use s.strip(). 

# Solution:

# s = input("Enter a string: ")

# print(s.strip())


# Intermediate Level (More Involved String Tasks) 
# 1. Count Vowels & Consonants 
# Count vowels and consonants (letters only; ignore digits/punctuation). 
# o Input: "Hello, World! 123" → Output: Vowels: 3, Consonants: 7 
# Hint: Iterate characters; check ch.isalpha(); membership test like ch.lower() in 
# "aeiou". 

# Solution:

# s = input("Enter a string: ")

# vowels = 0
# consonants = 0

# for ch in s:
#     if ch.isalpha():
#         if ch.lower() in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1

# print("Vowels:", vowels)
# print("Consonants:", consonants)


# 2. Palindrome Check (Ignore Case & Non-alphanumerics) 
# Determine if a string is a palindrome ignoring case and non-alphanumeric characters. 
# o Input: "A man, a plan, a canal: Panama!" → Output: True 
# Hint: Normalize with ''.join(ch.lower() for ch in s if ch.isalnum()); compare to 
# its reverse. 

# Solution:

# s = input("Enter a string: ")

# cleaned = ""

# for ch in s:
#     if ch.isalnum():
#         cleaned += ch.lower()

# if cleaned == cleaned[::-1]:
#     print("True")
# else:
#     print("False")


# 3. Title Case (Manual) 
# Convert a sentence to title case without using .title(). 
# o Input: "hELLO wORLD from PYTHON" → Output: "Hello World From Python" 
# Hint: Split into words; for each word: word[0].upper() + word[1:].lower() 
# (guard empty words).

# Solution:

# s = input("Enter a sentence: ")

# words = s.split()

# result = []

# for word in words:
#     new_word = word[0].upper() + word[1:].lower()
#     result.append(new_word)

# print(" ".join(result))

 
# 4. Find All Indices of a Substring (Allow Overlaps) 
# Return a list of starting indices where a substring occurs. 
# o Input: s="aaaa", sub="aa" → Output: [0, 1, 2] 
# Hint: Loop i from 0 to len(s) - len(sub); compare slices s[i:i+len(sub)].

# Solution:

# s = input("Enter main string: ")
# sub = input("Enter substring: ")

# indices = []

# for i in range(len(s) - len(sub) + 1):
#     if s[i:i + len(sub)] == sub:
#         indices.append(i)

# print(indices)


# 5. Character Frequency Dictionary 
# Build a frequency dictionary for characters (case-insensitive, skip spaces). 
# o Input: "Baa Baa Black Sheep" 
# o Output (order may vary): {'b':3,'a':5,'l':1,'c':1,'k':1,'s':1,'h':1,'e':3,'p':1} 
# Hint: Iterate for ch in s.lower(): and if ch != ' ': then count with a dict; 
# dict.get(ch, 0)+=1.

# Solution:

# s = input("Enter a string: ")

# frequency = {}

# for ch in s:
#     ch = ch.lower()

#     if ch != " ":
#         frequency[ch] = frequency.get(ch, 0) + 1

# print(frequency)


# 6. Anagram Checker 
# Check if two strings are anagrams (ignore spaces, punctuation, and case). 
# o Input: "Listen", "Silent" → Output: True 
# Hint: Normalize to letters with ch.isalpha() and lower(), then compare 
# sorted(s1) vs sorted(s2) or frequency dicts. 

# Solution:

# s1 = input("Enter first string: ")
# s2 = input("Enter second string: ")

# clean1 = ""
# clean2 = ""

# for ch in s1:
#     if ch.isalpha():
#         clean1 += ch.lower()

# for ch in s2:
#     if ch.isalpha():
#         clean2 += ch.lower()

# if sorted(clean1) == sorted(clean2):
#     print("True")
# else:
#     print("False")


# 7. Compress Repeated Characters (RLE-lite) 
# Compress runs of the same character as <char><count>. 
# o Input: "aaabbcaaaa" → Output: "a3b2c1a4" 
# Hint: Track current char and run length; flush when char changes or at the 
# end. 

# Solution:

# s = input("Enter a string: ")

# if not s:
#     print("")
# else:
#     result = ""
#     current = s[0]
#     count = 1

#     for i in range(1, len(s)):
#         if s[i] == current:
#             count += 1
#         else:
#             result += current + str(count)
#             current = s[i]
#             count = 1

#     result += current + str(count)

#     print(result)

# 8. Longest Word in a Sentence 
# Find the longest word; if multiple, return the first. Consider words as alphabetic 
# sequences. 
# o Input: "Find the longest_word here!" → Output: "longest" 
# Hint: Filter to letters using ''.join(ch for ch in token if ch.isalpha()); track max 
# by length.

# Solution:

# s = input("Enter a sentence: ")

# words = s.split()

# longest = ""

# for word in words:
#     clean_word = ""

#     for ch in word:
#         if ch.isalpha():
#             clean_word += ch

#     if len(clean_word) > len(longest):
#         longest = clean_word

# print("Longest word:", longest)


# 9. Remove Duplicate Characters but Keep Order 
# Remove duplicates while preserving the first occurrence order. 
# o Input: "banana" → Output: "ban" 
# Hint: Maintain a seen set; build result by adding chars not in seen. 

# Solution:

# sss = input("Enter a Input: ")
# seen = set()
# result = ""
# for x in sss:
#     if x not in seen:
#         result += x
#         seen.add(x)

# print(result)
        

# 10. Mask Email Username 
# Mask all but the first and last character of the username with *; keep domain intact. 
# o Input: "john.doe@example.com" → Output: "j******e@example.com" 
# Hint: Split on '@'; for the left part, if length ≥ 2, keep first and last and 
# replace middle with '*' * (len-2); if shorter, handle edge cases.

# Solution:

# ssst = input("Enter the Gmail :")
# username ,domain  = ssst.split("@")
# if len(username) >= 2:
#     masked = username[0] +"*"*(len(username)-2)+username[-1]
# else:
#     masked = username
# print(masked+"@"+domain)




