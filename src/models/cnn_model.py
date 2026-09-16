"""
# File: cnn_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable CNN (1D Convolutional networks) modules for the AI pipeline.
"""

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
import torchvision
import torchvision.transforms as transforms

batch_size = 64
num_classes = 10
learning_rate = 0.001
num_epochs = 20

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

"INPUTS X_train_3d.npy"
"""
1. Focal loss: -alpha_t * (1-p_t)^gamma * log(p_t), generalmente con gamma=2 (CHECK: y alpha=0.25 para la clase positiva y 0.75 para la clase negativa.)
2. Combinación de focal loss y class weights 
3. Montaje bipolar (doble banana)
4. No hay slide (solapamiento), porque consideran que aumentan la información de forma redundante
5.  


2. Weighted cross-entropy loss: -w_c * log(p_c), donde w_c es el peso de la clase c, que puede ser inversamente proporcional a la frecuencia de la clase en el dataset.
3. 
2. """

class FocalLossWithClassWeights(nn.Module):
    """
    
    """


class EEG_windows_dataset(Dataset):
    """
    Generic dataset for pytorch structure.
    """
    def __init__(self, windows_array, labels_array):
        self.X = torch.tensor(windows_array, dtype=torch.float32)
        self.X = torch.tensor(labels_array, dtype=torch.float32)

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

class CNN_model(nn.Module):
    """
    
    """
    def __init__(selt, n_channels, input_length, conv_channels=(16))


def build_cnn_model(input_shape, num_classes):



    model = nn.Sequential(
        nn.Conv1d(in_channels=input_shape[0], out_channels=32, kernel_size=3, stride=1, padding=1),
        nn.ReLU(),
        nn.MaxPool1d(kernel_size=2, stride=2),
        nn.Conv1d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1),
        nn.ReLU(),
        nn.MaxPool1d(kernel_size=2, stride=2),
        nn.Flatten(),
        nn.Linear(64 * (input_shape[1] // 4), 128),
        nn.ReLU(),
        nn.Linear(128, num_classes)
    )
    return model