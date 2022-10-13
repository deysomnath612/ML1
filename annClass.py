# %%
import numpy as np

# %%
class Layer:
    def __init__(self):
        self.input = None
        self.output = None

    def forward_prop(self, input):
        raise NotImplementedError
        
    def backward_prop(self, output_error, learning_rate):
        raise NotImplementedError

# %%
class FCLayer(Layer):
    def __init__(self, input_size, output_size):
        self.weight = np.random.rand(input_size, output_size)

    def forward_prop(self, input):
        self.input = input
        self.output = np.dot(input, self.weight)
        return self.output

    def backward_prop(self, output_error, learning_rate):
        input_error = np.dot(output_error, self.weight.T)
        weight_error = np.dot(self.input.T, output_error)

        self.weight -= learning_rate * weight_error
        return input_error

# %%
class ActivationLayer(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    def forward_prop(self, input):
        self.input = input
        self.output = self.activation(input)
        return self.output

    def backward_prop(self, output_error, learning_rate):
        return output_error * self.activation_prime(self.input)

# %%
class ANNetwork:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    def loss_fn(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime
    
    def addLayer(self, layer):
        self.layers.append(layer)
    
    def train(self, x_train, y_train, learning_rate, epochs):
        n = len(x_train)

        for i in range(epochs):
            err = 0
            for j in range(n):
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_prop(output)
                
                err += self.loss(y_train[j], output)

                error_prime = self.loss_prime(y_train[j], output)
                for layer in reversed(self.layers):
                    error_prime = layer.backward_prop(error_prime, learning_rate)
                
            err /= n
            # print('epoch %d   error : %f' % (i+1, err))
            return err

    def predict(self, inpData):
        n = len(inpData)
        result = []
        for i in range(n):
            output = inpData[i]
            for layer in self.layers:
                output = layer.forward_prop(output)
            result.append(output)
        return result

# %%
def tanh(x):
    return np.tanh(x)

def tanh_prime(x):
    return 1 - np.tanh(x)**2

def mse(yTrue, yPred):
    return np.mean(np.power(yTrue-yPred, 2))

def mse_prime(yTrue, yPred):
    return 2*(yPred-yTrue)/len(yTrue)

def sigm(x):
    return 1/(1+np.exp(-x))
def sigm_prime(x):
    return (sigm(x)*(1-sigm(x)))
