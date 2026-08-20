#If i have a number 7568 and i want to print it from reverse how should i do it

n = 7568 #input given

num = n
while(num > 0):
    last_digit = num % 10
    print("Last digit :", last_digit)
    num = num//10

# So how the loop works
# n = 7568 it first gives the remainder of the number and then does the floor division for the next number
# 1. last_digit = 7568 % 10 = 8 ; num = 7568 // 10 = 756
# 2. last_digit = 756 % 10 = 6 ; num = 756 // 10 = 75
# 3. last_digit = 75 % 10 = 5 ; num = 75 // 10 = 7
# 4. last_digit = 7 % 10 = 7 ; num = 7 // 10 = 0
# 5. last_digit = 0 % 10 = 0 ; num = 0 // 10 = 0