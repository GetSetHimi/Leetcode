class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        lgth = 0
        i = len(s)-1

        while i >= 0 and s[i] != ' ':
            lgth +=1
            i -=1
        
        return lgth
        