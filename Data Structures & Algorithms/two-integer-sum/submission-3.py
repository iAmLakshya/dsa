class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = {}

        for i, n in enumerate(nums):
            idx[n] = i

        for i, n in enumerate(nums):
            if target - n in idx and idx[target - n] != i:
                return sorted([i, idx[target - n]])
