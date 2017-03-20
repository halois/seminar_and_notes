#!/usr/bin/python
# -*- coding: UTF-8-*-

import math


p = 2 #input("请输入一个素数p:")
# 变成一个数组
truncOrd = [2,2] #input("请输入truncated次数n:")
aRange = 5 #input("请输入alpha1,2的最大范围:")

print("素数p为:",p)
print("截断次数n为:",truncOrd)
print('\n')
# 创建一个列表，用来放((\alpha_1,\alpha_2),i)
# 要改
LambdaList = [((x,y,z),1) for x in range(1,aRange) for y in range(aRange)]+[((x,y,z),2) for x in range(1,aRange) for y in range(1,aRange)]
# print(LambdaList)	
print("alpha", "\t|", "[alpha,1]".center(2),"\t&", "[alpha,2]".center(2), "\t|","[alpha]")
for item in LambdaList:
	i = item[1] # item中第二个是i
	alpha = item[0]
	x = item[0][0]
	y = item[0][1]
	z = item[0][2]
	if i == 1:
		 alphaComma1 = math.ceil( (truncOrd + 1)/x )  ＃要改

		alphaComma2 = '无'
		if (alpha,2) in LambdaList:
			alphaComma2 = math.ceil(truncOrd / x) ＃要改



		if x%p == 0 and y%p != 0: # alpha=(rp,alpha_2)情形 alpha_2不能被p整除
			bracketAlpha = alphaComma2 #[alpha]=[alpha,2]
		if x%p != 0 and y%p == 0: # alpha=(alpha_1,sp)情形 alpha_1不能被p整除
			bracketAlpha = alphaComma1 #[alpha]=[alpha,1]
		if x%p != 0 and y%p != 0 :
			bracketAlpha = max(alphaComma1,alphaComma2)
		if x%p == 0 and y%p == 0 :
			bracketAlpha = '无定义'

		print(alpha, "\t|\t", alphaComma1, "\t&\t", alphaComma2, "\t|\t", bracketAlpha)
	# elif i == 2:
	# 	alphaComma2 = math.ceil(truncOrd / x)
	# 	print(item,"\t|",alphaComma2)
