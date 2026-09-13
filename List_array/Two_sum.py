nums = [10, 5, 4,6, 7, 8 ,10]
target = 20
n = len(nums)
for i in range(0, n-1):
    for j in range(i+1, n):
        if(nums[i]+nums[j] == target):
            print(i,j)
            break
        
            