#example1:函数
#!/user/bin/python
#Filename:ptjiaocheng.py

def sayHello():
	print('Hello World!') # block belonging to the function
	
sayHello() # call the function




#example2:函数形参
#!/user/bin/python
#Filename:pyjiaocheng07.py
def printMax(a,b):
	if a>b:
		print(a,'is maximum')
	else:
		print(b,'is maximum')
printMax(3,4) # directly give literal values

x = 5
y = 7
printMax(x,y) # give variables as arguments