nums = [1,5,6,7,8,10, 11,234]
#Using slicig method TC = O(n)
n = len(nums)
nums = nums[-1:] + nums[0: n - 1]
print(nums)

#Using temp varibale method TC = O(n)
temp = nums[n -1]
for i in range (n-2, -1, -1):
    nums[i + 1] = nums[i]
nums[0] = temp
print(nums)