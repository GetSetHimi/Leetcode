class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None

        for num in nums:
            # Agar count 0 ho gaya, toh naya candidate chuno
            if count == 0:
                candidate = num
            
            # Agar current number candidate ke barabar hai toh vote badhao, nahi toh ghatao
            if num == candidate:
                count += 1
            else:
                count -= 1
                
        return candidate