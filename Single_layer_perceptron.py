import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ANN import FClayer
from ANN import ActivationLayer
from ANN import NetworkLayer

def mse(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2))

def mse_prime(y_true, y_pred):
    return 2*(y_pred-y_true)/y_true.size

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1-np.tanh(x)**2

df_train = np.array([[[1,0,0]], [[1,0,1]], [[1,1,0]], [[1,1,1]]])
df_class = np.array([[[0]], [[1]], [[1]], [[0]]])

net = NetworkLayer()
net.layers.append(FClayer(3,1))
net.layers.append(ActivationLayer(tanh,tanh_prime))
net.loss = mse
net.loss_deriv = mse_prime
net.train(df_train,df_class,epochs=5000,learn_rate=0.01)
out = net.testing(df_train)
print('\n','Predicted   ','Actual')
for i in range(len(out)):
    print(out[i],df_class[i])