import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *
# 解决图像无法现实中文问题
mpl.rcParams['font.sans-serif'] = ['SimHei'] 

#这里设模型函数为y=2x+2
x_data = [1.0,2.0,3.0]
y_data = [4.0,6.0,8.0]

# 定义模型
def forward(x):
    return x * w + b

# 定义损失函数
def loss(x,y):
    y_pred = forward(x)
    return (y_pred-y)*(y_pred-y)

mse_list = []
W=np.arange(0.0,4.1,0.1)
B=np.arange(0.0,4.1,0.1)
w,b=np.meshgrid(W,B)

l_sum = 0
for x_val, y_val in zip(x_data, y_data):
    y_pred_val = forward(x_val)
    loss_val = loss(x_val, y_val)
    print('x_val==', x_val,'\ny_val==', y_val,'\ny_pred_val==', y_pred_val, '\nloss_val==',loss_val)
    # 计算同一个w和b下的loss总和
    l_sum += loss_val

# 查找loss最低的w，b取值
target = {'loss': float('inf'), 'w':0, 'b':0}
for i in range(l_sum.shape[0]):
    for j in range(l_sum.shape[1]):
       if l_sum[i][j] < target['loss']:
            target['loss'] = l_sum[i][j]
            target['w'] = w[i][j]
            target['b'] = b[i][j]

print('target linear model is y = %.2f * x + %.2f' % (target['w'], target['b']))

# 定义三维坐标轴
fig = plt.figure()
#ax = Axes3D(fig,auto_add_to_figure=False)
ax = Axes3D(fig)
fig.add_axes(ax)
# 作图
ax.plot_surface(w, b, l_sum/3,rstride=1,cstride=1,cmap=plt.cm.coolwarm) #rstride:行之间的跨度；cstride:列之间的跨度；cmap:颜色映射表
ax.set_xlabel("权重 W")
ax.set_ylabel("偏置项 B")
ax.set_zlabel("损失值")
plt.show()


