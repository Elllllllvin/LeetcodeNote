> Problem: [65. 有效数字](https://leetcode.cn/problems/valid-number/description/)

# 思路

> 1.硬做。。。 2.这辈子也学不会的有限状态机。。

# Code1 自己做的

```Python []

class Solution:
    def isNumber(self, s: str) -> bool:
        res = True
        i = 0
        if len(s)==1 and s[0].isdigit() == False:
            return False
        if s[0] == '+' or s[0] == '-':
            s = s[1:]
        if len(s)==1 and s[0].isdigit() == False:
            return False
        cntE = 0
        cntSign = 0
        cntDot = 0
        cntdigit = 0
        while(i<len(s)):
            if s[i] == '+' or s[i] == '-':
                if cntSign == 0 :
                    res = False
                    break
                else:
                    if (s[i-1] == 'e' or s[i-1] == 'E') and i != len(s)-1:
                        cntSign = 0
                    else:
                        res = False
                        break
            if s[i].isalpha():
                if (s[i]=='e' or s[i] == 'E') and cntE == 0 and (len(s)-1>i>0 and (s[i-1].isdigit()or (s[i-1]=='.' and i != 1) ) and (s[i+1].isdigit() or s[i+1] in ['+','-'])):
                    cntE = 1
                    cntSign = 1
                else:
                    res = False
                    break

            if s[i] == '.' :
                if cntDot == 0 and cntE == 0:
                    cntDot = 1
                else:
                    res = False
                    break
            i+=1
        print(cntSign)
        return res
```

# Code2 官方：有限状态机（时间太晚了，，懒得看了。。。）

```Python []
from enum import Enum

class Solution:
    def isNumber(self, s: str) -> bool:
        State = Enum("State", [
            "STATE_INITIAL",
            "STATE_INT_SIGN",
            "STATE_INTEGER",
            "STATE_POINT",
            "STATE_POINT_WITHOUT_INT",
            "STATE_FRACTION",
            "STATE_EXP",
            "STATE_EXP_SIGN",
            "STATE_EXP_NUMBER",
            "STATE_END"
        ])
        Chartype = Enum("Chartype", [
            "CHAR_NUMBER",
            "CHAR_EXP",
            "CHAR_POINT",
            "CHAR_SIGN",
            "CHAR_ILLEGAL"
        ])

        def toChartype(ch: str) -> Chartype:
            if ch.isdigit():
                return Chartype.CHAR_NUMBER
            elif ch.lower() == "e":
                return Chartype.CHAR_EXP
            elif ch == ".":
                return Chartype.CHAR_POINT
            elif ch == "+" or ch == "-":
                return Chartype.CHAR_SIGN
            else:
                return Chartype.CHAR_ILLEGAL

        transfer = {
            State.STATE_INITIAL: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT,
                Chartype.CHAR_SIGN: State.STATE_INT_SIGN
            },
            State.STATE_INT_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_POINT: State.STATE_POINT_WITHOUT_INT
            },
            State.STATE_INTEGER: {
                Chartype.CHAR_NUMBER: State.STATE_INTEGER,
                Chartype.CHAR_EXP: State.STATE_EXP,
                Chartype.CHAR_POINT: State.STATE_POINT
            },
            State.STATE_POINT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_POINT_WITHOUT_INT: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION
            },
            State.STATE_FRACTION: {
                Chartype.CHAR_NUMBER: State.STATE_FRACTION,
                Chartype.CHAR_EXP: State.STATE_EXP
            },
            State.STATE_EXP: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER,
                Chartype.CHAR_SIGN: State.STATE_EXP_SIGN
            },
            State.STATE_EXP_SIGN: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
            State.STATE_EXP_NUMBER: {
                Chartype.CHAR_NUMBER: State.STATE_EXP_NUMBER
            },
        }

        st = State.STATE_INITIAL
        for ch in s:
            typ = toChartype(ch)
            if typ not in transfer[st]:
                return False
            st = transfer[st][typ]

        return st in [State.STATE_INTEGER, State.STATE_POINT, State.STATE_FRACTION, State.STATE_EXP_NUMBER, State.STATE_END]

作者：力扣官方题解
链接：https://leetcode.cn/problems/valid-number/solutions/564188/you-xiao-shu-zi-by-leetcode-solution-298l/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

```
