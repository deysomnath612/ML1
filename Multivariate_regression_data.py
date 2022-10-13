# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel("Multivariate_Regression_data.xlsx",sheet_name="Sheet1")
dataframe = pd.DataFrame(data)
df = dataframe.sample(frac=0.80)
data_size = len(df)
print(df)
X1 = df["X1"].to_numpy(float)
X2 = df["X2"].to_numpy(float)
Y = df["Y"].to_numpy(float)

# %%
#Making a copy of the excel file
#taking rondomly 80% data into the dataframe for testing
#Making numpy array X1, X2, Y to store testing data

# %%
fig = plt.figure()
fig.set_size_inches(20,10,forward=True)
ax = fig.add_subplot(projection='3d')
ax.scatter3D(dataframe['X1'],dataframe['X2'],dataframe['Y'],color="Red")
ax.set_xlabel('X1')
ax.set_ylabel('X2')
ax.set_zlabel('Y')
plt.show()

# %%
#plotting the graph for X1, X2, Y.

# %%
Ones = np.ones(data_size)
X1_training = X1[0:data_size]
X2_training = X2[0:data_size]
Y_training = Y[0:data_size]
Y_training = Y_training.reshape((data_size,1))
W = np.random.rand(3,1)
X = np.dstack((Ones,X1_training,X2_training))[0]

# %%
#Creating the Xn matrix
#Creating the random W array and managing the dimensions of matrix

# %%
Xtrans = np. transpose(X)
W = np.matmul(np.linalg.inv(np.matmul(Xtrans,X)),np.matmul(Xtrans,Y_training))
testing_data = dataframe.copy(deep=True)
testing_data = testing_data.drop(df.index)
testing_data['H(X1,X2)'] = W[0][0] + W[1][0]*testing_data['X1'] + W[2][0]*testing_data['X2']
print(testing_data)


# %%
#Computing ((Xt*X)^-1)*(Xt*Y) to get Wd
#Testing remaining 20% data to get H(X1,X2)


# %%
E = 0
diff = testing_data['Y'] - testing_data['H(X1,X2)']
diff = diff ** 2
E = np.mean(diff)
print("Mean sqare Error : ",E)

# %%
#Computing mean square from the testing data


