import numpy as np
import matplotlib.pyplot as plt

# 数据集，相同索引x,y为一个样本
x_data = [1.0, 2.0, 3.0]
y_data = [2.0, 4.0, 6.0]

# 模型的前馈，线性方程 y = x·w
def forward(x): 
    return x * w

# 损失计算
def loss(x, y):
    y_pred = forward(x) # 根据前馈求y_pred
    return (y_pred - y) * (y_pred - y)

w_list = [] # 权重
mse_list = [] # 权重对应的损失
for w in np.arange(0.0, 4.1, 0.1): # 穷举w
    print('w=', w)
    l_sum = 0

    # 从x_data，y_data去除x_val,y_val
    for x_val, y_val in zip(x_data, y_data):
        y_pred_val = forward(x_val)
        loss_val = loss(x_val, y_val)
        l_sum += loss_val
        print('\t', x_val, y_val, y_pred_val, loss_val)
    print('MSE=', l_sum / 3)
    w_list.append(w) 
    mse_list.append(l_sum / 3)
    
# 画图
plt.plot(w_list,mse_list)
plt.ylabel('Loss')
plt.xlabel('w')
plt.show()

