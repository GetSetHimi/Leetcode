class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # If lengths aren't equal, they can't be anagrams
        if len(s) != len(t):
            return False
            
        return sorted(s) == sorted(t)