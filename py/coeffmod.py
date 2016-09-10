# coding=utf-8
# 一个较完整的程序，
# 实现键盘输入一个多项式，
# 输入它最多要自乘的次数n，
# 输入展开到的次数t，
# 输出每次幂次展开后的多项式，
# 	除首项1以外的系数，
# 	截断到t的系数，
# 	mod p之后的系数
# 	判定多少次之后是0000，输出最小的次数，
from sympy import *


# 定义函数
def totalcoeff(polyexpand):  # 多项式展开后的系数，去掉首项系数后，按从低次到高次排序
    totalcoefflist = [polyexpand.coeff(x, i) for i in range(1, degree(polyexpand) + 1)]
    return totalcoefflist


def truncoeff(polyexpand, n):  # 多项式展开后的系数，去掉首项系数后，按从低次到高次排序，n次及n次以上的都忽略
    truncoefflist = [polyexpand.coeff(x, i) for i in range(1, n)]
    return truncoefflist


def truncoeffmodp(polyexpand, n, p):  # truncoeff(polyexpand,n) mod p 之后的系数
    trunclist = truncoeff(polyexpand, n)
    trunmodlist = [i % p for i in trunclist]
    return trunmodlist


init_printing(use_unicode=True)  # 为了使表达式美观
x = Symbol('x')
fp = input("输入基本多项式即括号内的多项式:")  # 输入基本多项式 即括号内的多项式
n = int(input("输入最多要自乘的次数n:"))  # 输入最多要自乘的次数n
t = int(input("输入展开到的次数t,t次及以上的项将忽略:"))  # 输入展开到的次数t,t次及以上的项忽略
p = int(input("输入模掉的素数p:"))  # mod p的素数p

fundpoly = sympify(fp)

polyn = [fundpoly ** i for i in range(1, n + 1)]

polyexpand = [expand(j) for j in polyn]  # 每次幂次展开后的多项式

polytotalcoeff = [totalcoeff(i) for i in polyexpand]  # 除首项1以外的系数

polytruncoeff = [truncoeff(i, t) for i in polyexpand]  # 截断到t的系数

polytruncoeffmodp = [truncoeffmodp(i, t, p) for i in polyexpand]  # mod p之后的系数
poly_new = [1 + sum(x ** (j + 1) * polytruncoeffmodp[i][j] for j in range(t - 1)) for i in range(n)]

print("展开后的多项式为: ", polyexpand)
print("除首项1以外的系数: ", polytotalcoeff)
print("截断到t的系数: ", polytruncoeff)
print("截断后mod p之后的系数: ", polytruncoeffmodp)
print("多项式的在mod p下的n次方为:", poly_new)
for i in poly_new:
    print(list.index(poly_new, i) + 1, "次方：", i, ", LaTeX表达式为", "$", latex(i), "$")
