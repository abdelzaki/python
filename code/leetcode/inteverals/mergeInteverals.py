"""
Given an array of intervals where intervals[i] = [starti, endi], 
merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
"""


class Solution:
    def merge(intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort()
        oldStart, oldStop = intervals[0]
        result = list()
        for i, element in enumerate(intervals[1:]):
            start, stop = element

            if start > oldStop :
                result.append((oldStart, oldStop ))
                oldStart, oldStop = element
            else:
                oldStart = min(oldStart, start)
                oldStop = max(oldStop, stop)
        result.append((oldStart, oldStop ))
        return result
    
    
intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals =  [[1,4],[0,0]]


print(Solution.merge(intervals))