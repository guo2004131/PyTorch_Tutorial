from __future__ import print_function
import torch

# Tensors are similar to numpy's ndarrays, with the addition being that
# Tensors can also be used on a GPU to accelerate computing
x = torch.Tensor(5, 3)
print ("just the tensor ", x)

# construct a randomly intilized matrix
x = torch.rand(5, 3)
print ("x is", x)

print("size of x is ", x.size())

y = torch.rand(5, 3)
print ("y is ", y)
print ("sum of x and y is ", x+y)
print ("torch add x and y is ", torch.add(x, y))

# giving an output tensor
result = torch.Tensor(5, 3)
torch.add(x, y, out=result)
print ("torch add return ", result)
