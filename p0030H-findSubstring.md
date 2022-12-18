> Problem: [30. 串联所有单词的子串](https://leetcode.cn/problems/substring-with-concatenation-of-all-words/description/)

# Code1 标答-滑动窗口

空间复杂度 $O(m*n)$
时间复杂度 $O(ls*n)$

```Python []

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        m, n, ls = len(words), len(words[0]), len(s)

        for i in range(n):
            if i + m * n > ls:
                break
            differ = Counter() #一个Counter
            for j in range(m):
                word = s[i + j * n: i + (j + 1) * n]
                differ[word] += 1
            for word in words:
                differ[word] -= 1
                if differ[word] == 0:
                    del differ[word]
            for start in range(i, ls - m * n + 1, n):
                if start != i:
                    word = s[start + (m - 1) * n: start + m * n]
                    differ[word] += 1
                    if differ[word] == 0:
                        del differ[word]
                    word = s[start - n: start]
                    differ[word] -= 1
                    if differ[word] == 0:
                        del differ[word]
                if len(differ) == 0:
                    res.append(start)
        return res

```

# Code2 自己模拟的滑动窗口，debug 了好久最后还是超时了。。。无语

心态崩了

```Python []
class Solution(object):
    def findSubstring(self, s, words):
        lenoW = len(words[0])
        res = []
        hashcnt = {}
        for item in words:
            if item in hashcnt.keys():
                hashcnt[item] += 1
            else:
                hashcnt[item] = 1
        for j in range(len(s)):
            if s[j:j+lenoW] in words:
                i = j
                left = right = i
                # print(j)
                tempcnt = {}
                for item in words:
                    tempcnt[item]= 0
                while i<len(s):
                    while s[i:i+lenoW] in words and tempcnt[s[i:i+lenoW]]<hashcnt[s[i:i+lenoW]]:
                        tempcnt[s[i:i+lenoW]] += 1
                        right = i+lenoW
                        i = i+lenoW
                    if right-left == lenoW * len(words):
                        res.append(left)
                        left += lenoW
                        i = right

                    else:
                        if s[i:i+lenoW] in words:
                            while(s[left:right].count(s[i:i+lenoW]) >= hashcnt[s[i:i+lenoW]]):
                                left += lenoW
                            right = i+lenoW
                            i = i+lenoW
                        else:
                            left = i+lenoW
                            right = left
                            i = left

        return list(set(res))



```
