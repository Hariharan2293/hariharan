if (__name__=='__main__'):
	T= int(input())
	E = list(map,int,input(),split())
	L= list(map,int,input(),split())
	currentpresence = 0
	maxpresence = 0 
	for i in range(T):
		currentpresence +=E[i]-L[i]
	if (maxpresence < currentpresence):

		maxpresence =currentpresence
		print (maxpresence, end = '')