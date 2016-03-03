#!/urs/bin/python
ab={'swaroop':'swaroop@qq.com',
	'larry':'larry@qq.com',
	'matsumoto':'matsumoto@qq.com',
	'spammer':'spammer@qq.com'};
print"swaroop's adress is %s"%ab['swaroop']
ab['guido']='guido@qq.com';
del ab['spammer'];
print'\nthere are %d cantacts in the address-book\n'%len(ab)
for name,address in ab.items():
	print'contact %s at %s'%(name,address)
if 'guido' in ab:
	print"\nguido's address is %s"% ab['guido']

