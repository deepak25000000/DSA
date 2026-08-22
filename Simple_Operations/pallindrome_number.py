n = int(input("Enter a number: "))
num = n
result = 0
while(num > 0):
    last_digit = num % 10
    result = (result * 10) + last_digit
    num = num//10
if (n == result):
    print("Pallindrome")
else:
    print("Not a Pallindrome")
#how the loop works for 123
#last_digit = 123 % 10 = 3
#result = (0 * 10) + 3 = 3
#num = 123 // 10 = 12

#last_digit = 12 % 10 = 2
#result = (3 * 10) + 2 = 32
#num = 12 // 10 = 1

#last_digit = 1 % 10 = 1
#result = (32 * 10) + 1 = 321
#num = 1 // 10 = 0