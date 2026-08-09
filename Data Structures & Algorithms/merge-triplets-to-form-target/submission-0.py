class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        cleanTriplets = []
        for triplet in triplets:
            delete = False
            for i, element in enumerate(triplet):
                if element > target[i]:
                    delete = True
                    break
            if not delete:
                cleanTriplets.append(triplet)
        
        for i, t in enumerate(target):
            found = False
            for triplet in cleanTriplets:
                if triplet[i] == t:
                    found = True
                    break
            
            if not found:
                return False
        
        return True