#!/usr/bin/python
# -*- coding: UTF-8-*-

import math


p = 7 #input("请输入一个素数p:")
truncOrd = 7 #input("请输入truncated次数n:")
aRange = 4 #input("请输入alpha1,2的最大范围:")

print("素数p为:", p, "\t", "截断次数n为:", truncOrd, "\n")


# 创建一个列表，用来放((\alpha_1,\alpha_2),i)
LambdaList = [((x,y),1) for x in range(1,6) for y in range(10)]+[((x,y),2) for x in range(1,6) for y in range(1,10)]




#计算[alpha]
def computeBracketAlpha(x,y): 
	if x%p == 0 and y%p != 0: # alpha=(rp,alpha_2)情形 alpha_2不能被p整除
		bracketAlpha = alphaComma2 #[alpha]=[alpha,2]
	if x%p != 0 and y%p == 0: # alpha=(alpha_1,sp)情形 alpha_1不能被p整除
		bracketAlpha = alphaComma1 #[alpha]=[alpha,1]
	if x%p != 0 and y%p != 0 :
		bracketAlpha = max(alphaComma1,alphaComma2)
	if x%p == 0 and y%p == 0 :
		bracketAlpha = '无定义'
	return bracketAlpha

def computeMin(): # 计算min{i|a_i%p !=0 and [a,i]=[a]} 
# 输入的是alpha_1,alpha_2
# alphaComma1,  alphaComma2分别是[a,1],[a,2]
# bracketAlpha 是[a]
# 
	if x%p !=0 and alphaComma1 == bracketAlpha:
		return 1
	elif x%p ==0 and y%p !=0 and alphaComma2 == bracketAlpha:
		return 2
	else:
		return "不存在"

# 判断 a 与 b 是否互素 (Euclid's Algorithm)
def gcd(a, b):
    while a != 0:
        a, b = b % a, a
    return b
# 定义一个函数来确定谁在lambda00中    
def isInLambda00():
	if computeMinValue == 1 and gcd(x,y) == 1 and y >= 1:
		result = "(" + str(alpha) + ", 2 ) = "+str(alphaComma2)
		return result
	elif computeMinValue == 2 and gcd(x,y) == 1:
		result = "(" + str(alpha) + ", 1 ) = " +str(alphaComma1)
		return result
	else :
		return "不在"

# ############主函数############ 

# print(LambdaList)	
print("alpha", "\t|", "[alpha,1]".center(2),"\t&", "[alpha,2]".center(2), "\t|","[alpha]", "\t|","min","\t|","谁在lambda00")
for item in LambdaList:
	i = item[1] # item[1]是i
	alpha = item[0]
	x,y = alpha[0],alpha[1]
	
	if i == 1:
		alphaComma1 = math.ceil( (truncOrd + 1)/x )
		alphaComma2 = '无'
		if (alpha,2) in LambdaList:
			alphaComma2 = math.ceil(truncOrd / x)
		bracketAlpha = computeBracketAlpha(x,y)
		computeMinValue = computeMin()
		inLambda00 = isInLambda00()
		print(alpha, "\t|\t", alphaComma1, "\t&\t", alphaComma2, "\t|\t", bracketAlpha,"\t|\t",computeMinValue,"\t|\t",inLambda00)
		



