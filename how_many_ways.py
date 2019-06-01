def how_many_ways(digitarray):
	a=str(digitarray)
	b=list(a)
	c=0
	for i in range(len(b)-1):
		if b[i] == '1' or b[i] == '2' and b[i+1] <= '6':
			c = c+1
	print 2**(len(b))+2**(len(b)-1)*c

how_many_ways(268)
how_many_ways(219)
how_many_ways(21925)