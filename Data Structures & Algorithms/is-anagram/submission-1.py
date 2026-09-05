class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        seen = defaultdict(int)

        for i in range(len(s)):
            seen[s[i]] += 1
            seen[t[i]]-=1
        
        for k in list(seen.values()):
            if k:
                return False
        return True
