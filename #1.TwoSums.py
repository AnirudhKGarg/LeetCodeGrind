#1 two sum
class Solution(object):
    def twoSum(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in dict:
                return dict[complement], i
            dict[nums[i]]=i
        
