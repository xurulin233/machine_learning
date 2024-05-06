import torch
class A():
    def __call__(self,param):
        print('I can be called like a function')
        print('传入参数的类型是：{}   值为： {}'.format(type(param), param))
        res = self.forward(param)
        return res

    def forward(self , input_):
        print('in  forward, 传入参数类型是：{}  值为: {}'.format( type(input_), input_))
        return input_

a = A()

input_param = a('i')
print("对象a传入的参数是：", input_param)
