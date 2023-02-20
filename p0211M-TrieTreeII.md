_Italic_> Problem: [211. 添加与搜索单词 - 数据结构设计](https://leetcode.cn/problems/design-add-and-search-words-data-structure/description/)

# 思路

## 方法 ：208 题的前缀树写法+dfs

Trie，又称前缀树或字典树，是一棵有根树，其每个节点包含以下字段：

- 指向子节点的指针数组 children。对于本题而言，数组长度为 26，即小写英文字母的数量。此时 children[0] 对应小写字母 a，children[1] 对应小写字母 b，…，children[25]\textit{children}[25]children[25] 对应小写字母 zzz。
- 布尔字段 isEnd，表示该节点是否为字符串的结尾。

## Code2

```Python
class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        # 从字典树的根开始，插入字符串。对于当前字符对应的子节点，
        # 如果存在，则跳到该子节点，并处理下一个
        # 如果不存在，则创建一个新的子节点
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        # 重复以上步骤，直到处理字符串的最后一个字符，然后将当前节点标记为字符串的结尾。
        node.isEnd = True


class WordDictionary:

    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)

    def search(self, word: str) -> bool:
        def dfs(i,node):
            if i == len(word):
                return node.isEnd
            ch = word[i]
            if ch =='.':
                for child in node.children:
                    if child != None and dfs(i+1,child):
                        return True
            else:
                child = node.children[ord(ch)-ord('a')]
                if child != None and dfs(i+1,child):
                    return True
            return False
        return dfs(0,self.trieRoot)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
```
