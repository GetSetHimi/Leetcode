class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """ 
        max_from_right = -1

        for i in range(len(arr) - 1, -1, -1):

            current_val = arr[i]
            arr[i] = max_from_right
            
            if current_val > max_from_right:
                max_from_right = current_val
                
        return arr