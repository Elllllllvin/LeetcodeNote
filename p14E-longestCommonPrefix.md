> Problem: [14. 最长公共前缀](https://leetcode.cn/problems/longest-common-prefix/description/)

# Code1 循环比较

时间长，空间小
28.77% 97.89%

```Python []

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        flag = 0
        res = ''
        if(len(strs)==0):
            return ""
        elif (len(strs)==1):
            return strs[0]

        for j in range(len(strs[0])):
            for i in range(1,len(strs)):
                if (j>=len(strs[i]) or strs[i][j]!=strs[0][j]):
                    flag = 1
                    break
            if(flag):
                break
            res += strs[0][j]

        return res

```

# Code2 字符串排序+比较第一个和最后一个

85.14% 84.98%

```Python []
class Solution:
    def longestCommonPrefix(self, s: List[str]) -> str:
        if not s:
            return ""
        s.sort()
        n = len(s)
        a = s[0]
        b = s[n-1]
        res = ""
        for i in range(len(a)):
            if i < len(b) and a[i] == b[i]:
                res += a[i]
            else:
                break
        return res

```

# Code3 zip 函数妙用

zip()函数可以把多个 list 中的元素，按照元素下标重新排列

```Python []
#Zip函数用法
list1 = [1,2,3,4,5]
list2 = ["hello","good","nice","haha"]
set3 = {True,False,None,0}
zipobj = zip(list1,list2,set3)  # 打包

print(zipobj) # 这是一个包,显示的是包所在的地址 <zip object at 0x00000149CFFFAB48>

print(list(zipobj)) #可以将包转化为列表,查看包中的内容

# 打印结果为 [(1, 'hello', False), (2, 'good', True), (3, 'nice', None)]

解题方法：
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):
            tmp_set = set(tmp)
            if len(tmp_set) == 1:
                res += tmp[0]
            else:
                break
        return res
```
