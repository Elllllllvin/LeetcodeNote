> Problem: [43. 字符串相乘](https://leetcode.cn/problems/multiply-strings/description/)

# 思路

> 按位打开，按位转换

# 解题方法

> 题目说不能直接转换成整数，结果官方自己用了 int 函数。。。。

# Code

```Python3 []

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        hashmap = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
                    0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9'}
        mul1,mul2 = 0,0
        for i in range(len(num1)):
            mul1 = mul1*10 + hashmap[num1[i]]
        for i in range(len(num2)):
            mul2 = mul2*10 + hashmap[num2[i]]
        s = mul1*mul2
        # print(mul1,mul2,s)
        res = ''
        if s==0:
            return hashmap[s]
        while s != 0:
            res = hashmap[s%10] + res
            s = s//10
        return res
```
