# %%
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_excel("PLA_Data1.xlsx",sheet_name="Sheet1")
dataframe = pd.DataFrame(data)
df = dataframe.sample(frac=0.75)
data_size = len(df)
print(df)

# %%
#Making a copy of the excel file
#taking randomly 75% data into the dataframe for testing

# %%
X1 = df["x1"].to_numpy(float)
X2 = df["x2"].to_numpy(float)
Y = df["Class"].to_numpy(float)
Y = Y.reshape((data_size,1))

# %%
#copying the array items into respective numpy arrays and reshaping the dimensions

# %%
fig = plt.figure()
fig.set_size_inches(20,10,forward=True)
ax = fig.add_subplot(projection='3d')
ax.scatter3D(X1,X2,Y,color="Red")
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Class')
plt.show()

# %%
#plotting the graph for X1, X2, Class.

# %%
Ones = np.ones(data_size)
X = np.dstack((Ones,X1,X2))[0]
W = np.random.rand(3,1)
count = 0
while count < data_size:
    count=0
    for i in range(data_size):
        Xtrain = X[i].reshape(3,1)
        if np.sign(Y[i]) != np.sign(np.matmul(np.transpose(W), Xtrain)):
            W += Y[i] * Xtrain
        else:
            count +=1


# %%
#Training the algo with 75% dataset to get the required Weight list.
#Testing the remaining 25% of the dataset.
#counting no. of errors in testing dataset

# %%
testing_data = dataframe.copy(deep=True)
testing_data = testing_data.drop(df.index)
testing_data['H(X1,X2)'] = np.sign(W[0][0] + W[1][0]*testing_data['x1'] + W[2][0]*testing_data['x2'])
print(testing_data)
Error_count=0
for i in testing_data.index:
    if testing_data.loc[i][2] != testing_data.loc[i][3]:
        Error_count += 1
print("No. of Errors in testing : ",Error_count)


