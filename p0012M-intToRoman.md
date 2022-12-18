> Problem: [12. 整数转罗马数字](https://leetcode.cn/problems/integer-to-roman/description/)

[TOC]

# Code1 贪心算法

73.42% 35.4%

```Python []

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''

        while(num>0):
            if (num>=1000):
                res = res+'M'*(num//1000)
                num = num%1000
            elif (1000>num>=500):
                if (num//100 == 9):
                    res += 'CM'
                    num -= 900
                else:
                    res += 'D'
                    num -= 500
            elif(500>num>=100):
                if (num//100 == 4):
                    res += 'CD'
                    num -= 400
                else:
                    res += 'C'
                    num -= 100
            elif(100>num>=50):
                if (num//10 == 9):
                    res += 'XC'
                    num -= 90
                else:
                    res += 'L'
                    num -= 50
            elif(50>num>=10):
                if (num//10 == 4):
                    res += 'XL'
                    num -= 40
                else:
                    res += 'X'
                    num -= 10
            elif(10>num>=5):
                if (num == 9):
                    res += 'IX'
                    num -= 9
                else:
                    res += 'V'
                    num -= 5
            elif(5>num):
                if (num== 4):
                    res += 'IV'
                    num -= 4
                else:
                    res += 'I'
                    num -= 1
        return res


```

# Code2 用哈希表优化一下代码

```Python []
class Solution:
    def intToRoman(self, num: int) -> str:
        # 使用哈希表，按照从大到小顺序排列
        hashmap = {1000:'M', 900:'CM', 500:'D', 400:'CD', 100:'C', 90:'XC', 50:'L', 40:'XL', 10:'X', 9:'IX', 5:'V', 4:'IV', 1:'I'}
        res = ''
        for key in hashmap:
            if num // key != 0:
                count = num // key  # 比如输入4000，count 为 4
                res += hashmap[key] * count
                num %= key
        return res

```
