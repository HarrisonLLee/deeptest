# _*_ coding : utf-8 _*_
__author__ = "Jason"
'''
Python支持三种不同类型的数值类型：
1.整型（int）
    通常称为整型或整数，为整数或者负数或者0，不带小数点。
    在Python3中，整型没有限制大小，即亦可作long类型使用，所以在Python3中无显性的long类型。
2.浮点型（float）
    即带小数点的数值，也可以用科学计数法表示：
3.复数（complex）
    由实数部分和虚数部分构成，表达式方式为：a + bj 或complex(a,b)，
    其中a为实数部分，b为虚数部分。
'''
#导入模块时需注意模块内部函数名是否重复
#比如math和cmath模块均有sqrt()函数，如果用“from 模块 import 函数”模式，则不能使用函数了。
import cmath
#负数取平方根，需使用cmath复数模块，结果为1j
print(cmath.sqrt(-1))
'''
复数的运算法则：
假设z1=a+bj，z2=c+dj
加法：z1+z2 = (a+c)+(b+d)j
减法：z1+z2 = (a-c)+(b-d)j
乘法：z1*z2 = (ac-bd)+(bc+ad)j
除法：z1/z2 = ((ac+bd)/(c^2+d^2))+((bc-ad)/(c^2+d^2))j
'''
a,b = 3+4j,5+6j
print(a+b)
print(a-b)
print(a*b)#结果是(3*5-4*6)+(4*5+3*6)j = (15-24)+(20+18)j = -9+38j
print(a/b)#结果是((3*5+4*6)/(5^2+6^2))+((4*5-3*6)/(5^2+6^2))j =(39/61)+(2/61)j

'''
常用数值函数：
1.数学函数
    主要进行各种数学计算，例如计算计算绝对值、幂运算、平方根等等，主要定义在math模块中。
2.随机数函数
    主要用于随机数的处理，主要定义在random模块中。
3.三角函数
    主要用于将数值转换为对应的三角弧度值，主要定义在math模块中。
4.数学常量
    Python中内置定义的数学常量，比如π。
注意：math模块返回的是非复数类型，cmath模块返回的是复数类型。

类型转换函数：
函数                返回值（描述）
int(x)              将x转换为一个整数。
float(x)            将x转换到一个浮点数。
complex(x)          将x转换到一个复数，实数部分为 x，虚数部分为 0。
complex(x, y)       将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。

数学函数：
函数	            返回值 ( 描述 )
abs(x)	            返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	            返回数字的上入整数，如math.ceil(4.1) 返回 5
cmp(x, y)           如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。 Python 3 已废弃 。使用 使用 (x>y)-(x<y) 替换。
exp(x)	            返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	            返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	        返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	            如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	        返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	    返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	    返回给定参数的最小值，参数可以为序列。
modf(x)	            返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	        x**y 运算后的值。
round(x [,n])	    返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	            返回数字x的平方根。

随机数函数：
函数	                            描述
choice(seq)	        从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1
random()	        随机生成下一个实数，它在[0,1)范围内。
seed([x])	        改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	    将序列的所有元素随机排序
uniform(x, y)       随机生成下一个实数，它在[x,y]范围内。

三角函数：
函数	            描述
acos(x)	            返回x的反余弦弧度值。
asin(x)	            返回x的反正弦弧度值。	
atan(x)	            返回x的反正切弧度值。
atan2(y, x)	        返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	            返回x的弧度的余弦值。
hypot(x, y)	        返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	            返回的x弧度的正弦值。
tan(x)	            返回x弧度的正切值。
degrees(x)	        将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	        将角度转换为弧度

数学常量：
常量	            描述
pi	                数学常量 pi（圆周率，一般以π来表示）
e	                数学常量 e，e即自然常数（自然常数）。
'''
'''
Python需注意round函数：
小数位大于0.5时，均进一位；
小数位等于0.5时，则依整数位，“奇进偶不进”；
小数位小于0.5时，则均不进。
'''
print(round(10.4))#结果为10
print(round(10.5))#结果为10
print(round(10.6))#结果为11
print()
print(round(11.4))#结果为11
print(round(11.5))#结果为12
print(round(11.6))#结果为12

#接着测试round函数
print()
print(round(10.49))#结果为10
print(round(10.50))#结果为10
print(round(10.51))#结果为11
print()
print(round(11.49))#结果为11
print(round(11.50))#结果为12
print(round(11.51))#结果为12

'''
补充另外一点，random.randint和random.sample
randint是在指定范围随机抽选一个整数；
sample是在指定序列截取片段
'''
import random
print(random.randint(1,100))
a = 'abcdefg'
lst = random.sample(a,3)#从a里截取3个片段
str = ''.join(lst)
print(lst)#随机结果之一为['d','e','g']
print(str)#随机结果之一为deg
