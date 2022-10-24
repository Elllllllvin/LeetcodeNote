> Problem: [17. 电话号码的字母组合](https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/)

[TOC]

# 思路

> 利用 python 标准库 itertools 中的 itertools.product()函数进行求解

# 解题方法

> 对于两个列表`a = ['a','b','c'],b = ['d','e','f']`,他们的笛卡尔积为`a×b = [('a','d'),('a','e'),('a','f'),('b','d'),('b','e'),('b','f'),('c','d'),('c','e'),('c','f')]`

建立一个数字与字母的 map，利用笛卡尔积根据 digits 中的元素求得对应元组，再将各个元组转化为列表并合并为字符串元素，即得到一个字符串列表，再用此列表继续进行笛卡尔积

时间击败了 98.48%，空间击败了 48.24%

# Code

```Python []
import itertools
class Solution(object):
    def letterCombinations(self, digits):
        phone = {   '2':['a','b','c'],'3':['d','e','f']    ,'4':['g','h','i'],'5':['j','k','l'],
                    '6':['m','n','o'],'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z']   }
        if(len(digits) == 0):
            return []
        elif (len(digits) == 1):
            return phone[digits]
        else:
            res = phone[digits[0]]
            for i in range(1,len(digits)):
                res = [''.join(list(x)) for x in itertools.product(res,phone[digits[i]])]
                #笛卡尔积生成的元素是tuple，先将tuple化成list，再合并到一起
        return res


```
