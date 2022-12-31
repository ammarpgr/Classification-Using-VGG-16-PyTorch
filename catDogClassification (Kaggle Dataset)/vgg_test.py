import torch
import torch.nn as nn
import torch.nn.functional as F
import torchvision
import torchvision.transforms as transforms
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Hyper-Paramerters
train_split = 0
test_split = 0
learning_rate = 0.001
num_epochs = 0
batch_size = 4


# images
input_channel = 3
classes = ('cat', 'dog')

transforms = transforms.Compose([
                    transforms.Resize(size = (224,224)),
                    transforms.ToTensor(),
                    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
                ])

train_data = torchvision.datasets.ImageFolder('./data/catDogDataset/train', transform = transforms)
test_data = torchvision.datasets.ImageFolder('./data/catDogDataset/test', transform = transforms)

train_loader = torch.utils.data.DataLoader(train_data, batch_size = batch_size, shuffle = True)
test_loader = torch.utils.data.DataLoader(test_data, batch_size = batch_size)


detailer = iter(train_loader)
images, labels = detailer.next()
print(type(images))

# conv1 = nn.Conv2d(3, 24, 5, 2, 4)
# pool = nn.MaxPool2d(2, 2)
# conv2 = nn.Conv2d(24, 48, 5, 2, 4)
# conv3 = nn.Conv2d(48, 96, 5, 2, 4)

conv1_1 = nn.Conv2d(3, 64, 3, padding='same')
conv1 = nn.Conv2d(64, 64, 3, padding='same')

pool = nn.MaxPool2d(2, 2)

conv2_1 = nn.Conv2d(64, 128, 3, padding='same')
conv2 = nn.Conv2d(128, 128, 3, padding='same')

conv3_1 = nn.Conv2d(128, 256, 3, padding='same')
conv3_2 = nn.Conv2d(256, 256, 3, padding='same')
conv3 = nn.Conv2d(256, 256, 3, padding='same')

conv4_1 = nn.Conv2d(256, 512, 3, padding='same')
conv4_2 = nn.Conv2d(512, 512, 3, padding='same')
conv4 = nn.Conv2d(512, 512, 3, padding='same')

conv5 = nn.Conv2d(512, 512, 3, padding='same')
# fc1 = nn.Linear(7*7*512, 4096)
# fc2 = nn.Linear(4096, 1000)
# fc3 = nn.Linear(1000, 2)

print(images.shape)


x = F.relu(conv1_1(images))
x = F.relu(conv1(x))
print("Images: ", x.shape)
x = pool(x)
print("---> Pool: ", x.shape)

x = F.relu(conv2_1(x))
x = F.relu(conv2(x))
print("Images: ", x.shape)
x = pool(x)
print("---> Pool: ", x.shape)

x = F.relu(conv3_1(x))
x = F.relu(conv3_2(x))
x = F.relu(conv3(x))
print("Images: ", x.shape)
x = pool(x)
print("---> Pool: ", x.shape)


x = F.relu(conv4_1(x))
x = F.relu(conv4_2(x))
x = F.relu(conv4(x))
print("Images: ", x.shape)
x = pool(x)
print("---> Pool: ", x.shape)

x = F.relu(conv5(x))
x = F.relu(conv5(x))
x = F.relu(conv5(x))
print("Images: ", x.shape)
x = pool(x)
print("---> Pool: ", x.shape)
