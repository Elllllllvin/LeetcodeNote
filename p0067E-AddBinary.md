> Problem: [67. 二进制求和](https://leetcode.cn/problems/add-binary/description/)

# 思路

自己想的非常朴素的方法

# Code

```Python []

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n = len(a)-1,len(b)-1
        res = ''
        c = 0
        while(m>=0 and n>=0):
            if a[m] != b[n]:
                if c == 1:
                    res = '0' + res
                elif c == 0:
                    res = '1' + res
            else:
                if a[m] == b[n] == '0':
                    res = str(c) + res
                    c = 0
                else:
                    if c == 1:
                        res = '1' + res
                    elif c == 0:
                        res = '0' + res
                    c = 1
            m -= 1
            n -= 1
            print(res)
        while(m>=0):
            if c==1:
                if a[m] == '0':
                    res = '1'+res
                    c = 0
                elif a[m] == '1':
                    res = '0'+res
                    c = 1
            else:
                res = a[m] + res
            m-=1
        while(n>=0):
            if c==1:
                if b[n] == '0':
                    res = '1'+res
                    c = 0
                elif b[n] == '1':
                    res = '0'+res
                    c = 1
            else:
                res = b[n] + res
            n-=1
        if c == 1:
            res = '1'+res
        return res

```

# code2 官方位运算(没懂，，)

```Python []
class Solution:
    def addBinary(self, a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

```
