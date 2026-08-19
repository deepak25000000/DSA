# name = "John"
from decimal import ConversionSyntax
name = 'Deep'
print(name)

print("Hello World")


name2 = 'Thorat'
name3 = 'Birajdar'
print(name3) 

# Changing the values of varibale in python 
name3 = 'Ghorpade'
print(name3)

#  Assigning multiple values to multiple varriables
name , age , city = 'Thorat', 20, 'Pune'
print(name)
print(age)
print(city)

# Assigning same value to multiple varibales 
name = city = age = 'Deepak'
print(city) 
# Literals are the values assigned to the varible. For example - 'Deepak', 20, 'Pune' 

# Type Conversion
# Implicit Conversion 
#Python automatically converts one variable to another is said to be Implicit Conversion

num1 = 20
num2 = 20.78
num3 = num1 + num2 
print("Value of the number :", num3)
print(type(num3)) 

# It is because Python always converts smaller data types to larger data types to avoid the loss of data.


# Explicit Type Conversion 

str1 = '26'
num5 = 34.65
print("Data Type of str1 :" ,type(str1))

# Explicit ConversionSyntax
str1 = int(str1)
print("Data Type f str1:", type(str1))
add = str1 + num5
print(add, type(add))


# Input and output in python 
''' There are total 5 paramters used in print function
 end, object, sep, file, flush
 1. object - value(s) to be printed
2. sep (optional) - allows us to separate multiple objects inside print().
3. end (optional) - allows us to add add specific values like new line "\n", tab "\t"
4. file (optional) - where the values are printed. It's default value is sys.stdout (screen)
5. flush (optional) - boolean specifying if the output is flushed or buffered. Default: False
'''
print('GOODDAY', end=' ')
print('BAD')

# Seperator or sep
print("Good", "Bad", "Day", sep=' ! ')


#Random Variable
import random
print(random.randrange(10, 20))
list1 = [20, 30, 'a', 'deepak', 't']
print(random.choice(list1)) 

random.shuffle(list1)
print(list1)
print(random.random())



#We can impport math library to to carry out different mathematics like trigonometry, logarithms, probability and statistics, etc
import math 
print(math.pi)

print(math.exp(35.769))