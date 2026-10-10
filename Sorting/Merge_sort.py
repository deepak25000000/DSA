class solution:
    def merge_array(self, left, right): #first we willl create a function for merging 2 sorted arrays 
        result =[]
        i = 0
        j = 0
        n = len(left)
        m = len(right)
        while (i < n and j < m): #this check the len and compare the elements of left and right arrays
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        if i < n: #this condition is used when j is exhuasted 
            while i<n:
                result.append(left[i])
                i += 1
        if j < m: #this condition is used when i is exausted
            while j<m:
                result.append(right[j])
                j += 1
        return result
    
    def merge_sort(self, nums):
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left_nums = nums[ : mid]
        right_nums = nums[mid : ]
        left =  self.merge_sort(left_nums)
        right = self.merge_sort(right_nums)
        return self.merge_array(left, right)
    
solution = solution()
nums = [1,5,6,2,4,8,9,23,5,1,2]
print(solution.merge_sort(nums))
print(len(nums))

#TC = O(NlogN)
#SC = O(N)
            
