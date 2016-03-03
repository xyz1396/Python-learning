#!/urs/bin/python
shoplist=['apple','mango','carrot','banana']
print 'I have',len(shoplist),'items to purchase.'
print'these items are:',
for item in shoplist:
	print item,
print'\n I also have to by rice.'
shoplist.append('rice')
print'my shoplist is now',shoplist
print'I will sort my list now'
shoplist.sort()
print'sorted shoplist is now',shoplist
print'the first item I wil buy is',shoplist[0]
olditem=shoplist[0]
del shoplist[0]
print'I bought the',olditem
print'my shoplist is now',shoplist