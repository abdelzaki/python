"""Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
return the k closest points to the origin (0, 0)"""
from cmath import sqrt
from collections import defaultdict,OrderedDict



class Solution:
    def kClosest(points: list[list[int]], k: int) -> list[list[int]]:
        distancedict = defaultdict(list)
        result = list()
        numberOfElements = 0
        for point in points:
            distance = (sqrt((point[0]*point[0]) + (point[1] * point[1]))).real
            distancedict[distance].append(point)
        od = sorted(distancedict.keys())
        for key in od:
            for point in distancedict[key]:
                if numberOfElements < k:
                    result.append(point)
                    numberOfElements += 1
                else:
                    return result
        return result

points = [[1,0],[0,1]]
k = 2
print(Solution.kClosest(points, k))