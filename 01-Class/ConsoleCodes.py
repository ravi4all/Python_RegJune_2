Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is c
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is 44
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is 44
Sum is 44
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is 44
Sum is 44
Sum of 12 and 32 is 44
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is 44
Sum is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is 44
Sum is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
>>> name = "Ram"
>>> msg = "Hello " + name
>>> msg
'Hello Ram'
>>> sal = 12000
>>> msg = "Salary is " + sal
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    msg = "Salary is " + sal
TypeError: can only concatenate str (not "int") to str
>>> msg = "Salary is {}".format(sal)
>>> msg
'Salary is 12000'
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is 44
Sum is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
Sum of 44 and 12 is 32
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is 44
Sum is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/01-Code.py 
44
Sum is 44
Sum is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
Sum of 12 and 32 is 44
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/02-Code.py 

1. Add           3. Div
2. Sub           4. Mul

>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/02-Code.py 
hello this is python.hello this is python.hello this is python.
hello this is python.hello this is python.
hello this is python.hello this is python.hello this is python.
hello this is python.hello this is python.

1. Add           3. Div
2. Sub           4. Mul

>>> name = "Hello Ram"
>>> print(name)
Hello Ram
>>> name = 'Hello "Ram"'
>>> print(name)
Hello "Ram"
>>> name = """'Hello "Ram"'"""
>>> print(name)
'Hello "Ram"'
>>> name = "Hello\nRam"
>>> print(name)
Hello
Ram
>>> name = "Hello'\n'Ram"
>>> print(name)
Hello'
'Ram
>>> name = "Hello\\nRam"
>>> print(name)
Hello\nRam
>>> name = r"Hello\nRam"
>>> print(name)
Hello\nRam
>>> first name = "Ram"
SyntaxError: invalid syntax
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/03-Code.py 
Enter your name : Ram
Hello Ram
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/03-Code.py 
Enter your name : Ram
Hello Ram
Enter first number : 12
Enter second number : 55
Sum is 1255
>>> type(f_num)
<class 'str'>
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/June/PythonReg_2/01-Class/03-Code.py 
Enter your name : Ravi
Hello Ravi
Enter first number : 12
Enter second number : 22
Sum is 34
>>> a = 6
>>> id(a)
140713905775408
>>> id(6)
140713905775408
>>> b = 6
>>> c = a
>>> a
6
>>> b
6
>>> c
6
>>> id(a) == id(b) == id(c)
True
>>> import sys
>>> sys.getsizeof(1)
28
>>> sys.getsizeof(0)
24
>>> sys.getsizeof(323423)
28
>>> sys.getsizeof(123456789)
28
>>> sys.getsizeof(1234567890)
32
>>> sys.getsizeof('')
49
>>> sys.getsizeof('h')
50
>>> sys.getsizeof('he')
51
>>> msg = "hello how are you ?"
>>> msg.encode()
b'hello how are you ?'
>>> msg = "नमस्ते आप कैसे हैं ?"
>>> msg.encode()
b'\xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xb8\xe0\xa5\x8d\xe0\xa4\xa4\xe0\xa5\x87 \xe0\xa4\x86\xe0\xa4\xaa \xe0\xa4\x95\xe0\xa5\x88\xe0\xa4\xb8\xe0\xa5\x87 \xe0\xa4\xb9\xe0\xa5\x88\xe0\xa4\x82 ?'
>>> 
