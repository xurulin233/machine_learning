import matplotlib.pyplot as plt  # 导入matplotlib库画图
import numpy as np  # 导入numpy库产生数据

x = np.linspace(-1, 1, 50)  # 生成-1到1的50等分数据为横坐标
y1 = 2 * x + 1  # 写出y的函数
y2 = x ** 2  # 写出y的函数
plt.figure(1)
plt.plot(x, y1)  # 以x为横坐标，y1为纵坐标画图
plt.plot(x, y2)  # 以x为横坐标，y2为纵坐标画图
plt.show()  # 将画的图显示出来，必不可少
