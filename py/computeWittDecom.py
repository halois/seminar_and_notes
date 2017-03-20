# coding=utf-8
import math

print("BigWitt_n(F_q)=1+xF_q[x]/(x^{n+1})")
n = int(input("请输入n:"))
p = int(input("请输入一个素数，即F_q的特征:"))
f = int(input("请输入F_q在F_p上的次数:"))

# 判断 a 与 b 是否互素 (Euclid's Algorithm)
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
# compute p-typical witt vectors W_l(F_{p^f})=
def witt(l,p,f):
	q = int(pow(p,l))
	if f == 1:
		return "Z/"+str(q)+"Z"
	else:
		return "(Z/"+str(q)+"Z)^"+str(f)

def ell(m,n,p):
	result = 1 + int(math.floor(math.log(n/m, p)))
	return result

def bigWitt(n,p,f):
	l = ell(1,n,p)
	result =  witt(l,p,f)
	for m in range(2,n+1):
		if gcd(m,p) == 1:
			l = ell(m,n,p)
			result += "+"+ witt(l,p,f) 
	return result

q = int(pow(p,f))
print("bigWitt_"+str(n)+"(F_" +str(q)+ ") = " +  bigWitt(n,p,f))
