class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        for j in points:
            for i in range(0,len(points)-1):
                a, c = pow(points[i][0], 2) , pow(points[i+1][0], 2)
                b, d= pow(points[i][1], 2), pow(points[i+1][1], 2)
                if sqrt(a + b) < sqrt(c + d):
                    points[i], points[i+1] = points[i+1], points[i]
        return points[-k:]
        
