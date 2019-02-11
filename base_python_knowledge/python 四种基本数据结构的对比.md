# python 四种基本数据类型比较

[TOC]

## list

> list是Python内置的一种数据类型是列表，是一种有序的集合，可以随时添加和删除其中的元素。

和Java相比的不同点：
1. 如果要取最后一个元素，除了计算索引位置外，还可以用-1做索引，直接获取最后一个元素：

   ```python
   classmates = ['Kong', 'John', 'Toms', 'Yang']
   classmates[-1]
   # Out[3]: 'Yang'
   ```

2. 可以把元素插入到指定的位置，比如索引号为1的位置：

   ```python
   classmates.insert(1, 'Maria')
   classmates
   # Out[5]: ['Kong', 'Maria', 'John', 'Toms', 'Yang']
   ```

3. 要删除list末尾的元素，用pop()方法，删除指定位置的元素，用pop(i)方法，其中i是索引位置。

4. list里面的元素的数据类型也可以不同：

   ```python
   L = ['Apple', 123, True]
   ```
5. list元素也可以是另一个list：

   ```python
   s = ['python', 'java', ['asp', 'php'], 'scheme']
   len(s)
   # Out[10]: 4
   ```

## tuple

> tuple和list非常类似，但是tuple一旦初始化就不能修改。因为tuple不可变，所以代码更安全。如果可能，能用tuple代替list就尽量用tuple。

**需要注意的地方**

1. 只有1个元素的tuple定义时必须加一个逗号`,`来消除歧义：

   ```python
   t1 = ('1')
   type(t1)
   # Out[15]: str
   t = ('1',)
   # Out[17]: ('1',)
   type(t)
   # Out[18]: tuple
   
   ```

   

2. 也存在“可变的”tuple：

   ```python
   xx = ('1',2,['hello', 'shanghai'])
   # Out[20]: ('1', 2, ['hello', 'shanghai'])
   xx[2][1] = 'beijing'
   # Out[23]: ('1', 2, ['hello', 'beijing'])
   
   ```

   这个tuple定义的时候有3个元素，分别是'a'，'b'和一个list。不是说tuple一旦定义后就不可变了吗？怎么后来又变了？
   别急，我们先看看定义的时候tuple包含的3个元素：``tuple[-1]``

   > 表面上看，tuple的元素确实变了，但其实变的不是tuple的元素，而是list的元素。tuple一开始指向的list并没有改成别的list，所以，tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
   > 理解了“指向不变”后，要创建一个内容也不变的tuple怎么做？那就必须保证tuple的每一个元素本身也不能变。

## dict

> Python内置了字典：dict的支持，dict全称dictionary，在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度（按位置做索引，不会随着字典大小的增加而变慢）。

**需要注意的地方**

1. 通过dict提供的get()方法，如果key不存在，可以返回None，或者自己指定的value,使用键直接获取若键不存在会报错：

   ```python
   yy = {'name': 'Kong', 'age': 12, 'grade': 10}
   yy.get('name')
   # Out[25]: 'Kong'
   yy.get('hello', 'none')
   # Out[26]: 'none'
   yy['name']
   Out[27]: 'Kong'
   yy['hello']
   Traceback (most recent call last):
     File "/Users/johntoms/Library/Python/2.7/lib/python/site-packages/IPython/core/interactiveshell.py", line 2882, in run_code
       exec(code_obj, self.user_global_ns, self.user_ns)
     File "<ipython-input-28-f8f486117aca>", line 1, in <module>
       yy['hello']
   KeyError: 'hello'
   
   ```

   

2. 请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

3. <span style="color:red">和list比较，dict有以下几个特点</span>

   - 查找和插入的速度极快，不会随着key的增加而变慢；

   - 需要占用大量的内存，内存浪费多。

   <span style="color:red">而list相反</span>

   - 查找和插入的时间随着元素的增加而增加；

   - 占用空间小，浪费内存很少。

     > 所以，dict是用空间来换取时间的一种方法。

> dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。
> 这是因为dict根据key来计算value的存储位置，如果每次计算相同的key得出的结果不同，那dict内部就完全混乱了。这个通过key计算位置的算法称为哈希算法（Hash）。
> 要保证hash的正确性，作为key的对象就不能变。在Python中，字符串、整数等都是不可变的，因此，可以放心地作为key。而list是可变的，就不能作为key。

## set

>  set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。要创建一个set，需要提供一个list作为输入集合：

```python
ww = {'1',1}
# Out[30]: {1, '1'}
```



注意，传入的参数[1, 2, 3]是一个list，而显示的{1, 2, 3}只是告诉你这个set内部有1，2，3这3个元素，显示的顺序也不表示set是有序的。
重复元素在set中自动被过滤。

set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。当把多个list放入set，会报错。

