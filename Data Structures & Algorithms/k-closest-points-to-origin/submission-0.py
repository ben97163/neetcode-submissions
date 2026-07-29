class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for point in points:
            dist = point[0] ** 2 + point[1] ** 2
            heapq.heappush(minheap, (dist, point))
        
        ans = []
        for i in range(k):
            ans.append(heapq.heappop(minheap)[1])
        
        return ans