import torch.nn as nn
import torch.nn.functional as F


# the base class for all neural network modules.
# Modules can also contain other Modules, allowing to nest them in a tree structure.
# You can assign the submodules as regular attributes:
class Model(nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.conv1 = nn.Conv2d(1, 20, 5)
        self.conv2 = nn.Conv2d(20, 20, 5)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        return F.relu(self.conv2(x))


# To use function "apply" to initilize the parameters of a model.
def init_weights(m):
    print (m)
    if type(m) == nn.Linear:
        m.weight.data.fill_(1.0)
        print (m.weight)

net = nn.Sequential(nn.Linear(2, 2), nn.Linear(2, 2))
net.apply(init_weights)


