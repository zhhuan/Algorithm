class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        returnlist=[]
        for element in set(nums):
            if nums.count(element) > len(nums)/3 :
                returnlist.append(element)
        return returnlist
        
