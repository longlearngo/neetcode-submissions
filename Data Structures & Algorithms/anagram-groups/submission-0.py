class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ALPHABET = 26
        anagram = {}

        for s in strs:
            freq = [0] * ALPHABET
            for ch in s:
                freq[ord(ch) - ord('a')] += 1
            
            key = tuple(freq)
            val = anagram.get(key, [])
            val.append(s)
            anagram[key] = val

        return list(anagram.values())

        
            
