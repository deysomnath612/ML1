# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from ANN import FClayer
from ANN import ActivationLayer
from ANN import NetworkLayer

# %%
data1 =  pd.read_csv('iris.data', sep=",", header=None, names=["sl","sw","pl","pw","class"])
#print(data1)
data2 = pd.read_csv('bezdekIris.data', sep=',', header = None, names=["sl","sw","pl","pw","class"])
#print(data2) 

# %%
SL = data1["sl"].to_numpy(float)
SW = data1["sw"].to_numpy(float)
PL = data1["pl"].to_numpy(float)
PW = data1["pw"].to_numpy(float)
CL = data1["class"].to_numpy(str)
Y=[]
for i in CL:
    if i == 'Iris-setosa':
        Y.append([0,0,1])
    elif i == 'Iris-versicolor':
        Y.append([0,1,0])
    else:
        Y.append([1,0,0])
#print(Y)


# %%
Y = np.array(Y)
Ones = np.ones((150,))
datainput = np.dstack((Ones,SL,SW,PL,PW,Y[:,0],Y[:,1],Y[:,2]))[0]
#print(datainput)
dataframe = pd.DataFrame(datainput)
train_df = dataframe.sample(frac=0.7)
#print(train_df)
testing_dataframe = dataframe.copy(deep=True)
testing_dataframe = testing_dataframe.drop(train_df.index)
testing_data = testing_dataframe.drop(testing_dataframe.columns[[5,6,7]], axis = 1).to_numpy().reshape(45,1,5)
class_data = testing_dataframe.drop(testing_dataframe.columns[[0,1,2,3,4]], axis = 1).to_numpy().reshape(45,1,3)
#print(testing_data)

# %%
df_train = train_df.to_numpy()[:,0:5].reshape(105,1,5)
#print(df_train)
df_class = train_df.to_numpy()[:,5:].reshape(105,1,3)
#print(df_class)

# %%
def mse(y_true, y_pred):
    return np.mean(np.power(y_true-y_pred, 2))

def mse_prime(y_true, y_pred):
    return 2*(y_pred-y_true)/y_true.size

def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1-np.tanh(x)**2

def sigm(x):
    return 1/(1+np.exp(-x))
def sigm_prime(x):
    return (sigm(x)*(1-sigm(x)))
# %%
net = NetworkLayer()
net.layers.append(FClayer(5,4))
net.layers.append(ActivationLayer(sigm,sigm_prime))
net.layers.append(FClayer(4,3))
net.layers.append(ActivationLayer(sigm,sigm_prime))
net.loss = mse
net.loss_deriv = mse_prime
error_train = []
error_test = []
epochs = 3000
for i in range(epochs):
    error_train.append(net.train(df_train,df_class,epochs=1,learn_rate=0.02))
    out = net.testing(testing_data)
    error_test.append(mse(class_data,out))

for i in range(len(out)):
    print(out[i],class_data[i])
#print(error_list)

# out = np.array(out).reshape(45,3)
# count_err = 0

# testing_error = mse(class_data,out)
# print('testing error mse = ',testing_error)


# # %%
fig, ax = plt.subplots()
tr_plot, = ax.plot(error_train)
te_plot, = ax.plot(error_test)
ax.set_xlabel('epoch')
ax.set_ylabel('mean error')
ax.legend((tr_plot, te_plot), ("Training", "Testing"), shadow=True)
plt.show()


