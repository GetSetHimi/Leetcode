class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        
        # Strings ko alphabetically sort karein
        strs.sort()
        # Sort karne ke baad pehla aur aakhri string nikalenge
        first = strs[0]
        last = strs[-1]

        ans = ""
        # Dono strings ke characters ko ek-ek karke compare karein
        # Hum dono me se jo choti string hogi, wahan tak hi loop chalayenge
        for i in range(min(len(first), len(last))):
            # Agar character match karta hai, toh use answer me add karo
            if first[i] == last[i]:
                ans += first[i]
            else:
                # Jahan mismatch mila, wahi ruk jao
                break
                
        return ans