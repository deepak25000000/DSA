n = int(input("Enter a number: "))
total = 0
num = n
nod = len(str(n))
while (num > 0):
    ld = num % 10
    total = total + (ld ** nod)
    num = num //10
    
if (total == n):
        print("ARMSTRONG NUMBER") 
else:
      print('Not a armstrong number')


