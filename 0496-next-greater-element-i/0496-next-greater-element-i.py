class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # Map store karega: {element: uska_next_greater_element}
        next_greater_map = {}
        stack = []
        
        # nums2 ko right se left (piche se) traverse karenge
        for num in reversed(nums2):
            # Jab tak stack ke top par chhota element hai, use hatao
            while stack and stack[-1] <= num:
                stack.pop()
            
            # Agar stack khali nahi hai, toh top element hi next greater hai
            if stack:
                next_greater_map[num] = stack[-1]
            else:
                next_greater_map[num] = -1
                
            # Current element ko stack mein push karo
            stack.append(num)
            
        # nums1 ke har element ke liye map se answer nikal lo
        ans = [next_greater_map[num] for num in nums1]
        
        return ans