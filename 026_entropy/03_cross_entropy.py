import torch
import numpy as np
from torch.distributions import Categorical, kl

# Cross entropy
p = [0.1, 0.2, 0.3, 0.4]
q = [0.1, 0.1, 0.7, 0.1]

Hpq = -sum([p[i] * np.log(q[i]) for i in range(len(p))])
print (f"H(p, q) = {Hpq}")
