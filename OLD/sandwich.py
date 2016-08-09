from random import randint

file1 = open('test.arff', 'a+')

meat = ['ham', 'turkey', 'beef', 'chicken', 'bacon', 'none']
bread = ['whole_wheat', 'white', 'none']
cheese = ['cheddar', 'swiss', 'cheese_slice', 'none']
division = ['diagonal', 'straight', 'none']
sauce = ['mustard', 'mayonaise', 'none']
good_sandwich = ''
current_sandwich = ''
counter = 0

while counter != 10:
	counter += 1
	current_sandwich = "%s, %s, %s, %s, %s," % (meat[randint(0,5)], bread[randint(0,2)], cheese[randint(0,3)], 							division[randint(0,2)], sauce[randint(0,2)])
	print current_sandwich
	answer = str(raw_input("Is this a good sandwich? y/n"))
	if answer == 'y':
		answer = current_sandwich + ' yes'
	else:
		answer = current_sandwich + ' no'
	file1 = open('test.arff', 'a+')
	file1.write("\n%s" % answer)
	file1.close()

