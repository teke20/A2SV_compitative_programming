class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        h1 = sorted(heights)
        sum1 = 0
        for i in range (len(heights)):
            if h1[i]!=heights[i]:
                sum1 += 1
        return sum1
