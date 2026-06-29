class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :type rtype: bool
        """
        # Agar length hi alag hai, toh isomorphic ho hi nahi sakte
        if len(s) != len(t):
            return False
            
        map_s = {}
        map_t = {}
        
        for char_s, char_t in zip(s, t):
            # Case 1: Agar s ka char pehle se mapped hai, par kisi aur se mapped hai
            if char_s in map_s and map_s[char_s] != char_t:
                return False
                
            # Case 2: Agar t ka char pehle se mapped hai, par kisi aur se mapped hai
            if char_t in map_t and map_t[char_t] != char_s:
                return False
                
            # Nayi mapping ko store karein
            map_s[char_s] = char_t
            map_t[char_t] = char_s
            
        return True