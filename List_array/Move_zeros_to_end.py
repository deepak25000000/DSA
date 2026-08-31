nums = [0, 3, 7, 5, 0, 0, 9, 4, 0, 2]
n = len(nums)

if len(nums) == 1:
    print(nums)

# Step 1: Find the index of the first zero
i = 0
while i < len(nums):
    if nums[i] == 0:
        break
    i += 1

# Step 2: If a zero was found, swap non-zero elements
if i < len(nums):
    j = i + 1
    while(j < len(nums)):
        if nums[j] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

print(nums)
