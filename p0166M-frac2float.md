> Problem: [166. 分数到小数](https://leetcode.cn/problems/fraction-to-recurring-decimal/description/)

# 思路

> 差点自己想出来，，，这个就是一位一位的算！

# Code

```Python []

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator%denominator == 0:
            return str(int(numerator/denominator))
        s = []
        if numerator*denominator<0:
            s.append('-')

        numerator = abs(numerator)
        denominator = abs(denominator)
        intergerPart = numerator //denominator
        s.append(str(intergerPart))
        s.append('.')

        indexMap = {}
        remainder = numerator%denominator
        while remainder and remainder not in indexMap:
            indexMap[remainder] = len(s)
            remainder *= 10
            s.append(str(remainder//denominator))
            remainder %= denominator
        if remainder:  # 有循环节
            insertIndex = indexMap[remainder]
            s.insert(insertIndex, '(')
            s.append(')')

        return ''.join(s)

```
