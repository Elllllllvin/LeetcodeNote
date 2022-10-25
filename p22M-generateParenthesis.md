> Problem: [22. 括号生成](https://leetcode.cn/problems/generate-parentheses/description/)

递归法没啥好说的

# Code

```Python []

class Solution(object):
    def generateParenthesis(self, n):
        res = []
        if(n == 1):
            return ['()']
        else:
            for item in self.generateParenthesis(n-1):
                for i in range(len(item)):
                    res.append(item[:i+1]+'()'+item[i+1:])
            res = list(set(res))
            return res
```
