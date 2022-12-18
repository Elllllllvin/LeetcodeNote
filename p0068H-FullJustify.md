> Problem: [68. 文本左右对齐](https://leetcode.cn/problems/text-justification/description/)

# 思路

> 终于自己做出来一回 555555

# Code

```Python []

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        n = len(words)
        i = 0
        while(i<n):
            s = []
            cnt = 0
            while(i<n and (cnt + len(words[i])+1 <= maxWidth+1)):
                s.append(words[i])
                cnt = cnt + len(words[i]) + 1
                i += 1
            perword = ''
            if i==n:
                templen = 0
                for j in range(len(s)):
                    if len(s[j]) == maxWidth:
                        perword = s[j]
                        templen += len(s[j])
                    else:
                        perword += s[j]+' '
                        templen += len(s[j])+1
                if templen > maxWidth:
                    perword = perword[:maxWidth]
                else:
                    perword += ' '*(maxWidth-templen)
            else:
                totalblank = maxWidth - len(''.join(s))
                inteval = len(s) - 1
                resblank = totalblank - inteval
                for j in range(len(s)):
                    if j<len(s)-1:
                        if(resblank % inteval != 0):
                            perword += s[j] + ' '*(1 + resblank // inteval +1)
                            resblank -=  resblank // inteval +1
                            inteval -= 1
                        elif(resblank % inteval == 0):
                            perword += s[j] + ' '*(1 + resblank // inteval)
                            resblank -=  resblank // inteval
                            inteval -= 1
                    else:
                        perword += s[j]
                        perword = perword + ' '*(maxWidth-len(perword))

            res.append(perword)

        return res

```
