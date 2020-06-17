def namer(inp):
	
		numstr = str(inp)
		numstr.lstrip('0')

		suffix = ['' , 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion', 'septillion', 'octillion', 'nonillion', 'decillion']
	
		singledigits = ['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]

		teen = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

		ty = ['','','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

		m = len(numstr) % 3
		if m == 1:
			numstr = '00' + numstr
		elif m == 2:
			numstr = '0' + numstr

		newlen = len(numstr)/3
	
		tripletlist =[]

		for i in range(int(newlen)):
			k = numstr[3*i:3*i +3]
			tripletlist.append(k)


		def digitname(n):
			return singledigits[n]
	
		def hundreds(a):
			if a == 0:
				return ""
			else:
				return digitname(a)+' '+ 'hundred '

		def doublet(b,c):
			if b == 0:
				return digitname(c)
			elif b == 1:
				return teen[c]
			else:
				op_b = ty[b]		
				op_c = digitname(c)
				return op_b + ' ' + op_c
		

		def trp(trip):
			a = trip[0]
			b = trip[1]
			c = trip[2]
			op_a = hundreds(int(a))
			op_bc = doublet(int(b),int(c))
			return op_a +op_bc
	
		nom =''
	
		for i in range(int(newlen)):
			k = tripletlist[i]
			nom += (trp(k)+' ' + suffix[int(newlen) - i -1] + ' ')	

		return nom

def namelength(s):
	k = namer(s)
	nomlen = len(k) - k.count(' ')
	return nomlen


import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0,10**3,10**3-1)

y = namelength(x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


plt.plot(x,y, 'r')

plt.show()
