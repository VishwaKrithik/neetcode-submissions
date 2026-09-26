import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        left, right = 0, len(nums) - 1
        target = len(nums) - k

        while left <= right:
            pivot = nums[random.randint(left, right)]

            lt, i, gt = left, left, right

            while i <= gt:
                if nums[i] < pivot:
                    nums[lt], nums[i] = nums[i], nums[lt]
                    i += 1
                    lt += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1

            if lt <= target <= gt:
                return nums[target]
            elif target > gt:
                left = gt + 1
            else:
                right = lt - 1
            

