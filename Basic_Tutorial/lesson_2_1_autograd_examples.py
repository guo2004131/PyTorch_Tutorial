"""
Every "Variable" has two flags: "requires_grad" and "volatile". they both allow for ine grained exclusion of sub-graphs
from gradient computation and can increase efficiency.

(1) "require_grad": if there's a single input to an operation that requires gradient, its output will also require
gradient. Conversely, only if all inputs don't require gradient, the output also won't require it. Backward computation
is never performed in the sub-graphs, where all "Variables" didn't require gradients.

(2) "volatile": it is recommended for purely inference mode, when you're sure you won't be even calling ".backward()".
It's more efficient than any other auto-grad setting - it will use the absolute minimal amount of memory to
evaluate the model. "volatile" also determines that "requires_grad = False". Volatile differes from "requires_grad" in
how the flag propagates. If there's even a single volatile input to an operation, its output is also going to be
volatile. Volatility spreads a cross the grpah much easier than non-requiring gradient - you only need a single volatile
leaf to have a volatile output, while you need all leaves to not require gradient to have an output that doesn't require
gradient. Using volatile flag you don't need to change any settings of your model parameters to sue it for inference.
It's enough to create a volatile input, and this will ensure taht no intermediate states are saved.
"""

import torch
import torchvision
from torch.autograd import Variable
from torch import nn
from torch import optim

x = Variable(torch.randn(5, 5))
y = Variable(torch.randn(5, 5))
z = Variable(torch.randn(5, 5), requires_grad=True)
a = x+y
print ("Parameter a is the sum of x and y, which does not necessarily require grad: %r" % a.requires_grad)
b = a + z
print ("Parameter b is the sum of a and z, which requires grad: %r" % b.requires_grad)

# This is especially useful when you want to freeze part of your model, or you know in advance that you're not going
# to use gradients w.r.t some parameters. For example if you want to finetune a pretrained CNN, it's enough to switch
# the "requires_grad" flags in the frozen base, and no intermediate buffers will be saved, until the computation gets to
# the last layer, where the affine transform will use weights that require gradient, and the output of the network will
# also require them.

model = torchvision.models.resnet18(pretrained=True)
for param in model.parameters():
    param.requires_grad = False

# Replace the last fully-connected layer
# Parameters of newly constructed modules have requires_grad=True by default
model.fc = nn.Linear(512, 100)
optimizer = optim.SGD(model.fc.parameters(), lr=1e-2, momentum=0.9)

regular_input = Variable(torch.randn(1, 3, 227, 227))
volatile_input = Variable(torch.randn(1, 3, 227, 227), volatile=True)
model = torchvision.models.resnet18(pretrained=True)
print(model(regular_input).requires_grad)
print(model(volatile_input).requires_grad)
print(model(volatile_input).volatile)
print(model(volatile_input).grad_fn is None)
