class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set()

        for n in nums:
            unique.add(n)

        res = 0
        for n in nums:
            if n + 1 in unique:
                continue

            m = n
            length = 0
            while m in unique:
                length += 1
                m -= 1
            res = max(res, length)

        return res
