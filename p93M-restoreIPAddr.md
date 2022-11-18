> Problem: [93. 复原 IP 地址](https://leetcode.cn/problems/restore-ip-addresses/description/)

[TOC]

# 思路

> 经典回溯算法，dfs

# Code

```Python []

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        n = len(s)
        res = []
        def dfs(addr,temp,cnt):
            if cnt == 4 and len(temp) == 0 and len(addr)==n+4:
                res.append(addr[:-1])
                return
            if len(temp) == 1:
                dfs(addr + str(int(temp[0:1]))+'.',temp[1:],cnt+1)
            elif len(temp) == 2:
                dfs(addr + str(int(temp[0:1]))+'.',temp[1:],cnt+1)
                dfs(addr + str(int(temp[0:2]))+'.',temp[2:] , cnt+1)
            elif len(temp) >= 3 :
                if 0 <= int(temp[0:3]) <= 255:
                    dfs(addr + str(int(temp[0:3]))+'.',temp[3:],cnt+1)
                dfs(addr + str(int(temp[0:1]))+'.',temp[1:],cnt+1)
                dfs(addr + str(int(temp[0:2]))+'.',temp[2:],cnt+1)
        dfs('',s,0)
        return res
```
