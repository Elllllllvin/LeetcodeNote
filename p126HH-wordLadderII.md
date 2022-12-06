> Problem: [126. 单词接龙 II](https://leetcode.cn/problems/word-ladder-ii/description/)

# 思路

> 好难好难好难好难好难！！！！！前 127 题中 Top3 难的一道

# Code BFS 建图+BFS 记录最短距离+DFS 求所有路径的集合

```Python []

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList = set(wordList + [beginWord])
        # Part1 建图
        n, dic= len(beginWord), defaultdict(list)
                                # 构建一个默认value为list的字典
        for word in wordList:
            for i in range(n):
                for j in range(26):
                    tmp = word[:i] + chr(ord('a')+j) + word[i + 1:]
                    if tmp != word and tmp in wordList:
                        dic[word].append(tmp)

        # Part2 BFS算最短路径
        queue, distance = [], defaultdict(int)
                                # 构建一个默认value为int的字典
        distance[endWord] = 0
        queue.append(endWord)
        # 从endWord开始
        while queue:
            for i in range(len(queue)):
                cur = queue.pop(0)
                for nxt in dic[cur]:
                    if nxt not in distance:
                        # 这里记录的均为最短路径
                        distance[nxt] = distance[cur] + 1
                        queue.append(nxt)
                # print(distance)
            if beginWord in distance:
                # 第一次bfs搜索到beginword后得到的distance一定是最短的
                break

        # Part3 DFS求路径集合
        def dfs(start, path):
            if start == endWord:
                res.append(path[:])
            else:
                for i in dic[start]:
                    if i in distance and distance[i] == distance[start] - 1:
                        path.append(i)
                        dfs(i, path)
                        path.pop() #回溯

        res = []
        dfs(beginWord, [beginWord])
        return res
```
