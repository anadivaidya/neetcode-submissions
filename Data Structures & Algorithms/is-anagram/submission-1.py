from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        if(set(s) != set(t)):
            return False
        if(Counter(t) != Counter(s)):
            return False
        return True