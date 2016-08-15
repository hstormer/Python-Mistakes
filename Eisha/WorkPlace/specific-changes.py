changes = [
      "-\t\t\t\tyes.append(float(hamming_df[alpha][beta])\n", 
      "+\t\t\t\tyes.append(float(hamming_df[alpha][beta]))\n"
    ]
counter = 0
LENGTHOFCHANGES = 0

print "=========================================================="

while len(changes) != 0 and len(changes) != 1:
	diff1 = []
	diff2 = []
	close = []
	least = 2000
	LENGTHOFCHANGES = 0
	for i in changes:
		close.append(len(i))
	print close
	for i in close:
		# Holds the item it is looking at, so it doesn't compare to itself
		hold = i
		close.remove(i)
		for otheritems in close:
			if (abs(i-otheritems)) < least:
				least = (abs(i-otheritems))
				diff1 = []
				diff2 = []
				diff1.append(i)
				diff2.append(otheritems)
				close.remove(otheritems)
				hold = 300000
		# Don't add myself back in, already been looked at.
		if hold != 300000:
			close.append(hold)

	for i in changes:
		if len(i) == diff1[0]:
			diff1 = []
			for letter in i:
				diff1.append(letter)
			changes.remove(i)
	for i in changes:
		if len(i) == diff2[0]:
			diff2 = []
			for letter in i:
				diff2.append(letter)
			changes.remove(i)
	print "The first line to compare: %r" % "".join(diff1)
	print "The second line to compare: %r" % "".join(diff2)

	if diff1[0] == '+' or diff1[0] == '-':
		diff1.pop(0)
	if diff2[0] == '+' or diff2[0] == '-':
		diff2.pop(0)
	run = True
	while run:
		if len(diff2) != 0 and len(diff1) != 0:
			if diff1[0] == diff2[0]:
				diff1.pop(0)
				diff2.pop(0)
			else:
				run = False
		else:
			run = False
	run = True
	while run:
		if len(diff2) != 0 and len(diff1) != 0:
			if diff1[-1] == diff2[-1]:
				diff1.pop(-1)
				diff2.pop(-1)
			else:
				run = False
		else: 
			run = False
	print "The differences:"
	print "%r" % "".join(diff1)
	print "%r" % "".join(diff2)
	counter += 1
	LENGTHOFCHANGES += len(diff1)
	LENGTHOFCHANGES += len(diff2)
	print "Length of changes so far: %r" % LENGTHOFCHANGES
	print "========================"

if len(changes) == 1:
	print "The differences:"
	print "%r" % changes[0]
	LENGTHOFCHANGES += len(changes[0])

print "Total differences: %d" % LENGTHOFCHANGES


