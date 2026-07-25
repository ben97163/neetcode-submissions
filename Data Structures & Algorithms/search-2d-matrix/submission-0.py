class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l+r)//2
            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                ll, rr = 0, len(matrix[mid]) - 1
                while ll <= rr:
                    mm = (ll + rr) // 2
                    if matrix[mid][mm] == target:
                        return True
                    elif matrix[mid][mm] > target:
                        rr = mm - 1
                    else:
                        ll =  mm + 1
                
                return False
            
            elif matrix[mid][0] < target:
                l = mid + 1
            
            else:
                r = mid - 1
        
        return False
 