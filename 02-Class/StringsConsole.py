Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> text = "Hello world this is python programming"
>>> text[0]
'H'
>>> text[0:4]
'Hell'
>>> text[0:5]
'Hello'
>>> text[-1]
'g'
>>> len(text)
38
>>> text[38]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    text[38]
IndexError: string index out of range
>>> text[37]
'g'
>>> text[30]
'g'
>>> text[0:20:2]
'Hlowrdti s'
>>> text
'Hello world this is python programming'
>>> text[20:0]
''
>>> text[20:0:-1]
'p si siht dlrow olle'
>>> text[20::-1]
'p si siht dlrow olleH'
>>> text[:]
'Hello world this is python programming'
>>> text[:7]
'Hello w'
>>> text[20:]
'python programming'
>>> text[::-1]
'gnimmargorp nohtyp si siht dlrow olleH'
>>> text[-1:-10]
''
>>> text[-1:-10:-1]
'gnimmargo'
>>> text[-10:-1]
'rogrammin'
>>> dir(str())
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> text.lower()
'hello world this is python programming'
>>> text.upper()
'HELLO WORLD THIS IS PYTHON PROGRAMMING'
>>> text.title()
'Hello World This Is Python Programming'
>>> text.capitalize()
'Hello world this is python programming'
>>> text.count('i')
3
>>> text.find('i')
14
>>> text.find('i',15)
17
>>> text.find('i',18)
35
>>> text.isalnum()
False
>>> text.isalpha()
False
>>> text.isdigit()
False
>>> text.startswith('h')
False
>>> text.startswith('H')
True
>>> text.startswith('h' or 'H')
False
>>> text.center(20)
'Hello world this is python programming'
>>> text.center(38)
'Hello world this is python programming'
>>> text.center(39)
' Hello world this is python programming'
>>> text.center(40)
' Hello world this is python programming '
>>> text.center(60)
'           Hello world this is python programming           '
>>> text.center(60,'*')
'***********Hello world this is python programming***********'
>>> text.zfill(50)
'000000000000Hello world this is python programming'
>>> 
