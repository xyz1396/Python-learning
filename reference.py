#1/urs/bin/python
print'simple assignment'
shoplist=['apple','mango','carrot','banana']
shoplist2=[]
for name in shoplist:
	shoplist2.append(name)
mylist=shoplist
del shoplist[0]
print'shop list is',shoplist
print'my list is',mylist
print'shoplist2 is',shoplist2
