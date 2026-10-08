class Solution():
    def findmini(self, nums:list[int], targte:int) -> int:
        n = len(nums)
        high =  n - 1
        low = 0
        minimum = float("inf")
        while low<=high:
            mid = (low+high)//2
            if nums[low]<=nums[mid]:
                minimum = min(minimum, nums[low])
                low = mid + 1
            else:
                minimum = min(minimum, nums[mid])
                high = mid -1
        return minimum

solution = Solution()
nums =  [0,4,6,1,3]
target = 0
print(solution.findmini(nums, target))

'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
TC = O(logN)
SC = O(1)
'''
