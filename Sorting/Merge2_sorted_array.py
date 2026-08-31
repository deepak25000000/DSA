nums1 = [1, 2,4,5,8]
nums2 = [1,2,3,5, 6, 7,9]
n = len(nums1)
m = len(nums2)
result = []
i = j = 0

while (i<n and j<m): #this loop runs until either i exhausted or j gets exhausted
    if(nums1[i] <= nums2[j]):
        if(len(result) == 0 or result[-1] != nums1[i]):
            result.append(nums1[i])
        i +=1 
    else:
        if(len(result) ==0 or result[-1] != nums2[j]):
            result.append(nums2[j])
        j += 1

while(i<n): #this loop if j gets exhausted first
    if(len(result) == 0 or result[-1] != nums1[i]):
        result.append(nums1[i])
    i +=1
while(j<m): #this loop if i gets exhausted first
    if(len(result) ==0 or result[-1] != nums2[j]):
        result.append(nums2[j])
    j += 1
print(result)

   

