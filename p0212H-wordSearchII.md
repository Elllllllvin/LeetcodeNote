_Italic_> Problem: [212. 单词搜索 II](https://leetcode.cn/problems/word-search-ii/description/)

# 思路

## 方法 1：前缀树+dfs 回溯

## Code1

```Python
class Trie:
    def __init__(self):
        self.children = collections.defaultdict(Trie)
        self.word = ''

    def insert(self,word):
        cur = self
        for ch in word:
            cur = cur.children[ch]
        cur.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rootTree = Trie() #建立字典树
        for word in words:
            rootTree.insert(word)

        def dfs(trie,i,j):
            if board[i][j] not in trie.children:
                return
            ch = board[i][j]

            cur = trie.children[ch]
            if cur.word != '': #表示ch是最后一个字符了
                #如果cur.word有东西，就表示trietree里已经找完该单词
                res.add(cur.word)
            if cur.children:#剪枝优化一下
                board[i][j] = '#' #暂时将该字符转换为特殊字符，防止dfs时重复遍历
                                #最后别忘了回溯

                for p,q in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:  #简便的dfs写法（学会！！）
                    if 0 <= p < m and 0 <= q < n:
                        dfs(cur,p,q)
                board[i][j] = ch #i，j点dfs之后要记得回溯

        res = set()
        m,n = len(board),len(board[0])

        for i in range(m):
            for j in range(n):
                dfs(rootTree,i,j)

        return list(res)
```
