nums = [5,1,2,3,4]
n = len(nums)
for i in range (0 , n-1):
    if(nums[i] > nums[i + 1]):
        print(False)
        break
else:
    print(True)