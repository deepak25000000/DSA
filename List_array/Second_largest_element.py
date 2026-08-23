# second largest element
#Using Brtue Force method 
#Due to sorting the TC= O(n log n)
#Due to indexing the SC= O(1)
num = [23, 45, 786, 326, 567, 30]
num.sort()
print(num)
print("SECOND LARGEST NUMBER: ", num[-2])

#Using The best optimal solution without sorting 

nums = list(map(int, input("Enter numbers for the list: ").split(',')))
n = len(nums)
largest = float('-inf')
second_largest = float('-inf')
for i in range (0, n):
    if (nums[i] > largest):
        second_largest = largest
        largest = nums[i]
    elif (nums[i] > second_largest and nums[i] != largest):
            second_largest = nums[i]
print("Second_largest:", second_largest)


#how the loops works for the [23, 30, 45, 326, 567, 786]
#assign both the largest and the second largest the float negative infinty value 
#it checks like 23 is the second largest for now then it will keep it as s_l then it will go for 
#30 30 > 23 which is true then it will keep it as s_l then it will go for 
#45 45 > 30 which is true then it will keep it as s_l then it will go for 
#326 326 > 45 which is true then it will keep it as s_l then it will go for 
#567 567 > 326 which is true then it will keep it as s_l then it will go for 
#786 786 > 567 which is true then it will keep it as s_l then it will go for  #loops stops
# same with all negative array integers input 