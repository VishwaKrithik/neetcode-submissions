class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        count = Counter(hand)
        
        for c in sorted(count):
            if count[c] == 0:
                continue
            
            freq = count[c]

            for i in range(groupSize):
                num = c + i
                if count[num] < freq:
                    return False

                count[num] -= freq
        
        return True
