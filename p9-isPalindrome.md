> Problem: [9. 回文数](https://leetcode.cn/problems/palindrome-number/description/)

# Code1 转化成字符串

转化成字符串，从两边往中间比较,效率不是很高

65.24% , 39.93%

- 时间复杂度: $O(n)$

```Python []

class Solution:
    def isPalindrome(self, x: int):
        if (x<0):
            return False
        x = str(x)
        i = 0
        j = len(x)-1
        flag = 1
        while(i<j):
            if x[i]!=x[j]:
                flag = 0
                break
            i += 1
            j -= 1
        if flag:
            return True
        else:
            return False

```

# Code2 数学解法

更慢了。。不推荐

```Python []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        flag = 1
        y = 1
        realx = x
        revx = 0
        frontzero = 0
        while(True):
            if (x==0):
                break
            if (flag and x%10 == 0):
                flag = 1
                frontzero += 1
            else :
                flag = 0

            revx = revx*10 + x%10
            y = y*10
            x = x//10

        if frontzero == 0 and revx == realx :
            return True
        else:
            if (frontzero != 0 and '0'*frontzero + str(revx) == str(realx)):
                return True
            else :
                return False

```

# Code3 Python 切片解法

最快！python 特性
79.8% 5.30%（因为用了字符串）

```Python []
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        elif(0<=x<=9):
            return True

        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

```
