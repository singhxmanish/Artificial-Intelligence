# dot product opertor - @ in background python uses A.__matmul__(B).
# The computation is performed using highly optimized, low-level code (written in C++ and CUDA)

# elementwise multiplication - operator *

import numpy as np
import torch

print(' '*1)
print('-'*20)
## With torch
print('numpy Implementation')
print(f'numpy Version: {np.__version__}')
print('-'*20)
A = np.array([[1,2,3,4],[5,6,7,8]])
print(A)
B = np.array([[1,2],[3,4],[5,6],[7,8]])
print(B)

C = A @ B
print(C)

print(' '*1)
print('-'*20)
## With torch
print('Torch Implementation')
print(f'Torch Version: {torch.__version__}')
print('-'*20)
A1=torch.tensor([[1,2,3,4],[5,6,7,8]])
B2=torch.tensor([[1,2],[3,4],[5,6],[7,8]])
C=A1 @B2
print(C)


print(' '*1)
print('-'*20)

print('element wise multipliation. This require A3 and B3 to be os same dimeanion')
print(' '*1)
print('-'*20)

A3 = torch.tensor([[1,2,3,4],[5,6,7,8]])
B3 = torch.tensor([[2,2,2,2],[2,2,2,2]])
M = A3*B3
print(M)
print(' '*1)
print('-'*20)
