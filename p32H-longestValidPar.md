> Problem: [32. 最长有效括号](https://leetcode.cn/problems/longest-valid-parentheses/description/)

[TOC]

# 思路

> 自己想的双指针，做好久没做出来。最后参考的官方

> 官方的另外两种常用方法：动态规划和栈方法

# Code1 双指针法

利用两个计数器，从左往右计数，遇到左括号 l+1，遇到右括号 r
+1，当遇到右括号后，判断此时 l 与 r 的关系，如果 l==r 则说明此时匹配成功，结果应为（原先的结果，r\*2）中的最大值（这个地方没想出来），如果左口号多，则 continue，如果右括号多，则匹配失败，l 和 r 重新置为 0

这种方法在遇到`'(()'`时会失效，因此需要倒着在遍历一遍，并且求得到的最大值，因为从左往右的时候，l 一直大于 r，因此 res 不会发生变化，到了倒序时才会改变

- 时间复杂度: $O(n)$
- 空间复杂度: $O(1)$

```Python []

class Solution:
    def longestValidParentheses(self, s: str) -> int:


        res = 0
        if len(s)<=1:
            return 0
        i = 0
        l = 0
        r = 0
        while i<len(s):
            if s[i]== '(':
                l += 1
            elif s[i]== ')':
                r += 1

            if(l==r):
                res = max(res,2*r)
            elif(r > l):
                l = 0
                r = 0
            i+=1

        j = len(s)-1
        l = 0
        r = 0
        while j>=0:
            if s[j]== '(':
                l += 1
            elif s[j]== ')':
                r += 1

            if(l==r):
                res = max(res,2*l)
            elif(l>r):
                l = 0
                r = 0
            j-=1

        return res
```

# Code2 栈方法

遇到左括号就压入栈，遇到右括号且栈非空则弹出栈，将括号的 index 加入到 res 中去，
因为要求最长字串，最长子串的 index 肯定是项链的，因此对 res 进行排序，找到最长的连续数列中元素的个数即为结果

```Python []
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        res = []
        stack = []
        for i in range(len(s)):
            if stack and s[i] == ")":
                res.append(stack.pop())
                res.append(i)
            if s[i] == "(":
                stack.append(i)
        res.sort()
        i = 0
        ans = 0
        n = len(res)
        while i < n:
            j = i
            while j < n - 1 and res[j + 1] == res[j] + 1:
                j += 1
            ans = max(ans, j - i + 1)
            i = j + 1
        return ans
```

# Code3 动态规划

动态规划题目分析的 4 个步骤：

- 确定状态
  - 研究最优策略的最后一步
  - 化为子问题
- 转移方程
  - 根据子问题定义得到
- 初始条件和边界情况
- 计算顺序

定义一个 dp 数组，其中第 i 个元素表示以下标为 i 的字符结尾的最长有效字符串的长度

- `s[i]=='('`则该字符串必不可能有效，因此`dp[i]=0`
- `s[i]==')'`：分情况讨论
  - `s[i-1] = '('`:此时 s[i:i+2]组成有效括号，`dp[i] = dp[i-2]+2`
  - `s[i-1] = ')'`:若想 i 位的右括号为有效的，则必许保证 i-1 位的右括号也必须组成有效括号对才行，否则若前一位无效，i 位肯定无效，此时，只需要找到和 s[i]配对的位置，并判断其是否是`'('` 即可。和其配对对位置为`i-dp[i-1]-1`,若该位置是`'('`,则`dp[i] = dp[i-1]+2`，再加上左括号前面的有效括号对，因此，最终结果`dp[i] = dp[i-1]+2 + dp[i-dp[i-1]-1-1]`
- 初始条件和边界情况：
  - 初始条件：dp[i] = 0，边界情况必须`i-2>=0 and i-dp[i-1]-2>=0`
- 最终结果：dp 中的最大值
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

```Python []
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n = len(s)
        if n == 0: return 0
        dp = [0] * n
        res = 0
        for i in range(n):
            if i>0 and s[i] == ")":
                if  s[i - 1] == "(":
                    dp[i] = dp[i - 2] + 2
                elif s[i - 1] == ")" and i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == "(":
                    dp[i] = dp[i - 1] + 2 + dp[i - dp[i - 1] - 2]
                if dp[i] > res:
                    res = dp[i]
        return res
```
