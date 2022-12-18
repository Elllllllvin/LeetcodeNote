> Problem: [29. 两数相除](https://leetcode.cn/problems/divide-two-integers/description/)

# Code

68.28% 60.80%

```Python []

import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        x = dividend/divisor

        if(x<-1*math.pow(2,31)):
            x = math.pow(2,31)
        elif(x>math.pow(2,31)-1):
            x=math.pow(2,31)-1
        x = int(x)
        return x
```
