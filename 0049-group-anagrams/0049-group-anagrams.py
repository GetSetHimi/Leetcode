class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = {}
        
        # Array ke har ek string par loop chalayein
        for s in strs:
            # String ke characters ko sort karein taaki anagrams ki pehchan ho sake
            # sorted(s) hume characters ki list dega, 'join' use karke use wapas string banayein
            sorted_s = "".join(sorted(s))
            
            # Agar yeh sorted string pehle se map mein nahi hai, toh ek khali list banayein
            if sorted_s not in anagram_map:
                anagram_map[sorted_s] = []
            
            # Asli string (s) ko uske sorted_s waali list mein append (add) kar dein
            anagram_map[sorted_s].append(s)
            
        # Dictionary ki saari values (jo ki lists hain) ko ek badi list mein return karein
        return list(anagram_map.values())