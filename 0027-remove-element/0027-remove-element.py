class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        
        for i in range(len(nums)):
            # Agar current element val ke barabar nahi hai
            if nums[i] != val:
                # Toh use k-th position par rakh do
                nums[k] = nums[i]
                # Aur k ko agli position par move kar do
                k += 1
                
        # k hi bache huye elements ka sahi count hoga
        return k