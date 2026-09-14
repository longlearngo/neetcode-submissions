class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        SIZE = len(nums)
        pre_product = [1] * SIZE
        post_product = [1] * SIZE

        for i in range(1, SIZE):
            pre_product[i] = pre_product[i - 1] * nums[i - 1]

        for j in range(SIZE - 2, -1, -1):
            post_product[j] = post_product[j + 1] * nums[j + 1]

        res = []
        for i in range(SIZE):
            res.append(pre_product[i] * post_product[i])

        return res