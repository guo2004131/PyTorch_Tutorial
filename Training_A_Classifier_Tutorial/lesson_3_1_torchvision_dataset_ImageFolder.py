from torchvision import datasets, models, transforms
import torch
import os


data_transforms = {
    'train': transforms.Compose([
        transforms.RandomSizedCrop(224),
        transforms.RandomHorizontalFlip(),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
    'val': transforms.Compose([
        transforms.Scale(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ]),
}

# To define the data folder
data_dir = 'hymenoptera_data'
# "dsets" is dictionary type. Each "x" in ['train', 'val'] are listed as keys in the dictionary
# Note that the data_transform is also a dict type variable.
dsets = {x: datasets.ImageFolder(os.path.join(data_dir, x), data_transforms[x]) for x in ['train', 'val']}

# "dset_loaders" uses "torch.utils.data.Dataloader" function, which sets the batch_size.
# "dset_loaders" is used to feed the neural network.
# Note that the loader here only processed "file names" not loading it into the CPU memory/GPU memory
dset_loaders = {x: torch.utils.data.DataLoader(dsets[x], batch_size=4, shuffle=True, num_workers=4)
                for x in ['train', 'val']}
