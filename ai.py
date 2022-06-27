# AI for Self Driving Car

# Importing the libraries
import numpy as np 
import random
import os
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd 
import Variable

#Creating the architect of the Neural Network 
class Network(nn.module):
    def __init__(self, input_size, nb_action):
        super(Network, self , nb_action).__init__()
        self.input_size = input_size
        self.nbaction = nb_action
        self.fc1 = nn.Linear(input_size, 30)
        self.fc2 = nn.Linear(30, nb_action)
        
    def forward(self, state):
        x = F.relu(self.fc1(state))
        
