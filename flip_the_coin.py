import random as rd
def flipping(time):
	ngua=0
	sap=0
	for x in xrange(0,int(time)):
		rn=rd.random()

		if rn>0.5:
			ngua+=1
		else:
			sap+=1
		

	return sap, ngua


time= raw_input('so lan tung dong xu  >>')

print ('ket qua sap/ ngua la: ', flipping(time))