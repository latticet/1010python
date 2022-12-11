"""
 新建一个文件，定义一个计算类,有两个属性,数字1,数字2,具有 加 减 乘 除 方法
"""


class Calc:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def dec(self):
        return self.num1 - self.num2


calc = Calc(2, 1)
print(calc.add())
print(calc.dec())
