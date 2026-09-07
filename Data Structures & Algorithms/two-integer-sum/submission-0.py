class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        inv = {}
        for i, n in enumerate(nums):
            if target - n in inv:
                return [inv.get(target - n), i]

            inv[n] = i

        return []
        