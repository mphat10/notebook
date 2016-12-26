def monthlypayment(mortage, term, rate):
	mrate=rate/12
	mortage= mortage+ mrate*0.01*mortage
	sumx= mortage
	monthlypayment= sumx/term
	return monthlypayment

mortage =float(raw_input('so tien vay >>>'))
term =float(raw_input('thoi gian vay bao nhieu thang>>>'))
rate = float(raw_input('lai suat % moi nam>>>'))
print ('monthly payment: ', monthlypayment(mortage,term,rate) )