class Solution:
    def insetion_sort(self, nums):
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            while (j>=0 and nums[j]>key):
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key
        return nums

solution = Solution()
nums = [12,11,13,5,6]
print(solution.insetion_sort(nums))
'''
https://www.geeksforgeeks.org/problems/insertion-sort/1
TC = O(n^2)
SC = O(1)
'''