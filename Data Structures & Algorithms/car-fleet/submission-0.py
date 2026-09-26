class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        nums = [(position[i], speed[i]) for i in range(len(speed))]

        nums = sorted(nums, key=lambda x: x[0], reverse=True)

        timeStack = []

        for pos, speed in nums:
            time = (target - pos) / speed
            if timeStack and time <= timeStack[-1]:
                continue
            else:
                timeStack.append(time)
        
        return len(timeStack)
