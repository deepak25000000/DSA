nums = [1, 1,1,1,0,0,1,0,1,1,0,1,1,1,0,1,1,1,1,1,1,0,1,1,1]
max_count = 0
count = 0
n = len(nums)
for i in range(0, n):
    if(nums[i] == 1):
        count += 1
    else:
        max_count = max(max_count, count)
        count = 0
max_count = max(max_count, count)
print(max_count)