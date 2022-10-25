> Problem: [5. 最长回文子串](https://leetcode.cn/problems/longest-palindromic-substring/description/)

# Code1 中心扩散法

将字符串每个元素作为 pivot，向两边扩散，区分奇数和偶数

时间复杂度, $O(n^2)$
空间复杂度, $O(1)$

击败 76.46%

```Python []

class Solution(object):
    def expand(self,s,left,right):
        while (left>=0 and right<len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return left + 1 , right - 1
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        start = 0
        end = 0
        for i in range(len(s)):
            l1,r1 = self.expand(s,i,i)
            l2,r2 = self.expand(s,i,i+1)
            if r1-l1 > end-start:
                start = l1
                end = r1
            if r2-l2 > end - start:
                start = l2
                end = r2
        return s[start:end+1]

```

# Code2 动态规划法

仍然需要枚举。。时间复杂度，空间复杂度都很高

时间复杂度, $O(n^2)$
空间复杂度, $O(n^2)$

击败 76.46%

```Python []
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s

        max_len = 1
        begin = 0
        # dp[i][j] 表示 s[i..j] 是否是回文串
        dp = [[False] * n for _ in range(n)]
        for i in range(n):
            dp[i][i] = True

        # 递推开始
        # 先枚举子串长度
        for L in range(2, n + 1):
            # 枚举左边界，左边界的上限设置可以宽松一些
            for i in range(n):
                # 由 L 和 i 可以确定右边界，即 j - i + 1 = L 得
                j = L + i - 1
                # 如果右边界越界，就可以退出当前循环
                if j >= n:
                    break

                if s[i] != s[j]:
                    dp[i][j] = False
                else:
                    if j - i < 3:
                        dp[i][j] = True
                    else:
                        dp[i][j] = dp[i + 1][j - 1]

                # 只要 dp[i][L] == true 成立，就表示子串 s[i..L] 是回文，此时记录回文长度和起始位置
                if dp[i][j] and j - i + 1 > max_len:
                    max_len = j - i + 1
                    begin = i
        return s[begin:begin + max_len]
```
