import matplotlib.pyplot as plt  # 导入matplotlib库画图
import numpy as np  # 导入numpy库产生数据

x = np.linspace(-3, 3, 50)  # 生成-1到1的50等分数据为横坐标
y1 = 2 * x + 1  # 写出y1的函数
y2 = x ** 2  # 写出y2的函数
plt.figure(1)
plt.plot(x, y1)  # 以x为横坐标，y1为纵坐标画图
plt.plot(x, y2)  # 以x为横坐标，y2为纵坐标画图
plt.figure(2, figsize=(8, 5))  # 给图像序号和大小设置长为8宽为5
plt.plot(x, y1, color='r', linewidth=1.0, linestyle='-.')
"""以x为横坐标，y1为纵坐标画图,设置线的颜色红色,线宽1.0,线的类型虚线"""
plt.plot(x, y2)  # 以x为横坐标，y2为纵坐标画图
plt.show()  # 将画的图显示出来，必不可少
