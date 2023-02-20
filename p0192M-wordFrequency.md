_Italic_> Problem: [192. 统计词频（bash）](https://leetcode.cn/problems/word-frequency/description/)

# 思路

> bash 写脚本！！第一次遇到

1.切割
`tr` 命令用于转换或删除文件中的字符,`-s`缩减连续重复的字符成指定的单个字符。

```powershell
cat Words.txt| tr -s ' ' '\n'

the
day
is
sunny
the
the
the
sunny
is
is

```

2.排序单词

```powershell
cat Words.txt| tr -s ' ' '\n' | sort

day
is
is
is
sunny
sunny
the
the
the
the
```

3.统计单词出现次数
`uniq`命令用于检查及删除文本文件中重复出现的行列，一般与 sort 命令结合使用。`-c`：在每行旁边显示该行重复出现次数。

```powershell
cat Words.txt| tr -s ' ' '\n' | sort | uniq -c

1 day
3 is
2 sunny
4 the
```

4.排序单词出现次数，`-r`：以相反顺序排序。

```powershell
cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r

4 the
3 is
2 sunny
1 day

```

5.打印

```powershell
cat Words.txt| tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{print $2, $1}'

the 4
is 3
sunny 2
day 1

```

# Code

```powershell
# Read from the file words.txt and output the word frequency list to stdout.
cat words.txt | tr -s ' ' '\n' | sort | uniq -c | sort -r | awk '{ print $2, $1 }'


```
