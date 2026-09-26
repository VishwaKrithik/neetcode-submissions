class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        # soln using only 2 vars

        nums = [(pos, spe) for pos, spe in zip(position, speed)]

        nums = sorted(nums, key=lambda x:x[0], reverse=True)

        count = 0
        prevMax = float("-inf")

        for pos, speed in nums:
            time = (target - pos) / speed

            if time <= prevMax:
                continue
            else:
                prevMax = time
                count += 1
        
        return count

        # Soln using full stack

        # nums = [(position[i], speed[i]) for i in range(len(speed))]

        # nums = sorted(nums, key=lambda x: x[0], reverse=True)

        # timeStack = []

        # for pos, speed in nums:
        #     time = (target - pos) / speed
        #     if timeStack and time <= timeStack[-1]:
        #         continue
        #     else:
        #         timeStack.append(time)
        
        # return len(timeStack)
