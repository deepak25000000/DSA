nums = [1, 1, 2 ,2 ,3 ,3 ,4 ,4 ,5 ,8 ,7 ,6 ,5]
n = len(nums)
if n==1:
    print(1)
   
i = 0
j = i + 1
unq = 0
while (j < n):
    if nums[j] != nums[i]:
        i += 1
        nums[i], nums[j] = nums[j], nums[i]
    j += 1
unq = i
print(unq)
    

    