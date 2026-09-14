class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        SIZE = len(nums)
        res = [1] * SIZE

        prefix = 1
        for i in range(SIZE):
            res[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for j in range(SIZE - 1, -1, -1):
            res[j] *= suffix
            suffix *= nums[j]

        return res