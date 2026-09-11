class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        buckets = [set() for _ in range(len(nums))] #[{1},{2},{3},{},{},{}]

        for n in nums: #[1,2,2,3,3,3] freq={1:1,2:2,3:3}
            if not n in freq:   
                freq[n] = 1
                buckets[0].add(n)
            else:
                buckets[freq[n] - 1].remove(n)
                freq[n] += 1
                buckets[freq[n] - 1].add(n)

        res = []
        j = len(nums) - 1   # 5
        for _ in range(k, 0, -1):  # 2
            while len(buckets[j]) == 0:
                j -= 1

            res.append(buckets[j].pop())

        return res


        # quickselect: map<n, freq> -> map<freq, n> + freq quick select O(n) + O(n) + O(n) = O(n)
        # heap: map<n, freq> (object) + heap (nlogk) = O(n) + O(nlogk)
