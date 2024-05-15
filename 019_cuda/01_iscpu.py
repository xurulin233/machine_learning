import torch
import torch.nn as nn
 
# ----------- 判断模型是在CPU还是GPU上 ----------------------
 
model = nn.LSTM(input_size=10, hidden_size=4, num_layers=1, batch_first=True)
print(next(model.parameters()).device)  # 输出：cpu
 
# ----------- 判断数据是在CPU还是GPU上 ----------------------
 
data = torch.ones([2, 3])
print(data.device)  # 输出：cpu
 
