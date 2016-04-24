dividendList = []

for denominator in range(10,100):
	for numerator in range(10,100):

		if numerator >= denominator:
			continue

		preDividend = numerator / denominator

		if str(numerator)[0] in str(denominator):
			cancelledNum = str(numerator).replace(str(numerator)[0], "", 1)
			cancelledDen = str(denominator).replace(str(numerator)[0], "", 1)
			
			postDividend = int(cancelledNum) / int(cancelledDen) 
			
			if preDividend == postDividend:
				dividendList.append(int(cancelledNum))
				dividendList.append(int(cancelledDen))
				
		elif str(numerator)[1] in str(denominator):
			if str(numerator)[1] != '0':
				cancelledNum = str(numerator).replace(str(numerator)[1], "", 1)
				cancelledDen = str(denominator).replace(str(numerator)[1], "", 1)
				
				postDividend = int(cancelledNum) / int(cancelledDen)
				
				if preDividend == postDividend:
					dividendList.append(int(cancelledNum))
					dividendList.append(int(cancelledDen))

for dividend in dividendList:
	print dividend
