changes = [
      "-# Copyright (C) 2015, 2016 Andrew Cagney <cagney@gnu.org>\n", 
      "+# Copyright (C) 2015-2016 Andrew Cagney <cagney@gnu.org>\n", 
      "+\n", 
      "+\n", 
      "+\n", 
      "+\n", 
      "-    # XXX: While len(expected) should technically be sufficient, that\n", 
      "-    # isn't clear without looking at sources.  Instead just \"double,\n", 
      "-    # and then double again\".\n", 
      "-    domain.logger.info(\"waiting %d seconds for domain to start\", timeout)\n", 
      "+    # XXX: While searchwindowsize=len(expected) should technically be\n", 
      "+    # sufficient to speed up matching, it isn't.  In fact, when more\n", 
      "+    # than searchwindowsize is read as a single block, pexpect only\n", 
      "+    # searchs the last searchwindowsize characters missing anything\n", 
      "+    # before it.\n", 
      "+    #\n", 
      "+    # See: https://github.com/pexpect/pexpect/issues/203\n", 
      "+    domain.logger.info(\"waiting %d seconds for domain to start (%s)\", timeout, expected)\n", 
      "-    console.expect(expected, timeout=timeout,\n", 
      "-                   searchwindowsize=(len(expected)*4))\n", 
      "+    console.expect_exact(expected, timeout=timeout)\n", 
      "+\n", 
      "-    domain.logger.info(\"login timeouts: %s seconds for login prompt; %s seconds for password prompt; %s seconds for shell prompt\",\n", 
      "+    domain.logger.info(\"waiting %s seconds for login prompt; %s seconds for password prompt; %s seconds for shell prompt\",\n", 
      "-    # Heuristic for figuring out the search window size.  Assume, in\n", 
      "-    # the worst case, the other end contains the entire current\n", 
      "-    # directory in the prompt.  The number is then \"doubled, and then\n", 
      "-    # doubled again\".\n", 
      "-    searchwindowsize = max(100, (len(os.getcwd()) + len(console.prompt.pattern) * 4))\n", 
      "-    domain.logger.debug(\"using search window size of %s\", searchwindowsize)\n", 
      "-\n", 
      "-    if console.expect([\"login: \", console.prompt], timeout=login_timeout,\n", 
      "-                      searchwindowsize=searchwindowsize):\n", 
      "+    if console.expect([\"login: \", console.prompt], timeout=login_timeout):\n", 
      "-    if console.expect([\"Password: \", console.prompt], timeout=password_timeout,\n", 
      "-                      searchwindowsize=searchwindowsize):\n", 
      "+    if console.expect([\"Password: \", console.prompt], timeout=password_timeout):\n", 
      "+\n", 
      "+\n", 
      "+\n", 
      "+\n", 
      "+\n", 
      "-        domain.destroy()\n", 
      "+        # On F23 the domain sometimes becomes wedged in the PAUSED\n", 
      "+        # state.  When it does, give it a full reset.\n", 
      "+        if domain.state() == virsh.STATE.PAUSED:\n", 
      "+            domain.destroy()\n", 
      "+        else:\n", 
      "+            domain.shutdown()\n", 
      "+\n"
    ]
counter = 0
LENGTHOFCHANGES = 0

print "=========================================================="

while len(changes) != 0 and len(changes) != 1:
	diff1 = []
	diff2 = []
	close = []
	least = 2000
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


