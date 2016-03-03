#!/urs/bin/python
zoo=('wolf','elephant','penguin')
if __name__=='__main__':
	print'number of animals in the zoo is',len(zoo)
new_zoo=('monkey','dolphin',zoo)
if __name__=='__main__':
	print'number of animals in the new zoo is',len(new_zoo)
	print'animals in new zoo are',new_zoo
	print'animals brought from old zoo are',new_zoo[2]
	print'last animal brought from old zoo is',new_zoo[2][2]