class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dct = Counter(tasks)
        maxHeap = []
        for v in dct.values():
            heapq.heappush(maxHeap, -v)
        print(maxHeap)
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                val = heapq.heappop(maxHeap)
                if val + 1 < 0:
                    queue.append((val + 1, time + n))
            if queue:
                while queue[0][1] == time:
                    heapq.heappush(maxHeap, queue.popleft()[0])
                    if not queue:
                        break
        

        return time
        