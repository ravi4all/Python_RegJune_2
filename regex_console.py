Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import re
>>> text = "Salary of Ram is 15000 and Salary of Shyam is 20000"
>>> re.findall('[A-Z]\w+', text)
['Salary', 'Ram', 'Salary', 'Shyam']
>>> re.findall('[A-Z|0-9]\w+', text)
['Salary', 'Ram', '15000', 'Salary', 'Shyam', '20000']
>>> email = 'ram123@gmail.com'
>>> re.match('[a-z|0-9]\w+[@]\w+[.]\w{3}',email)
<re.Match object; span=(0, 16), match='ram123@gmail.com'>
>>> words = ["playing","starting","working","studying"]
>>> words = ["playing","starting","working","studying","study",]
>>> 
>>> words = ["playing","starting","working","studying","study","work","play"]
>>> for word in words:
	if re.match('[a-z]\w+[ing]', word):
		print(word)

		
playing
starting
working
studying
>>> 
