#Count number of digits in an integer
#this appraoch used floor division and remainder

num = int(input("Enter a number: "))
count = 0
while(num > 0):
    num = num//10
    count = count + 1
    print(count)

#time complexity for the above is = O(log10(N))

#Second appraoch is using math library 

from math import *
num2 = int(input("Enter a number: "))
def count2(num2):
    return int(log10(num2)+1)
print("Number of digits :", count2(num2))
