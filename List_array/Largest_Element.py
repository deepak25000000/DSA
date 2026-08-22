#Largest element in array/list 
#time complexity O(n) and space O(1)

num_arr = list(map(int, input("Enter numbers for the list:").split(','))) #[35, 437, 231, -72, 0, 5]
largest = num_arr[0]
n = len(num_arr)

for i in range(0 , n):
    if (num_arr[i] > largest):
     largest = num_arr[i] #or we can use if else loop 
    #largest = max(largest, num_arr[i]) we can use here max fucntion 
print("Largest number :", largest)
