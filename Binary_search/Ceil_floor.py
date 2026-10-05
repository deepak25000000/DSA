nums = [1, 4, 5, 6,7,7,8,19,20,20,34,43]
n = len(nums)
target = 13
low = 0
high = n - 1
floor = -1
ceil = -1

while low<=high:
    mid = (low+high)//2
    if nums[mid] == target:
        print(mid)
        print(nums[mid], nums[mid])
    elif nums[mid] > target:
        ceil = nums[mid]
        high = mid - 1
    else:
        floor = nums[mid]
        low = mid + 1
print(floor, ceil)
#TC = O(logn)
#SC = O(1)

