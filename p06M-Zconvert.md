> Problem: [6. Z 字形变换](https://leetcode.cn/problems/zigzag-conversion/description/)

# Code1 又麻烦又蠢的方法——二维数组表示

```Python []

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        res = [[False]*len(s) for i in range(numRows)]
        i = 0
        n = 1
        if numRows <= 1:
            return s;
        elif numRows >1:
            n = numRows-1
        for cur_col in range(0,len(s),n):
            for cur_row in range(2*numRows-2):
                if(i>=len(s)):
                    break
                if cur_row < numRows:
                    res[cur_row][cur_col]=s[i]
                    i+=1
                elif cur_row >= numRows:
                    x = (cur_row+1)%numRows #col
                    y = numRows - 1 - x
                    res[y][x+cur_col] = s[i]
                    i+=1
        reslst = []
        for r in range(numRows):
            for line in range(len(s)) :
                if(res[r][line]!=False):
                    reslst.append(res[r][line])
        finalres = ''.join(reslst)
        return finalres

```

# Code1 别人的神仙方法——flag 妙用

```Python []
class Solution(object):
    def convert(self, s, numRows):
        if numRows < 2: return s
        res = ["" for _ in range(numRows)]
        i, flag = 0, -1
        for c in s:
            res[i] += c
            if i == 0 or i == numRows - 1: flag = -flag
            i += flag
        return "".join(res)


```
