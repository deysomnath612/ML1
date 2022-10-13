import numpy as np
import pandas as pd
class Layer:
    def __init__(self):
        self.input = None
        self.output = None
    def forward_prop(self,input_data):
        raise NotImplementedError
    def back_prop(self,out_err,learn_rate):
        raise NotImplementedError

class FClayer(Layer):
    def __init__(self,input_size,output_size):
        self.weights = np.random.rand(input_size,output_size) 
    def forward_prop(self,input_data):
        self.input = input_data
        self.output = np.dot(self.input,self.weights)
        return self.output
    def back_prop(self, out_err, learn_rate):
        self.learn_rate = learn_rate
        input_err = np.dot(out_err,self.weights.transpose())
        self.weights_err = np.dot(self.input.transpose(),out_err)
        self.weights -= self.weights_err * learn_rate
        return input_err

class ActivationLayer(Layer):
    def __init__(self,sigm,sigm_deriv):
        self.sigm = sigm
        self.sigm_deriv = sigm_deriv
    def forward_prop(self,input_data):
        self.input = input_data
        self.output = self.sigm(self.input)
        return self.output
    def back_prop(self, out_err, learn_rate):
        return self.sigm_deriv(self.input) * out_err

class NetworkLayer:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_deriv = None
    def train(self,x_train,y_train,epochs,learn_rate):
        err_list = []
        for i in range(epochs):
            err = 0
            for j in range(len(x_train)):
                output = x_train[j]
                for layer in self.layers:
                    input_data = output
                    output = layer.forward_prop(input_data)
                err += self.loss(y_train[j],output)
                error = self.loss_deriv(y_train[j],output)
                for layer in reversed(self.layers):
                    error = layer.back_prop(error,learn_rate)
            err/=len(x_train)
            err_list.append(err)
        return err
    def testing(self,input_data):
        result = []
        for i in range(len(input_data)):
            output = input_data[i]
            for layer in self.layers:
                output = layer.forward_prop(output)
            result.append(output)
        return result 
