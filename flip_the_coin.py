import random as rd
def flipping(time):
	for x in xrange(0,int(time)):
		rn=rd.random()

		pass
	if rn>0.5:
		kq ='mat ngua'
	else:
		kq='mat sap'

	return kq


time= raw_input('so lan tung dong xu  >>')

print ('ket qua la: ', flipping(time))