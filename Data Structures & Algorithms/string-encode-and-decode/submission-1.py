class Solution:
    def __init__(self):
        self.lens = []

    def encode(self, strs: List[str]) -> str:
        for s in strs:
            self.lens.append(len(s))
        return "".join(strs)

    def decode(self, s: str) -> List[str]:
        string_builder = []
        res = []
        i = 0
        for l in self.lens:
            for _ in range(l):
                string_builder.append(s[i])
                i += 1
            res.append("".join(string_builder))
            string_builder = []
        return res