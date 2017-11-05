class Solution:
    
    """
    http://www.lintcode.com/en/problem/subsets/
    @param: nums: A set of numbers
    @return: A list of lists
    """
    
    def findSubsets(self, nums, subset, startIndex):
        self.results.append(subset)
        i = startIndex
        while i <  len(nums):
            self.findSubsets(nums, subset + [nums[i]], i+1)
            i += 1
            
    def subsets(self, nums):
        # write your code here
        self.results = []
        self.findSubsets(sorted(nums), [], 0)
        return self.results
