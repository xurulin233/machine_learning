from sklearn import linear_model
import numpy as np
x = np.array([[0, 2], [1, 1], [2,3],[3,2],[4,5],[5,2]]) 
y = np.array([8,7,15,14,25,18])
xt = np.insert(x, x.shape[1], 1, axis=1)
w = np.linalg.inv(xt.T@xt)@xt.T@y
print("模型参数W："+str(w))
