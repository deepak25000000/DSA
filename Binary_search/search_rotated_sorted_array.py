class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1
        while low<=high:
            mid = (high+low)//2
            if nums[mid]==target:
                return mid
            if nums[mid] <= nums[high]:
                 if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                 else:
                    high = mid - 1
            else:
                 if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                 else:
                    low = mid + 1
        return -1

solution = Solution()
nums = [4,5,6,7,0,1,2]
target = 0
print(solution.search(nums, target))


'''
https://leetcode.com/problems/search-in-rotated-sorted-array/

brute force solution:
for i in range (0, n):
    if nums[i] == target:
        return i
    return -1
    TC for Brute force  is O(N)
    SC for Brute force is O(1)

TC = O(logN) for optimal solution 
SC = O(1) for optimal solution
'''

        

            
            
           
            
        