class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s_sorted = sorted(s.lower())
            t_sorted = sorted(t.lower())
            if s_sorted == t_sorted:
                return True
        return False
