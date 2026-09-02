'''
Leetcode 485 question MAX CONSECUTIVE ONEs
Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 
'''

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

# T.C =O(n)
# S.C = O(1)