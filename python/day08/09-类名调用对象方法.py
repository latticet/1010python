class Demo:
    def info(self):
        print('info')


d1 = Demo()
d1.info()

Demo.info(d1)  # 一般不用类调用
