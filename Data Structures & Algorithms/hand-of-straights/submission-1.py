class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        dct = {}
        hand.sort()
        for card in hand:
            dct[card] = dct[card] + 1 if card in dct else 1
        
        for _ in range(len(hand) // groupSize):
            smallest = list(dct.keys())[0]
            for i in range(groupSize):
                if smallest+i not in dct:
                    return False
                dct[smallest+i] -= 1

                if dct[smallest+i] == 0:
                    del dct[smallest+i]
        
        return True
            
        
