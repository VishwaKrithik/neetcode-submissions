class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        res = []

        for k in range(len(nums)):
            if nums[k] > 0:
                return res
            
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            

            left = k + 1
            right = len(nums) - 1

            while(left < right):
                Sum = nums[k]+nums[left]+ nums[right]
                if Sum == 0:
                    l = []
                    l.append(nums[k])
                    l.append(nums[left])
                    l.append(nums[right])
                    res.append(l)
                    while(left+1< len(nums) and nums[left] == nums[left+1]):
                        left+=1
                    left+=1
                    while(right > 0 and nums[right] == nums[right-1]):
                        right-=1
                    right-=1
                elif Sum< 0:
                    while(left+1< len(nums) and nums[left] == nums[left+1]):
                        left+=1
                    left+=1
                else:
                    while(right>0 and nums[right] == nums[right-1]):
                        right-=1
                    right-=1
        return res


