# 创建类
class Foo:
     
    def Bar(self):
        print('Bar')
 
    def Hello(self, name):
        print('i am %s' %name)
 
# 根据类Foo创建对象obj
obj = Foo()
obj.Bar()            #执行Bar方法
obj.Hello('wupeiqi') #执行Hello方法　
