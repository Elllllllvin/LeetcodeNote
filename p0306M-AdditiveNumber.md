> Problem: [306. 累加数](https://leetcode.cn/problems/additive-number/description/)

[toc]

# 思路

> 枚举第一个数和第二个数。。。。


# Code

```Python


class Solution:

    def isAdditiveNumber(self, num: str) -> bool:

        n = len(num)

        if n < 3:

            return False


        for secondstart in range(1,n-1):

            if num[0] == '0' and secondstart != 1:

                break

            for secondend in range(secondstart,n-1):

                if num[secondstart] == '0' and secondstart!= secondend:

                    break

                if self.valid(secondstart,secondend,num):

                    return True

        return False


    def valid(self,secondstart,secondend,num):

        n = len(num)

        firststart,firstend = 0,secondstart - 1

        while secondend <= n-1:

            third = self.addnum(firststart,firstend,secondstart,secondend,num)

            thirdstart = secondend + 1

            thirdend = thirdstart + len(third) - 1

            if thirdend >= n or num[thirdstart:thirdend+1] != third:

                break

            if thirdend == n-1:

                return True

            firststart,firstend = secondstart,secondend

            secondstart,secondend = thirdstart,thirdend

        return False


    def addnum(self,firststart,firstend,secondstart,secondend,num):

        a = int(num[firststart:firstend+1])

        b = int(num[secondstart:secondend+1])

        return str(a+b)



```
