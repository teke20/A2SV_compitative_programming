class Solution:
    def smallerNumbersThanCurrent(self, nums):
        n= len(nums)
        out = []
        count=0
        for i in nums:
            for j in range(n):
               if (nums[j]-i)<0:
                   count+=1
            out.append(count)
            count=0
        return out
   
