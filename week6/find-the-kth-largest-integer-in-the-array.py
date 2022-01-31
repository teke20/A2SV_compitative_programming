class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        res = []
        for i in range(len(nums)):
            res.append(int(nums[i]))
        res.sort()
        ans = res[-k]
        return "%s" %(ans)
