class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {}
        for c in s:
            count[c] = count[c] + 1 if c in count else 1
        
        for c in t:
            if not c in count:
                return False
            count[c] -= 1
            
            if count[c] == 0:
                del count[c]

        return len(count) == 0