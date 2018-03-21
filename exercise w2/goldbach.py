def primes(n):
    out = list()
    for num in range (2, n + 1): 
        prime = True
        for i in range(2, num):
            if (num % i == 0):
                prime = False
        if prime:
            out.append(num)
    return out
def goldbach(n):
	l1=primes(n)
	l2=l1[::-1]
	out=[]
	l3=set()
	for i in l1:
		for j in l2:
			iflag= i in l3
			jflag = j in l3
			if i+j==n and iflag==False and jflag==False:
				tup=(i,j)
				out.append(tup)
				l3.add(i)
				l3.add(j)
	return out

b=goldbach(100)
print(b)