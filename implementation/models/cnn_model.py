"""
# File: cnn_model.py
# Project: Trabajo de graduación
# Author: Maria Fernanda Andrade Recinos

Reusable CNN (1D Convolutional networks) modules for the AI pipeline.
"""

import torch
import torch.nn as nn
import torchvision
import torchvision.transforms as transforms

batch_size = 64
num_classes = 10
learning_rate = 0.001
num_epochs = 20

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
