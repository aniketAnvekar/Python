#factorial using recursion'
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)


#Factorial using basic loops
def factorial(n):
	if n==0:
		return 1
	else:
		c=1
		sum=n
		while(c<n):
			sum*=(n-1)
			c+=1
		return sum
