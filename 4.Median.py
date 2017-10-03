class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        nums = sorted(nums)
        if len(nums) %2 ==1:
            a=len(nums)-1
            return nums[int(a/2)]
        else:
            i = int(len(nums)/2)
            num = nums[i]+nums[i-1]
            return num/2
