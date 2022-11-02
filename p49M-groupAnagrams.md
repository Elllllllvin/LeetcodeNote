> Problem: [49. 字母异位词分组](https://leetcode.cn/problems/group-anagrams/description/)

# Code1 hash 表计数

```Python []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        if n <= 1 :
            return [strs]
        base = ord('a')
        hashtable = {}
        for item in strs:
            temp = [0]*26
            for letter in item:
                index = ord(letter)-ord('a')
                temp[index]+=1
            if tuple(temp) not in hashtable.keys():
                hashtable[tuple(temp)] = [item]
            elif tuple(temp) in hashtable.keys():
                hashtable[tuple(temp)].append(item)
        res = list(hashtable.values())
        print(hashtable)
        return res

```

# Code2 sorted 函数是可以把字符串拆开再排序的！！！

```Python []
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            key = "".join(sorted(st))
            mp[key].append(st)

        return list(mp.values())

```
