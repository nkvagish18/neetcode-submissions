class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch,0) + 1
        length = 0
        odd_found = False
        for value in freq.values():
            length += (value // 2) * 2
            if value % 2 == 1:
                odd_found = True
        if odd_found:
            length += 1
        return length