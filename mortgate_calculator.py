def periodlypayment(mortage, term, rate):
	if don_vi_tien == 2 :
		mortage*= 1000
	elif don_vi_tien==3:
		mortage*=1000000
	if interval == 1:
		term =term
	elif interval == 2:
		term *= 4
	else:
		term *= 30

	mrate=rate/12
	mortage= mortage+ mrate*0.01*mortage
	sumx= mortage
	periodlypayment= sumx/term
	return periodlypayment

def nap(val, mess):
	val=float(raw_input(mess))
	return val


don_vi_tien= float(raw_input('don vi tien te > 1: dollar, 2: nghin dong, 3: trieu dong >>'))
mortage =float(raw_input('so tien vay >>>'))
term =float(raw_input('thoi gian vay bao nhieu thang >>>'))
rate = float(raw_input('lai suat % moi nam>>>'))
interval = float(raw_input('chu ky tra no> 1: thang, 2: tuan, 3:ngay >>>'))
print ('so tien tra moi chu ky: ', periodlypayment(mortage,term,rate) )

