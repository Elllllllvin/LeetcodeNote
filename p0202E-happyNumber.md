_Italic_> Problem: [202. 快乐数](https://leetcode.cn/problems/happy-number/)

# 思路

哈希表！

# Code

```Python

class Solution:
    def isHappy(self, n: int) -> bool:
        temp = n
        dic = {}
        while temp != 1 and temp not in dic:
            dic[temp] = 1
            s = 0
            while temp>0:
                s += (temp%10)**2
                temp = temp//10
            temp = s

        return temp == 1

```
