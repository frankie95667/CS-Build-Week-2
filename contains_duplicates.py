class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        # sort list
        nums.sort()
        
        # iterate through list
        for i in range(len(nums) - 1):
            # if current and next index are the same
            if nums[i] == nums[i + 1]:
                # return true
                return True
        
        # return false
        return False