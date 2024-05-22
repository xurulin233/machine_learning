import torch
import numpy as np
from torch.distributions import Categorical, kl

# Entropy
p = [0.1, 0.2, 0.3, 0.4]

Hp = -sum([p[i] * np.log(p[i]) for i in range(len(p))])
print (f"H(p) = {Hp}")
dist_p = Categorical(torch.tensor(p))
print (f"Torch H(p) = {dist_p.entropy().item()}")
