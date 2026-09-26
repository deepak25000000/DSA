class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        n  = len(nums)
        my_set = set()
        for i in range(0,n):
            my_set.add(nums[i])
        longest = 0
        for nums in my_set:
            if nums-1 not in my_set:
                x = nums
                count = 1
            while x+1 in my_set:
                count += 1
                x += 1
                longest = max(longest, count)
        return longest

sol = Solution()
print(sol.longestConsecutive([100, 4, 200, 1, 3, 2])) #Output: 4

# Tc = O(n)
# Sc = O(n)
'''
https://leetcode.com/problems/longest-consecutive-sequence/ 

'''