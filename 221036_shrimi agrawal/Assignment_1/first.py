Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def my_function(rollno,name):
...     print(rollno,name)
... 
...     
>>> my_function(221036,"shrimi")
221036 shrimi
>>> 
>>> #question 7
>>> def my_function2():
...     print("example of calling a function")
... 
...     
>>> my_function2()
example of calling a function
>>> 
>>> #question 8
>>> def my_function3(k):
...     if(k>0):
...         return k+ my_function3(k-1)
...     else:
...         return 0
... 
...     
>>> my_function3(10)
55
