class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        output = []
        n = len(intervals)
        for i in range(n):
            for j in range(n-i-1):
                if intervals[j][0] > intervals[j+1][0]:
                    intervals[j], intervals[j+1] = intervals[j+1], intervals[j]
        output.append(intervals[0])
        for i in range(1, n):
            last = output[-1]

            # If overlapping
            if last[1] >= intervals[i][0]:
                last[1] = max(last[1], intervals[i][1])
            else:
                output.append(intervals[i])

        return output