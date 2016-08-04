changes = []

diff1 = []
diff2 = []

if len(changes) == 2:
	for i in changes[0]:
		diff1.append(i)
	for i in changes[1]:
		diff2.append(i)
	if diff1[0] == '+' or diff1[0] == '-':
		diff1.pop(0)
	if diff2[0] == '+' or diff2[0] == '-':
		diff2.pop(0)
	run = True
	while run:
		if len(diff2) != 0 and len(diff1) != 0:
			if diff1[0] == diff2[0]:
				print "%r" % diff1[0]
				print "%r" % diff2[0]
				diff1.pop(0)
				diff2.pop(0)
				print "------------------"
			else:
				run = False
		else:
			run = False
	run = True
	while run:
		if len(diff2) != 0 and len(diff1) != 0:
			if diff1[-1] == diff2[-1]:
				print "pop"
				print "%r" % diff1[-1]
				print "%r" % diff2[-1]
				diff1.pop(-1)
				diff2.pop(-1)
				print "------------------"
			else:
				run = False
		else: 
			run = False

print diff1
print diff2


