import torch
import numpy as np
from torch.distributions import Categorical, kl
from torch.nn import CrossEntropyLoss

# Cross entropy loss
p = [1, 2, 3, 4]
q = [1] # [0, 1, 0, 0] = torch.nn.functional.one_hot(torch.tensor(q), len(p))

celoss = -p[q[0]] + np.log(sum([np.exp(i) for i in p]))
print (f"Cross Entropy Loss: {celoss}")

loss = CrossEntropyLoss()
tensor_p = torch.FloatTensor(p).unsqueeze(0)
tensor_q = torch.tensor(q)
output = loss(tensor_p, tensor_q)
print (f"Torch Cross Entropy Loss: {output.item()}")
