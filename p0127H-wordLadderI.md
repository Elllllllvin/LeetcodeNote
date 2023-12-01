> Problem: [127. 单词接龙](https://leetcode.cn/problems/word-ladder/description/)

# 思路

> 1.非常经典的 BFS 广度优先搜索

# 解题方法

> 1.通过 bfs 的方法，构建一个图

# Code1 BFS

- 时间复杂度: $O(n*Lengthofword)$
- 空间复杂度: $O(n)$

```Python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if not wordList or endWord not in wordList:
            return 0
        word_set = set(wordList)

        queue = [(beginWord,1)]
        while queue:
            word,level = queue.pop(0)
            if word == endWord:
                return level
            for i in range(len(word)):
                for j in range(26):
                    new_word = word[:i] + chr(ord('a')+j) + word[i+1:]
                    if new_word in word_set:
                        queue.append((new_word,level+1))
                        word_set.remove(new_word)

        return 0
```

# Code2
