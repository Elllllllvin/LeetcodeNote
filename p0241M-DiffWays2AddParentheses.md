> Problem: [241. 为运算表达式设计优先级](https://leetcode.cn/problems/different-ways-to-add-parentheses/description/)

[TOC]

# 思路
> 分治法 dfs啊啊啊啊啊

# 复杂度
- 时间复杂度: 复杂度与最终结果数相关，最终结果数为「卡特兰数

- 空间复杂度: 复杂度与最终结果数相关，最终结果数为「卡特兰数

# Code
```Python []

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        if expression.isdigit():
            return [int(expression)]

        res = []
        # 2*3-4*5
        for i in range(len(expression)):
            if expression[i].isdigit():
                continue
            else:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i+1:])
                for l in left:
                    for r in right:
                        if expression[i] ==  '+':
                            res.append(l+r)
                        elif expression[i] == '-':
                            res.append(l-r)
                        else:
                            res.append(l*r)
        
        return res

            
```
