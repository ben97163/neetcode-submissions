class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = [-stone for stone in stones]
        heapq.heapify(arr)
        while arr:
            if len(arr) == 1:
                return -arr[0]
            top, second = -heapq.heappop(arr), -heapq.heappop(arr)
            if top == second:
                continue
            heapq.heappush(arr, - (top - second))
        return 0

            

