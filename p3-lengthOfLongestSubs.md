Problem: [3. 无重复字符的最长子串](https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/)

# Code1 循环遍历

最老土的办法:嵌套循环，耗时过长，仅击败 9.37%

- 时间复杂度:
  > $O(n^2)$

```Python []

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        for head in range(len(s)):
            lst = []
            subs = s[head:]
            length = 0
            for i in subs:
                if i in lst:
                    break
                if i not in lst:
                    lst.append(i)
                    length += 1
                if length > maxlen:
                    maxlen = length
        return maxlen

```

# Code2 滑动窗口思想！重要!

滑动窗口思想：遍历字符串，窗口长度先加 1，如果当前元素之前没出现过，那么记录当前最大长度，并继续循环下一个，如果出现过，则一直删除前面窗口的元素，保证窗口内没有重复元素，因为之前已经记录了最大窗口长度，因此不必担心前面删除了其他元素

- 时间复杂度: 37.64%
  > $O(n)$

```Python []

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxlen = 0
        d = []
        cnt = 0
        for i in range(len(s)):
            cnt +=1
            while s[i] in d :
                cnt -= 1
                d = d[1:]
            d.append(s[i])
            if cnt > maxlen:
                maxlen = cnt
        return maxlen

```
