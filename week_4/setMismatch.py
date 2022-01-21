class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        :type nums: List[int]
        :rtype: List[int]
        """ 
        lookup = Counter(nums)
        N = len(nums)
        for i in range(1,N+1):
            if i not in lookup:
                mis = i
            elif lookup[i]>1:
                rep = i
                
        return [rep,mis]
