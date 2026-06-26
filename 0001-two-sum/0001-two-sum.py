class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}  # Dictionary to store: {number: index}

        for i, num in enumerate(nums):
            partner = target - num
            
            # Agar partner dictionary me mil jata hai
            if partner in seen:
                return [seen[partner], i]
            
            # Agar nahi milta, toh current number aur uske index ko save kar lo
            seen[num] = i