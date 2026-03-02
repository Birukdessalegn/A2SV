class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = []
        for point in points:
            x.append(point[0])
        x.sort()
        max_width = 0
        n = len(x)
        for i in range(1 , n):
            diff = x[i] - x[i-1]
            if diff > max_width:
               max_width = diff
        return max_width
        