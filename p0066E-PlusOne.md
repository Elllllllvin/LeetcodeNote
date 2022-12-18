> Problem: [66. 加一](https://leetcode.cn/problems/plus-one/description/)

# 思路

> 最朴素的做法

# Code

```Python []

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for i in range(len(digits)):
            num = num*10 + digits[i]
        num += 1
        res = []
        while(num>0):
            res = [num%10] + res
            num = num // 10
        return res
```
