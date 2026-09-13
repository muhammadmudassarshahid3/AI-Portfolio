# String Manipulation


# 1 Write a program to create a new string  made of an input string's first,middle and last character.
# Solution:


#I = str(input("Enter String:"))

#First = I[0]

#Length= len(I)

#Middle1= Length//2

#Middle = I[Middle1]

#End   = I[-1]

#New_String = (First,Middle,End)

#print("New String:",New_String)
#("..................")



# 2 write a program to count occurences of all characters within a string given
# Solution:


#string = str(input("Enter the String:"))
#length = len(string)

#print("Length:",length)
#print("...............")



# 3 Reverse a given string
# Solution:


#String = str(input("Enter the String   :"))

#Reverse = String[::-1]

#print("Reverse of a string:",Reverse)
#print("...............")



# 4 Split a string on hyphens
# Solution:


#String = str(input("Enter a String:"))

#Hyphen = (String).split()

#Hyphens = "-".join(Hyphen)

#print("New String    :",Hyphens)
#print("...............")



# 5 remove special symbols / puntuation from a string
# Solution:


#String = (input("Enter the string:"))

#for x in String:

#    if x in ("!@#$%^&*()_-+=~`';:,<.>/?|\\"):

#        continue

#    print(x, end="")
#print()
#print("...............")
    



# LIST MANIPULATION

# 1 Reverse a list in Python
# Solution:


#L = ["Apple",5,1.34,False,"He is men"]

#print(L[::-1])
#print("...............")



# 2 Turn every item of a list into its square
# Solution:

#L = [3.234,5,678,4,4.5]
#for X in L:
#  print(X*X,end="  ")
#print()
#print("...............")


# 3 Remove empty strings from the list of strings
# Solution:

#L = ["Pakistan","","will","win","","worldcup"]
#for X in L:
#    if X in (""):
#        continue
#    print(X,end=" ")
#print()
#print("...............")


# 4 Add new item to list after a specific item
# Solution:

#List = ["Pakistan","India","Nepal","Berlin"]
#List.insert(0,"China")
#print("List after Insert:",List)
#print("...............")


# 5 Replace List item with new value if found
# Solution:

#List = ["str","Pakistan",5,5.8865,3.1416]
#List[1] = "India"
#print(List)
#print("...............")


# Dictionary Manupulation

# 1 Check if a value exists in a dictionary
# Sollution:


#House = {"Area":33100 , "Housenumber": 4 , "Society":"Gulshan-e-Iqbal"}
#for flat in House:
#    print(flat,end=" ")
#print()
#for flat in House:
#    Area = House[flat]
#    print(Area,end=" ")
#print()
#print("...............")


# 2 Get the key of a minimum value from the following dictionary
# Solution:

#student = {"b": 1000, "a": 6000, "c": 700, "d": 800}
#minimum_key = min(student, key=student.get )
#print(minimum_key)
#print("...............")


# 3 Delete a list of keys from a dictionary
# Solution:

#Dic = {"A":444,"B":5.54,"C":"Hello","Dictionary":"hello"}
#DIC1 = ["A","Dictionary"]
#for x in DIC1:
#    del Dic[x]
#print(Dic)
#print("...............")


#Tuple Manipulation

# 1 Reverse the tuple
# Solution:

#T = (9,6,"AN",7.87)
#print(T[::-1])
#print("...............")


# 2 Access value 20 from the tuple
# Solution:

#TU = (9,6,20,"AN",7.87)
#print(TU[2])
#print("...............")


# 3 Swap two tuples in Python
# Solution:

#T1 = (43,56,41,98)
#T2 = (1,2,3,4)
#temt = T1
#T1 = T2
#T2 = temt
#print("The value of T1:",T1)
#print("The value of T2:",T2)
#print("...............")


#Loop Manipulation 

# 1 Print first 10 natural numbers using while 
# Solution:

#Number = 1
#while Number<=10:
#       print(Number)
#       Number = Number+1
#print("...............")


# 2 Take Input from user , and print even number till that input number
# Solution:
    
#c = int(input("Enter the Number :"))
#if c % 2 == 0:
#  for x in range(2,c+1,2):
#            print(x)
#else:
#   for x in range(2,c+1,2):
#       print(x)
       

# 3  Take Input from user , and print odd number till that input number
# Solution:

#c = int(input("Enter the Number :"))
#for x in range(1,c+1,2):
#       print(x)
#print("...............")


# 4 Take Input from user , and print prime number till that input number
# Solution:

#number  = int(input("Enter the Number:"))
#for x in range(2,number+1):
#    is_prime = True
#    for y in range(2,x):
#        if x % y == 0:
#          is_prime = False
#          break
#    if is_prime:
#        print(x)
#print("...............")


# 5 Print multiplication table of a given number 
# Solution:

#number  = int(input("Enter the Number:"))
#for x in range(1,11):
#    print(number*x)
#print(...............) 
