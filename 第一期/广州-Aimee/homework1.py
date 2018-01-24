# coding = utf-8

__author__ = 'Aimee'

# 实现一个四则运算的类，要求实现任意两个数的加减乘除运算

class Calc:
    def __init__(self,a,b):  #初始化函数 参数定义，也可以不定义参数
        self.a = a
        self.b =b

    #加法
    def add(self):
        return self.a + self.b

    #减法
    def sub(self):
        return self.a - self.b

    #乘法
    def mul(self):
        return self.a * self.b

    #除法
    def div(self):
        if b !=0:
            return round(self.a /self.b, 4)

        else:
            print(" 除数为0，非法")

def test(calc):

    sum = calc.add()
    sub = calc.sub()
    mul = calc.mul()
    div = calc.div()

    print(sum,sub,mul,div)


if __name__ == "__main__":

    a = int( input('请输入第一个数：'))
    # 在Python3中raw_input和input 整合了不存在raw_input

    b = int(input('请输入第二个数：'))
    calc = Calc(a,b)
    test(calc)















