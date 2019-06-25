Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = (4,3,3,5,56,4)
>>> type(x)
<class 'tuple'>
>>> x = 4,3,3,5,56,4
>>> type(x)
<class 'tuple'>
>>> x = 12,
>>> x
(12,)
>>> data = "Ram","Shyam","Gopal","Anuj"
>>> data
('Ram', 'Shyam', 'Gopal', 'Anuj')
>>> data[0] = 'Hello'
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    data[0] = 'Hello'
TypeError: 'tuple' object does not support item assignment
>>> del data[0]
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    del data[0]
TypeError: 'tuple' object doesn't support item deletion
>>> data = name,age,sal = "Ram",40,40000
>>> data
('Ram', 40, 40000)
>>> name
'Ram'
>>> age
40
>>> sal
40000
>>> 
