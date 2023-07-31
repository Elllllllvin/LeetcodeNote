> Problem: [233. 数字 1 的个数](https://leetcode.cn/problems/number-of-digit-one/description/)

[TOC]

# 思路
>  想像成自行车密码锁


# Code
```Python []

class Solution:
    def countDigitOne(self, n: int) -> int:
        digit = 1
        res = 0
        high = n // 10
        cur = n % 10
        low = 0
        # 想像成自行车密码锁
        while high != 0 or cur != 0 :
            if cur == 0:
                res += (high-1)*digit + digit - 1 + 1
            elif cur == 1:
                res += high * digit + low + 1
            elif cur > 1 :
                res += (high+1)*digit
            low += digit*cur
            # 注意update变量时的顺序！！
            cur = high%10
            high = high//10
            digit = digit*10    

        return res


                 

        


```
