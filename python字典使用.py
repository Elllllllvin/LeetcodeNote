''' 一、python标准库之collections 
    collections是python中基础数据类型的容器模块，
    提供了更加便捷和快速的数据类型操作的方法，主要有以下几个：
    - 1.Counter()
    - 2.defaultdict()
    - 3.OrderDict()
    - 4.namedtuple()
    - 5.deque()
'''


'''
 - 1.Counter()
统计序列中元素的个数：
作为输入， Counter对象可以接受任意的由可哈希（hashable）元素构成的序列对象。
在底层实现上，一个 Counter 对象就是一个字典，将元素映射到它出现的次数上。
'''
from collections import Counter

def test_counter():
    text = "kshfkhdghskdnvknsighdsihinisdhguidhicoidsjiohfiuerhrfjsiohgi"
    words = Counter(text)
    print(words.items())        # 序列中各元素出现的次数
    print(words.most_common(3)) # 序列中出现次数最多的三个
    print(words["k"])           # 查看序列中某个元素出现的次数
    print(words)                # 查看序列
# test_counter()


'''
 - 2.defaultdict()
   定义一个默认格式的字典
'''
from collections import defaultdict
def test_defaultdict():
    d = defaultdict(list)  # 创建一个value默认为list类型的字典
    d["a"].append(1)
    d["a"].append(2)
    d["a"].append(3)
    print(d)
    print(d["a"])
    print(d["b"])   # 即使没有key("b"),取值也不会报错，依然会有默认值[]
                    # 换言之，用defaultdict，就不需要判断if key in d.keys() ... 了

    s = defaultdict(set)  # 创建一个value默认为list类型的字典
    s["aa"].add(1)
    s["aa"].add(2)
    print(s["aa"],"__", s["bb"])
# test_defaultdict()

'''
- 3.OrderDict()
保留键值插入的顺序并以此顺序排列:
OrderDict内部维护着一个根据键值插入顺序的双向链表，每当一个新的元素被插入进来的时候，它会被放到链表的尾部。
对于一个已存在的键值赋值不会改变键值的顺序。
'''
from collections import OrderedDict
def test_OrderedDict():
    od = OrderedDict()  # 创建一个value默认为list类型的字典
    od['z'] = 1
    od['y'] = 2
    od['x'] = 3
    print(od)
    od.move_to_end('z') #将该元素移到字典的末尾
    print(od)
    od.move_to_end('z',last = False) #将该元素移到字典的首位
    print(od)
    a = od.popitem(last = False) #删除字典首个元素
    print(a)
    b = od.popitem(last = True) #则删除字典末尾元素
    print(b)
    print(od)
# test_OrderedDict()


'''
- 4.namedtuple()
namedtuple()是一个方法生成的对象是tuple的子类，用来定义一个有指定含义的元组，
通常我们定义一个元组无法知道他内部元素的含义，但是使用了namedtuple()就可以很清晰的知道这个元祖的的元素是用来干什么的
'''
# 和类的作用一样
from collections import deque, namedtuple
def test_namedtuple():
    Person = namedtuple("Person", ["name", "age", "gender"])
    person = Person("lily", 20, "female")
    print(person.age)
    print(person.name)
    print(person.gender)
    print(person)
test_namedtuple()

'''
- 5.deque()
deque()可以创建一个队列容器
它与python的list的区别在于deque()在增加元素的时候，超出设定元素个数大小时，会默认删除最早的那个;
同时deque不像list是一个线性存储，deque是一个双向链表，数据量大的时候插入效率大大高于list
'''
from collections import deque
def test_deque():
    q1 = deque(maxlen=3)
    q1.append(1)
    q1.append(2)
    q1.append(3)
    q1.append(4)
    print(q1)
# deque包含的方法：其中pop从队列的尾部抛出数据，
# 从队列头部取数据则用popleft（）
    a = q1.pop()
    b = q1.popleft()
    print(a,b)
    print(q1)


test_deque()
# deque([2, 3, 4], maxlen=3)

    