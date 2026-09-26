import random

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        left, right = 0, len(nums) - 1
        target = len(nums) - k

        while left <= right:
            pivot_idx = random.randint(left, right)
            pivot = nums[pivot_idx]

            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]

            store = left
            for r in range(left, right):
                if nums[r] < pivot:
                    nums[store], nums[r] = nums[r], nums[store]
                    store += 1

            nums[right], nums[store] = nums[store], nums[right]

            if store == target:
                return nums[target]
            elif store < target:
                left = store + 1
            else:
                right = store - 1
            

