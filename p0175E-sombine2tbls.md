_Italic_> Problem: [175.组合两个表](https://leetcode.cn/problems/combine-two-tables/description/)

# 思路

> 数据库的题

inner join：2 表值都存在
outer join：附表中值可能存在 null 的情况。

总结：

①A inner join B：取交集

②A left join B：取 A 全部，B 没有对应的值，则为 null

③A right join B：取 B 全部，A 没有对应的值，则为 null

④A full outer join B：取并集，彼此没有对应的值为 null

上述 4 种的对应条件，在 on 后填写。

# Code 动态规划

```sql

select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
;

```
