#7 reverse integers
class Solution(object):
    def reverse(self, x):
        self.x = x
        if x >= 0:
            x = [int(i) for i in str(x)]
            x = x[::-1]
            x = int("".join([str(i) for i in x]))
        else:
            x = abs(x)
            x = [int(i) for i in str(x)]
            x = x[::-1]
            x = int("".join([str(i) for i in x]))
            x = -1 * x
        
        if x > 2147483647 or x < -2147483648:
            x = 0
        return x
        
reverse(x)
