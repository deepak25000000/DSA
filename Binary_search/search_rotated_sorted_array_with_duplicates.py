class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        n = len(nums)
        low = 0
        high = n - 1
        while low<=high:
            mid = (low+high)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[low]==nums[high]:
                low = low + 1
                high = high - 1
                continue
            if nums[mid]<=nums[high]:
                if nums[mid]<= target <= nums[high]:
                    low = mid + 1     
                else:
                    high = mid - 1
            else:
                if nums[low]<= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

        return False
solution = Solution()
nums = [2,5,6,0,0,1,2]
target = 0
print(solution.search(nums, target))

'''https://leetcode.com/problems/search-in-rotated-sorted-array-ii/?source=submission-noac
TC = O(N) best and worst case
TC = O(logN) in best case
SC = O(1)

'''