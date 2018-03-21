def is_credit_card_valid(number):
	number_as_list=list(str(number))
	rev=number_as_list[::-1]
	mystr=[]
	sums=0
	if len(rev)%2==0:
		return False
	for i in range(0,len(rev),+2):
		mystr.append(rev[i])
	for i in range(1,len(rev),2):
		digit=int(rev[i])
		digit*=2
		sub=list(str(digit))
		for i in sub:
			mystr.append(i)
	
	for i in mystr:
		sums+=int(i)
	print(sums)
	if sums % 10 ==0:
		return True
	return False
print(is_credit_card_valid(79927398713))
		