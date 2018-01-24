#example1
#表达式：求周长和面积
#!/user/bin/python
#Filename:expression.py

length = 5
breadth = 2
area = length * breadth
print('Area is', area)
print('Perimeter is',2*(length + breadth))

#example2
#!/user/bin/py
#Filename:pyjiaocheng.py
number = 23
guess = input('Enter an integer:')
if guess == number:
	print('Congretlation,you guessed it.')#new block starts here
	print('but you do not win any prizes')#new block ends here
elif:
	print('No,it is a little higher than that')#Another block
	# You can do whatever you want in a block ...
else:
	print('No,it is a little lower than that')
	#you must have guess number to reach here
print('Done')
#This last statement is always executed , after the if statement is executed


#example3：while循环
#!/user/bin/python
#Filename:pyjiaocheng.py

number == 23
running = True

while runing:
	guess = input('Enter')
	if guess == number:
		print('Congretlation,you guessed it.')
		running = False #this causes the while loop to stop
	elif guess > number:
		print('No,it is a little higher than that')
	else:
		print('No,it is a little lower than that')
else:
	print('The while loop is over.')
	# Do anything else you want to do here
print('Done')



#example4 : for循环
#!/user/bin/python
#Filename:pyjiaocheng.py
for i in range(1,5):
	print(i)
else:
	print('The for loop is over')

#example5 ：break语句 
#!/user/bin/python
#Filename:pyjiaocheng.py
while True:
	s = raw_input('Enter something:')
	if s == 'quit':
		break
	print('Length of the string is',len(s))
print('Done')


#example06：continue语句
'''
continue 语句用来告诉Python跳过当前循环块中的剩余语句，然后进行下一轮循环
'''
#!/user/bin/python
#Filename:pyjiaocheng.py
while True:
	s = input('Enter something:')
	if s == 'quit':
		break
	if len(s)
	print('Input is of sufficient length')
	


























