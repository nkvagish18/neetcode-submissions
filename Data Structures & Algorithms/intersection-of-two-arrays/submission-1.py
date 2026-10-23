class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        list1 = set(nums1)
        res = set()
        for i in nums2:
            if i in list1:
                res.add(i)
        return list(res)