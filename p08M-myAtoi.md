> Problem: [8. 字符串转换整数 (atoi)](https://leetcode.cn/problems/string-to-integer-atoi/description/)

注意各种条件！！限制

# Code

击败了 88.95% 12.63%

```Python []

import math
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        signal = True
        res = ''
        if s == "" or s =="+" or s=="-":
            return 0
        if s[0].isdigit()==False and s[0]!='-'and s[0]!='+':
            return 0

        if (s[0]=='-'):
            signal = False
            s=s[1:]
        elif (s[0]=='+'):
            signal = True
            s=s[1:]

        for item in s:
            if item.isdigit():
                res = res+item
            else:
                break
        if res == "" :
            return 0

        if signal==True:
            res = int(res)
            if (res > math.pow(2,31)-1):
                res = math.pow(2,31)-1
        else:
            res = (-1)*int(res)
            if (res < -1*math.pow(2,31)):
                res = -1*math.pow(2,31)


        return int(res)



```
