import torch
import numpy as np
from torch.distributions import Categorical, kl

# KL divergence
p = [0.1, 0.2, 0.3, 0.4]
q = [0.1, 0.1, 0.7, 0.1]

Dpq = sum([p[i] * np.log(p[i] / q[i]) for i in range(len(p))])
print (f"D(p, q) = {Dpq}")
dist_p = Categorical(torch.tensor(p))
dist_q = Categorical(torch.tensor(q))
print (f"Torch D(p, q) = {kl.kl_divergence(dist_p, dist_q)}")
