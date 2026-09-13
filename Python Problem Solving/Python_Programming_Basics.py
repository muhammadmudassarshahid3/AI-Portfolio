# Python Programming Assignment: 
# Fundamentals



# Topics: I/O Functions, Variables, & Operators 
# Part 1: Input & Output Functions (print & input)



# 1. Write a program to print "Hello, World!" and your name on two separate lines

# Solution:

# print("Hello, World!")
# print("Mudassar Shahid")
# print("...............")


# 2. Ask the user for their favorite color using input() and print "Your favorite color is [color]". 

# Solution:

# color = input()
# print("Your favorite color is",color)
# print("...............")


# 3. Use a single print() statement to display three different words separated by a hyphen (-).

# Solution:

# print("MY-NAME-MUDASSAR")
# print("...............")


# 4. Prompt the user for their birth year and print their age (assume the current year is 2026). 

# Solution:

# user = int(input("Enter Birth Year:"))
# c = 2026-user
# print("Age of User:",c)
# print("...............")


# 5. Print the result of 5 + 5 such that the output is: The sum of 5 and 5 is 10. 

# Solution:

# print("The sum of 5 + 5 is",5+5)
# print("...............")


# 6. Use the end parameter in print() to join two separate print statements with a space. 

# Solution:

# print("my name is",end=" ")
# print("mudassar")
# print("...............")


# 7. Write a program that takes two strings from the user and prints them joined together.

# Solution:

# c = input("ENTER THE STRING:")
# d = input("ENTER THE STRING:")
# print(c,end="")
# print(d)
# print("...............")

# 8. Create a greeting that takes a user's name and prints "Welcome, [Name]!" in all uppercase. 

# Solution:

# ca = input("ENTER THE NAME:")
# Name = ca.upper()
# print("WELCOME",Name,"!")
# print("...............")


# 9. Ask for a user's city and country, then print them in the format: "City, Country". 

# Solution:

# cas = input("ENTER THE CITY:")
# cad = input("ENTER THE COUNTRY:")
# print(cas,cad)
# print("...............")


# 10. Experiment: What happens if you try to add a string and an integer in a print statement? 
# Write a code snippet that fixes this using str().

# Solution:

# age = 15
# print("My age is " + str(age))
# print("...............")


# Part 2: Variables & Data Types 

#V Focus: Direct Assignment and User Input Assignment for Int, Float, String, Complex, and 
# Boolean. 


# 11. Create an integer variable age and a float variable height. Print their types. 

# Solution:

# Age = 20 
# Height = 6.2
# print(type(Age))
# print(type(Height))
# print("...............")


# 12. Store the value 3 + 4j in a variable. Print the variable and its type.

# Solution:

# Variable = 3 + 4j
# print(Variable)
# print(type(Variable))
# print("...............")


# 13. Create a boolean variable is_python_fun and set it to True.

# Solution:

# is_python_fun = bool(1)
# print(is_python_fun)
# print("...............")


# 14. Method 1: Assign three different values to three variables in a single line.

# Solution:

# apple,ball,cat = 3,3.32,3+6j
# print(apple,ball,cat)
# print("...............")


# 15. Method 2: Assign the same value to three different variables in a single line

# Solution:

# apple=ball=cat= 3
# print(apple,ball,cat)
# print("...............")


# 16. Take a numeric input from a user and convert it to a float.

# Solution:

# user = int(input("Enter the Value"))
# print(float(user))
# print("...............")


# 17. Take a string input "100" and convert it to an int. 

# Solution:

# string = "100"
# print(type(string))
# c = (int(string))
# print(type(c))
# print("...............")


# 18. Create a variable with a complex number and print only its real part.

# Solution:

# variable = 3+4j
# print(variable.real)
# print("...............")


# 19. Define a string variable containing a paragraph and print its length. 

# Solution:

# my_String = "Hy myself mudassar shahid i am AI Engineer"
# print("Length:",len(my_String))
# print("...............")


# 20. Swap the values of two variables a and b without using a third variable.

# Solution:

# a = 20 
# b = 30 
# a,b = b,a
# print(a,b)
# print("...............")


# Part 3: Arithmetic Operators 


# 21. Write a program to calculate the area of a rectangle (Length × Width). 

# Solution:

# Length = float(input("Enter the length of rectangle :"))
# Width = float(input("Enter the Width of rectangle  :"))
# print("Area of rectangle:",Length*Width)
# print("...............")


# 22. Take two numbers and print the result of the first raised to the power of the second (a^b).

# Solution:

# my_num1 = int(input("Enter the Power Number :"))
# my_num2 = int(input("Enter the Base Number  :"))
# Result = my_num2**my_num1
# print("Result:",Result)
# print("...............")


# 23. Demonstrate the difference between / (division) and // (floor division) with the numbers 10 
# and 3.

# Solution:

# c = 10/3
# d = 10//3
# print(c,d)
# print(".................")


# 24. Use the modulus operator % to find the remainder when 25 is divided by 4. 

# Solution:

# H = 25%4
# print(H)
# print(".................")


# 25. Calculate the average of five numbers entered by the user.

# Solution:

# Num1 = float(input("Enter the first number:"))
# Num2 = float(input("Enter the second number:"))
# Num3 = float(input("Enter the third number:"))
# Num4 = float(input("Enter the fourth number:"))
# Num5 = float(input("Enter the fifth number:"))
# USER = (Num1+Num2+Num3+Num4+Num5)/5
# print("The average of five numbers:",USER)
# print(".................")


# 26. Create a program that converts minutes into hours and remaining minutes. 

# Solution:


# Minutes = int(input("Enter Minutes:"))
# Hours   = Minutes//60
# Remaining_Minutes = Minutes%60
# print("Hours            :",Hours)
# print("Remaining Minutes:",Remaining_Minutes)
# print(".................")


# 27. Calculate the area of a circle where Area = \pi r^2 (Use 3.14 for \pi). 

# Solution:

# pi = 3.14
# r = float(input("Enter the Radius:"))
# Area = pi*r**2
# print("Area of a circle:",Area)
# print(".................")


# 28. Find the cube of a number entered by the user. 

# Solution:

# Number = float(input("Enter the Number:"))
# cube = Number*Number*Number
# print("The Cube of a Number  :",cube)
# print(".................")


# 29. Perform the calculation 10 + 5 * 2. Does Python follow PEMDAS? Prove it with code. 

# Solution:

# calculation = 10 + 5 * 2
# print(calculation)
# print(".................")


# 30. Write a program to calculate simple interest: (P \times R \times T) / 100. 

# Solution:

# P = float(input("Enter the Number:"))
# R = float(input("Enter the Number:"))
# T = float(input("Enter the Number:"))
# SI = (P*R*T)/100
# print("Simple interest:",SI)
# print(".................")


# Part 4: Comparison & Logical Operators 


# 31. Compare two numbers entered by the user and print if the first is greater than the second. 

# Solution:

# P = float(input("Enter the First Number:"))
# T = float(input("Enter the Second Number:"))
# if P>T:
#     print(P,T)
# else:
#     print("First number is not Greater then Second number")
# # print(".................")


# 32. Check if a user-entered number is even (Number % 2 == 0) and print the Boolean result. 
   
# Solution:

# P = int(input("Enter the Number:"))
# Result = P % 2 == 0
# print(Result)
# # print(".................")


# 33. Write a program that checks if a number is between 10 and 50 (inclusive) using and.

# Solution:

# P = int(input("Enter the Number:"))
# if P>=10 and P<=50:
#     print("Number in range")
# else:
#     print("Nunber is not in range")
# print(".................")


# 34. Check if a string entered by the user is equal to "Python". 

# Solution:

# P = input("Enter the String:")
# if P == "Python":
#     print("String is Python")
# else:
#     print("Not Python")
# print(".................")


# 35. Use the or operator to check if a user is either "Admin" or "Superuser".

# Solution:

# User = input("Enter your role:")
# if User == "Admin" or User == "Superuser":
#     print("Access allowed")
# else:
#     print("Access denied")
# print(".................")


# 36. Demonstrate the not operator by reversing a Boolean variable. 

# Solution:

# a = True
# print(a)
# print(not a)
# print(".................")


# 37. Compare two floating-point numbers: 0.1 + 0.2 == 0.3. Explain the result. 

# Solution:

# Result = 0.1 + 0.2 == 0.3
# print(Result)
# print(".................")


# 38. Take a user's age and check if they are NOT under 18.

# Solution:

# User = int(input("Enter User Age:"))
# if not User < 18:
#     print("User is not under 18")
# else:
#     print("User is under 18")
# print(".................")


# 39. Check if a number is positive and odd using logical operators.

# Solution:

# P = int(input("Enter the Number:"))
# if P>0 and P%2 == 1:
#     print("Number is positive and odd")
# else:
#     print("Number is not positive and odd")
# print(".................")


# 40. Compare the lengths of two strings provided by the user.
 
# Solution:

# L1 = input("Enter the string:")
# L2 = input("Enter the string:")
# Length1 = len(L1)
# Length2 = len(L2)
# L3 = Length1==Length2
# print(L3)
# print(".................")


# Part 5: Assignment Operators with Arithmetic 


# 41. Initialize a variable x = 10. Use += to add 5 to it. 

# Solution:

# x = 10
# x += 5
# print(x)
# print(".................")


# 42. Use -= to subtract 3 from a variable price. 

# Solution:

# Price = 10
# Price -= 3
# print(Price)
# print(".................")


# 43. Multiply a variable balanceby2 using the *= operator.

# Solution:

# Price = 10
# Price *= 2
# print(Price)
# print(".................")


# 44. Divide a variable total by 4 using the /= operator.

# Solution:

# Price = 10
# Price /=4
# print(Price)
# print(".................") 


# 45. Use **= to square a variable.

# Solution:

# Price = 10
# Price **=2
# print(Price)
# print(".................")


# 46. Create a counter variable and increment it by 1 using assignment operators. 

# Solution: 

# counter = 10
# counter += 1
# print(counter)
# print(".................")


# 47. Use %= to find the remainder of a variable divided by 2 and update the variable.

# Solution: 

# counter = 11
# counter %= 2
# print(counter)
# print(".................")


# 48. Use //= to perform floor division on a variable and update it.

# Solution:

# counter = 11
# counter //= 2
# print(counter)
# print(".................")


# 49. Start with n = 2. In three lines of code using assignment operators, turn it into 20.

# Solution:

# n = 2
# n *= 5
# n += 15
# n -= 5
# print(n)
# print(".................")


# 50. Ask the user for a number, then use += to add 10 to it and print the final result. 

# Solution:

# user = int(input("Enter the Number:"))
# user += 10
# print(user)
# print(".................")
