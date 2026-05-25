class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea = 0
        if len(heights) <=1:
            return 0

        for i in range(len(heights)):
            j = len(heights)-1
            while j > i:
                width = j-i
                minHeight = min(heights[j], heights[i])
                if minHeight*width > maxArea:
                    maxArea = minHeight*width
                j-=1
        return maxArea