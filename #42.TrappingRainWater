#42 trapping rainwater
class Solution(object):
    def trap(self, height):
        max_left = [0] * (len(height) + 1)
        max_right = [0] * (len(height) + 1)
    
        for k, v in enumerate(height):
            max_left[k] = max(max_left[k-1], v)
            
        for k, v in reversed(list(enumerate(height))):
            max_right[k] = max(max_right[k+1], v)
     
        water = 0

        for k, v in enumerate(height):
            water += max(0, min(max_left[k], max_right[k]) - v)
    
        return water
