class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        length = len(flowerbed)
        
        for i in range(length):
            # Agar n zero ya usse kam ho chuka hai, toh aage check karne ki zaroorat nahi
            if n <= 0:
                return True
                
            # Check karo ki current position khaali hai ya nahi
            if flowerbed[i] == 0:
                # Left check: Agar pehla element hai ya left mein 0 hai
                left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                
                # Right check: Agar aakhiri element hai ya right mein 0 hai
                right_empty = (i == length - 1) or (flowerbed[i + 1] == 0)
                
                # Agar dono taraf khaali hai, toh flower laga do
                if left_empty and right_empty:
                    flowerbed[i] = 1  # Flower plant kar diya
                    n -= 1            # Ek flower kam ho gaya
                    
        return n <= 0