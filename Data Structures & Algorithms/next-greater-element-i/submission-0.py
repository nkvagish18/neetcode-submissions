class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack =[]
        mp = {}
        for num in nums2:
            while stack and num > stack[-1]:
                x = stack.pop()
                mp[x] = num
            stack.append(num)
        ans = []
        for num in nums1:
            if num in mp:
                ans.append(mp[num])
            else:
                ans.append(-1)
        return ans