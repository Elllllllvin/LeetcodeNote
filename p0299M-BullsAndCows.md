> Problem: [299. 猜数字游戏](https://leetcode.cn/problems/bulls-and-cows/description/)

[TOC]

# 思路
> 1.我自己的笨办法
> 2.官方的聪明算法（巧用zip）

# 解题方法
> 描述你的解题方法

# 复杂度
- 时间复杂度: 
> 添加时间复杂度, 示例： $O(n)$

- 空间复杂度: 
> 添加空间复杂度, 示例： $O(n)$

# Code1
```Python []

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        n = len(secret)
        A,B = 0,0
        dic = dict()
        for i in range(n):
            if secret[i] not in dic:
                dic[secret[i]] = 1
            else:
                dic[secret[i]] += 1
        for i in range(n):
            if secret[i] == guess[i] and guess[i] in dic and dic[guess[i]] > 0:
                A += 1
                dic[guess[i]] -= 1
        for i in range(n):
            if secret[i] != guess[i] and guess[i] in dic and dic[guess[i]] > 0:
                B += 1
                dic[guess[i]] -= 1
        print(dic)
        return str(A)+'A'+str(B)+'B'
            

```
# Code2
``` Python []
class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cntS, cntG = [0] * 10, [0] * 10
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                cntS[int(s)] += 1
                cntG[int(g)] += 1
        cows = sum(min(s, g) for s, g in zip(cntS, cntG))
        return f'{bulls}A{cows}B'

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/bulls-and-cows/solutions/1088724/cai-shu-zi-you-xi-by-leetcode-solution-q9lz/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


```
