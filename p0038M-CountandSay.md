> Problem: [38. 外观数列](https://leetcode.cn/problems/count-and-say/description/)

# 思路

> 递归求解

# 复杂度

- 时间复杂度: $O(n)$

- 空间复杂度: $O(n)$
  递归的空间复杂度取决于栈的深度

# Code

```Python []

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==1:
            return '1'
        else:
            last = self.countAndSay(n-1)
            pre_i = 0
            i = 0
            l = []
            while(i<len(last)):
                i += 1
                while(i < len(last) and last[i] == last[i-1]):
                    i += 1
                l.append(last[pre_i:i])
                pre_i = i

            res = ''
            for item in l:
                res += str(len(item))+item[0]
            return res
```
