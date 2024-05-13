import matplotlib.pyplot as plt  # 导入matplotlib库画图
import numpy as np  # 导入numpy库产生数据

x = np.linspace(-3, 3, 50)  # 生成-1到1的50等分数据为横坐标
y1 = 2 * x + 1  # 写出y1的函数
y2 = x ** 2  # 写出y2的函数
plt.figure(1, figsize=(8, 5))  # 给图像序号和大小设置长为8宽为5
plt.plot(x, y1, color='red', linewidth=1.0, linestyle='--')
"""以x为横坐标，y1为纵坐标画图,设置线的颜色红色,线宽1.0,线的类型虚线"""
plt.plot(x, y2)  # 以x为横坐标，y2为纵坐标画图
plt.xlim((-1, 3))  # 设置x坐标的范围是-1到3
plt.ylim((-2, 8))  # 设置y坐标的范围是-2到8
plt.xlabel('I am x')  # 设置横坐标
plt.ylabel('I am y')  # 设置纵坐标
new_ticks = np.linspace(-1, 3, 5)
print(new_ticks)
plt.xticks(new_ticks)  # 设置横坐标为-1到3分为5个标记
plt.yticks([-2, 1, 4, 6, 8], [r'$really\ bad$', r'$bad\ \alpha$', r'$common$', r'$good$', r'$very\ good$'])
# 将纵坐标分成5种图标
plt.show()  # 将画的图显示出来，必不可少




