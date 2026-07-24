class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        zipped_lists = sorted(zip(position, speed), reverse=True)

        # 2. 用 zip(*...) 將它們解開還原成兩個獨立的 tuple / list
        position_sorted, speed_sorted = map(list, zip(*zipped_lists))

        print(position_sorted, speed_sorted)

        time_needed = [((target - p) / s) for p,s in zip(position_sorted, speed_sorted)]
        count = 1
        max_time = time_needed[0]
        for i, time in enumerate(time_needed[1:]):
            if time > max_time:
                count += 1
                max_time = time
            
        return count