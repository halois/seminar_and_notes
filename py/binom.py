import operator
import math

def c(n,r): #定义组合数
	f = math.factorial
	return f(n) / f(r) / f(n-r)

def binom(n,a): # (1+ax)^n的系数 除去第一项 1
	binomlist = []
	for i in range(1,n+1):
		t = pow(a,i) * c(n,i)
		binomlist.append(t)
	return binomlist

def binomod(n,a,p): # (1+ax)^n的系数modp
	binomodlist = []
	oldlist = binom(n,a)
	for j in oldlist:
		binomodlist.append(j%p)
	return binomodlist

def findcyclic(n,a,p): # 将1+ax, (1+ax)^2,一直到(1+ax)^n的系数mod p后显示出来
	findcycliclist = []
	for i in range (1,n+1):
		t = binomod(i,a,p)
		findcycliclist.append(t)
	return findcycliclist

# 每一个系数列表，只显示到截断的长度

def findcyclic(n,a,p,trun): # 将1+ax, (1+ax)^2,一直到(1+ax)^n的系数mod p后显示出来 直到截断长度  如1+xA[x]/(x^5),trun = 5
	findcycliclist = []
	for i in range (1,n+1):
		t = binomod(i,a,p)[:trun-1]
		findcycliclist.append(t)
	return findcycliclist


##### 下面调用符号计算
from sympy import *
x = Symbol('x')
poly = (1+x+pow(x,3))**8  #输入多项式
polyexpand = expand(poly)  #展开多项式

def totalcoeff(polyexpand):  # 多项式展开后的系数，去掉首项系数后，按从低次到高次排序
	totalcoefflist = [polyexpand.coeff(x,i) for i in range(1,degree(polyexpand)+1)]
	return totalcoefflist

def truncoeff(polyexpand,n): # 多项式展开后的系数，去掉首项系数后，按从低次到高次排序，n次及n次以上的都忽略
	truncoefflist = [polyexpand.coeff(x,i) for i in range(1,n)]
	return truncoefflist

totallist = totalcoeff(polyexpand)

trunclist = truncoeff(polyexpand,5)


def truncoeffmodp(polyexpand,n,p):
	trunclist = truncoeff(polyexpand,n)
	trunmodlist = [i%p for i in trunclist]
	return trunmodlist


truncmodlist = truncoeffmodp(polyexpand,5,2)

