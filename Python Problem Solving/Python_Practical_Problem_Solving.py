# Question 1:
# Write a program that converts a temperature from Celsius to Fahrenheit. The formula to convert Celsius to Fahrenheit. 
# F = (C * 9/5) + 32.

# Solution:

Celsius = float(input("Enter the temperature in celsius:"))
Fahrenheit = (Celsius*9/5)+32
print("Temperature in Fahrenheit:",Fahrenheit,"f")
print("       .....................")


# Question 2:
# Calculate Area of a Rectangle

# Solution:

A = float(input("Enter the length of the rectangle:"))
B = float(input("Enter the width of the rectangle :"))
C = (A*B)
print("Area of a Rectangle:",C)
print("       .....................")


# Question 3:
# Calculate Compound Interest
# CI = P*(1+R/100)**T-P
# P = principal
# R = rate 
# T = time

# Solution:

P = float(input("Enter the value of principal(P):"))
R = float(input("Enter the value of rate(R)     :"))
T = float(input("Enter the value of time(T)     :"))
CI = P*(1+R/100)**T-P
print("Compound Interest:",CI)
print("       .....................")


# Question 4:
# Calculate  the Perimeter
# Perimeter = 2*(Length + Width)

# Solution:

Length = float(input("Enter the length of the rectangle:"))
Width  = float(input("Enter the width of the rectengle :"))
Perimeter = 2*(Length + Width)
print("Perimeter:",Perimeter)
print("       .....................")


# Question 5:
# Average of three numbers

# solution:

A = float(input("Enter the first number :"))
B = float(input("Enter the second number:"))
C = float(input("Enter the third number :"))
D = (A+B+C)/3
print("Average of Three Numbers:",D)
print("       .....................")


# Question 6:
# square and cube of a Number

# Solution:

Number = float(input("Enter the Number:"))
squareroot = Number*Number
print("The Square of a Number:",squareroot)
cube = Number*Number*Number
print("The Cube of a Number  :",cube)
print("       .....................")


# Question 7:
# Distribute Candles to each students 
# Candles left

# Solution:

n = int(input("Number of Candles :"))
k = int(input("Number of Students:"))
print("Candles each student gets:",n//k)
print("Remaining Candles:",n%k)
print("       .....................")


# Question 8:
# Calculate profit and loss

# solution:

cost_price = float(input("Cost Price   :"))
sell_price = float(input("Selling Price:"))
if sell_price>cost_price:
  print("Profit Amount:",sell_price-cost_price)
elif sell_price<cost_price:
    print("Loss Amount  :",cost_price-sell_price)
elif sell_price==cost_price:
    print("NO Profit NO Loss")
print("       .....................")


# Question 9:
# Total Marks
# Percentage
# Average

# Solution:

English1 = int(input("Obtained Marks in English         :"))
if 50>=English1>-1:
   English = English1
else:
    print("Invalid Input")
Computer1 = int(input("Obtained Marks in Computer        :")) 
if 50>=Computer1>-1:
    Computer = Computer1
else:
    print("Invalid Input") 
Machine_Learning1= int(input("Obtained Marks in Machine_Learning:")) 
if 50>=Machine_Learning1>-1:
    Machine_Learning = Machine_Learning1
else:
    print("Invalid Input") 
Generative_AI1= int(input("Obtained Marks in GenerativeAI    :")) 
if 50>=Generative_AI1>-1:
    Generative_AI = Generative_AI1
else:
    print("Invalid Input") 
Deep_Learning1= int(input("Obtained Marks in Deep_Learning   :")) 
if 50>=Deep_Learning1>-1:
    Deep_Learning = Deep_Learning1
else:
    print("Invalid Input")


TOTAL_Obtained_MARKS = English+Computer+Machine_Learning+Generative_AI+Deep_Learning
print("Total Obtained Marks:",TOTAL_Obtained_MARKS)

Total_Marks = 250
print("Total Marks         :",Total_Marks)

Percentage1 = (TOTAL_Obtained_MARKS/Total_Marks)*100
print("Percentage:",Percentage1)

Average1 =  (English+Computer+Machine_Learning+Generative_AI+Deep_Learning)/5
print("Average   :",Average1)
print("       .....................")


# Question 10:
# Total Salary

# Solution:
Basic_Salary = int(input("Enter Basic Salary:"))
DA= (Basic_Salary*15)/100
HRA=(Basic_Salary *25)/100
Total_Salary = int(Basic_Salary+DA+HRA)
print("TOTAL SALARY:",Total_Salary)


# Question 11:
# age input in years and convert it into months
# age input in years and convert it into days

# Solution:

Age = int(input("Enter your age in years:"))
AGE_IN_MONTHS = Age*12
print("Age in Months:",AGE_IN_MONTHS)

AGE_IN_DAYS =   Age*365
print("Age in Days  :",AGE_IN_DAYS)
print("        .....................")


# Questiion 12:
# (USD TO PKR)

# Solution:

USD = int(input("Enter Number of Dollars:"))
PKR = USD*277.83
print("PKR                    :",PKR)
print("         .....................")


# Question 13:
# Sum of n and find value of N

# Solution:

n = float(input("Enter Number of n:"))
sum = n*(n+1)/2
print("Sum of N:",sum)
print("          .....................")


# Question 14:
# Percentage of Correct Answer

# Solution:

question = int(input("Total Questions:"))
answer   = int(input("Correct Answers:"))
percentage_score = answer/question*100
print("Percentage_Score:",percentage_score)
print("           .....................")


# Question 15:
# Calculate Speed

# Solution:

D = float(input("Enter Distance covered:"))
T = float(input("Enter Time taken      :"))

S = D/T
print("Speed of object:",S)
print("            .....................")


# Question 16:
# Calculate BMI

# Solution:

weight = float(input("Enter weight in KG    :"))
height = float(input("Enter Height in Meters:"))


BMI = weight/(height**2)
print("BMI:",BMI)
print("            .....................")


# Question 17
# Convert Minutes to Hours

# Solution:

Minutes = int(input("Enter Minutes:"))
Hours   = Minutes//60
Remaining_Minutes = Minutes%60
print("Hours            :",Hours)
print("Remaining Minutes:",Remaining_Minutes)
print("            .....................")