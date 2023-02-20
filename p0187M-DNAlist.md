_Italic_> Problem: [187. DNA 重复序列](https://leetcode.cn/problems/repeated-dna-sequences/description/)

# 思路

法 1：hashtable
法 2：滑动窗口 + 位运算 + hashtable

# 解题方法

法 1：将序列长为 10 的序列全都存到 hash 表中，记录出现次数，只计算出现两次的序列。

法 2：因为一共四个字符 AGCT，可以将每个字符用 2 个比特表示，因此表示一个 10 位的字符串可以用 20bit 表示，又因为一个 int 为 32bit，因此可以用一个整数来表示序列，为了提升效率，使用滑动窗口。

# Code1: hashtable

- 时间复杂度: $O(n*L)$
- 空间复杂度: $O(n*L)$

```Python

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n<10:
            return []
        res = []
        cnt = defaultdict(int)
        for i in range(n-10+1):
            sub = s[i:i+10]
            cnt[sub] += 1
            if cnt[sub]  == 2:
                res.append(sub)
        return res
```

# Code2 slide window + bit compute + hashtable

```Python
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n<10:
            return []
        res = []
        chr2bin = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        x = 0
        for ch in s[:9]:
            x = (x << 2) | chr2bin[ch]
        cnt = defaultdict(int)
        for i in range(n - 10 + 1):
            x = ((x << 2) | chr2bin[s[i + 10 - 1]]) & ((1 << (2 * 10)) - 1)
            cnt[x] += 1
            if cnt[x] == 2:
                res.append(s[i : i + 10])

        return res
```
