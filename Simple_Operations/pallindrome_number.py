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
        
