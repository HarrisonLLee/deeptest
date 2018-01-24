
#This is my shopping list
shoplist = ['apple','mango','carrot','banana']
print('I have',len(shoplist),'items to purchase.')

print('there items are:',)#Notice the comma at end of the line
for item in shoplist:
	print(item,)

print('\nI also have to buy rice')
shoplist.append('rice')
print('My shopping list is now',shoplist)

print('I will sort my list new')
shoplist.sort() #将列表内的item按字母顺序排序
print('Sorted shopping list is',shoplist)

print('The first item I will buy is',shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the',olditem)
print('My shopping list is now',shoplist)