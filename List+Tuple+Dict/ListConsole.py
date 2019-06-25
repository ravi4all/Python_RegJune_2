Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = [1,2,3,45,6,12,'hello','hi','bye']
>>> type(x)
<class 'list'>
>>> x[0]
1
>>> x[0:4]
[1, 2, 3, 45]
>>> x[-1]
'bye'
>>> x[0:-1]
[1, 2, 3, 45, 6, 12, 'hello', 'hi']
>>> data = []
>>> data.append(12)
>>> data
[12]
>>> data.append(21)
>>> data
[12, 21]
>>> data.append(25)
>>> data.append(72)
>>> data.append(54)
>>> data
[12, 21, 25, 72, 54]
>>> data.append(65,43,21,45,6)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    data.append(65,43,21,45,6)
TypeError: append() takes exactly one argument (5 given)
>>> data.append([65,43,21,45,6])
>>> data
[12, 21, 25, 72, 54, [65, 43, 21, 45, 6]]
>>> data[-1]
[65, 43, 21, 45, 6]
>>> data.pop()
[65, 43, 21, 45, 6]
>>> data
[12, 21, 25, 72, 54]
>>> data.extend([65,43,21,45,6])
>>> data
[12, 21, 25, 72, 54, 65, 43, 21, 45, 6]
>>> data.pop()
6
>>> data.insert(2,100)
>>> data
[12, 21, 100, 25, 72, 54, 65, 43, 21, 45]
>>> data.pop(4)
72
>>> data.remove(5)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    data.remove(5)
ValueError: list.remove(x): x not in list
>>> data.remove(72)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    data.remove(72)
ValueError: list.remove(x): x not in list
>>> data.remove(54)
>>> data
[12, 21, 100, 25, 65, 43, 21, 45]
>>> data.index(65)
4
>>> data.sort()
>>> data
[12, 21, 21, 25, 43, 45, 65, 100]
>>> data.sort(reverse=True)
>>> data
[100, 65, 45, 43, 25, 21, 21, 12]
>>> data
[100, 65, 45, 43, 25, 21, 21, 12]
>>> x = data
>>> y = x
>>> x == y
True
>>> x == y == data
True
>>> x[0] = 0
>>> x
[0, 65, 45, 43, 25, 21, 21, 12]
>>> data
[0, 65, 45, 43, 25, 21, 21, 12]
>>> y
[0, 65, 45, 43, 25, 21, 21, 12]
>>> data[:]
[0, 65, 45, 43, 25, 21, 21, 12]
>>> z = data[:]
>>> z
[0, 65, 45, 43, 25, 21, 21, 12]
>>> dara
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    dara
NameError: name 'dara' is not defined
>>> data
[0, 65, 45, 43, 25, 21, 21, 12]
>>> z == data
True
>>> z[0] = 'hello'
>>> z
['hello', 65, 45, 43, 25, 21, 21, 12]
>>> data
[0, 65, 45, 43, 25, 21, 21, 12]
>>> x is y
True
>>> y is data
True
>>> x is z
False
>>> id(z)
2640926096328
>>> data.append([3,4,5,7,67,34])
>>> data
[0, 65, 45, 43, 25, 21, 21, 12, [3, 4, 5, 7, 67, 34]]
>>> x = data
>>> y = data[:]
>>> x is data
True
>>> y is data
False
>>> x[-1][0] = 'hello'
>>> x
[0, 65, 45, 43, 25, 21, 21, 12, ['hello', 4, 5, 7, 67, 34]]
>>> data
[0, 65, 45, 43, 25, 21, 21, 12, ['hello', 4, 5, 7, 67, 34]]
>>> y
[0, 65, 45, 43, 25, 21, 21, 12, ['hello', 4, 5, 7, 67, 34]]
>>> x is y
False
>>> x[-1]
['hello', 4, 5, 7, 67, 34]
>>> y[-1]
['hello', 4, 5, 7, 67, 34]
>>> x[-1] is y[-1]
True
>>> data.copy()
[0, 65, 45, 43, 25, 21, 21, 12, ['hello', 4, 5, 7, 67, 34]]
>>> z1 = data.copy()
>>> z1
[0, 65, 45, 43, 25, 21, 21, 12, ['hello', 4, 5, 7, 67, 34]]
>>> z1[-1][0] = 'bye'
>>> z1
[0, 65, 45, 43, 25, 21, 21, 12, ['bye', 4, 5, 7, 67, 34]]
>>> data
[0, 65, 45, 43, 25, 21, 21, 12, ['bye', 4, 5, 7, 67, 34]]
>>> import copy
>>> z2 = copy.deepcopy(data)
>>> z2[-1][0] = 'hello world'
>>> z2
[0, 65, 45, 43, 25, 21, 21, 12, ['hello world', 4, 5, 7, 67, 34]]
>>> z1
[0, 65, 45, 43, 25, 21, 21, 12, ['bye', 4, 5, 7, 67, 34]]
>>> data
[0, 65, 45, 43, 25, 21, 21, 12, ['bye', 4, 5, 7, 67, 34]]
>>> 
