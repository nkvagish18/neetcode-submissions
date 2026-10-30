class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        if x < 0:
            sign = -1
        else:
            sign = 1
        x = abs(x)
        while x:
            lastDig = x % 10
            rev = rev*10 + lastDig
            x = x // 10
        rev *= sign
        if rev < -2**31 or rev > 2**31:
            return 0
        return rev