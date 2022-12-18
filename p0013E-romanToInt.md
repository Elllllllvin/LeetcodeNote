> Problem: [13. 罗马数字转整数](https://leetcode.cn/problems/roman-to-integer/description/)

# Code1 字符串子串替换

84.72% 12.22%

```Python []

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0

        hashMap1={'CM':900,'CD':400,'XC':90,'XL':40,'IX':9,'IV':4}
        for item in hashMap1:
            if(item in s):
                s = s.replace(item, str(hashMap1[item]))
                res += hashMap1[item]
        hashMap2={'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
        for item in hashMap2:
            if(item in s):
                res += hashMap2[item]*s.count(item)
                s = s.replace(item, str(hashMap2[item]))
        return res
```
