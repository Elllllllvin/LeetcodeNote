> Problem: [343. 整数拆分](https://leetcode.cn/problems/integer-break/description/)

[toc]

# 思路

法1:dp
由于题目要求要将n拆分成k>=2的整数，因此，0和1不符合要求，dp[{0,1}]=0，然后用动态规划，要么继续拆`j*dp[i-j]`，要么不拆了`j*(i-j)`，要么不变`dp[i]`

法2:[数学推导，这个人推的非常清晰](https://leetcode.cn/problems/integer-break/solutions/29098/343-zheng-shu-chai-fen-tan-xin-by-jyd/)
**推论：将数字 n 尽可能以因子 3 等分时，乘积最大**
于是：
拆分规则：
最优： 3 。把数字 n 可能拆为多个因子 3 ，余数可能为 0,1,2 三种情况。
次优： 2 。若余数为 2 ；则保留，不再拆为 1+1 。
最差： 1 。若余数为 1 ；则应把一份 3+1 替换为 2+2，因为 2×2>3×1

# 复杂度
dp:
- 时间复杂度: $O(n)$
- 空间复杂度: $O(n)$

数学推导：
- 时间复杂度: $O(1)$
- 空间复杂度: $O(1)$

# Code1 dp

```Python
class Solution:
    def integerBreak(self, n: int) -> int:
        res = 1 
        dp = [0]*(n+1)
        # 1和0都不能拆分，题目规定要拆成k>=2个数
        for i in range(2,n+1):
            for j in range(1,i):
                dp[i] = max(j*(i-j),j*dp[i-j],dp[i])
                # print(i,dp[i])
        return dp[n]

```

# Code2
```Python3 []

class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3:
            return n-1
        a,b = n//3 , n%3
        if b==0:
            return 3**a
        elif b==1:
            return 3**(a-1)*(3+1)
        elif b == 2:
            return 3**a*2

        

                
```
  