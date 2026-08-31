nums = [1, 2,56, 7, 3,4]
target = 4
n = len(nums)
for i in range (0, n):
    if (nums[i] == target):
        print("Element is at index :", i)
        break
else:
    print("Element not in the array")