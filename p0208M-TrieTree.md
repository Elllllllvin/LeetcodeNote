_Italic_> Problem: [208. 实现前缀树](https://leetcode.cn/problems/implement-trie-prefix-tree/description/)

# 思路

## 方法 1：自己想的，遍历找 prefix，能过但是太慢了

## Code1 dfs

时间复杂度：o(n)

空间复杂度：o(n)

```Python
class Trie:

    def __init__(self):
        self.TrieTree = set()

    def insert(self, word: str) -> None:
        self.TrieTree.add(word)

    def search(self, word: str) -> bool:
        if word in self.TrieTree:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for string in self.TrieTree:
            if prefix in string and string.index(prefix) == 0:
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

```

## 方法 2：官方前缀树写法

Trie，又称前缀树或字典树，是一棵有根树，其每个节点包含以下字段：

- 指向子节点的指针数组 children。对于本题而言，数组长度为 26，即小写英文字母的数量。此时 children[0] 对应小写字母 a，children[1] 对应小写字母 b，…，children[25]\textit{children}[25]children[25] 对应小写字母 zzz。
- 布尔字段 isEnd，表示该节点是否为字符串的结尾。

## Code2

```Python
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def searchPrefix(self, prefix: str) -> "Trie":
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return None
            node = node.children[ch]
        return node

    def insert(self, word: str) -> None:
        node = self
        # 从字典树的根开始，插入字符串。对于当前字符对应的子节点，
        # 如果存在，则跳到该子节点，并处理下一个
        # 如果不存在，则创建一个新的子节点
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        # 重复以上步骤，直到处理字符串的最后一个字符，然后将当前节点标记为字符串的结尾。
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.searchPrefix(word)
        return node is not None and node.isEnd
#     从字典树的根开始，查找前缀。对于当前字符对应的子节点，有两种情况：
#           - 子节点存在。沿着指针移动到子节点，继续搜索下一个字符。
#           - 子节点不存在。说明字典树中不包含该前缀，返回空指针。
# 重复以上步骤，直到返回空指针或搜索完前缀的最后一个字符。

# 若搜索到了前缀的末尾，就说明字典树中存在该前缀。此外，若前缀末尾对应节点的 isEnd\textit{isEnd}isEnd 为真，则说明字典树中存在该字符串。

    def startsWith(self, prefix: str) -> bool:
        return self.searchPrefix(prefix) is not None

作者：力扣官方题解
链接：https://leetcode.cn/problems/implement-trie-prefix-tree/solutions/717239/shi-xian-trie-qian-zhui-shu-by-leetcode-ti500/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```
