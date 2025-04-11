#import numpy as np
from tqdm import tqdm
from sklearn.model_selection import train_test_split
from dataset import *

def general_deco(func, *args, **kwargs):
    def wrap():
        print(f"\nStarting {func.__name__}\n")
        func(*args, **kwargs)
        print(f"\nEnding {func.__name__}...\n")
    return wrap

class MLP:
    def __init__(self, input_size=5, hidden_size=30, output_size=2, learning_rate=0.01):
        self.lr = learning_rate
        self.bias_hidden = np.zeros(hidden_size) * self.lr
        self.bias_output = np.zeros(output_size) * self.lr
        self.weights_hidden = np.random.randn(input_size, hidden_size) * self.lr
        self.weights_output = np.random.randn(hidden_size, output_size) * self.lr
        self.h = None

    @staticmethod
    def ReLu(data):
        return np.maximum(0, data)
    @staticmethod
    def sigmoid(data):
        return 1 / (1 + np.exp(-data))

    @staticmethod
    def softmax(x):
        exps = np.exp(x - np.max(x))  # για αριθμητική σταθερότητα
        return exps / np.sum(exps)

    @staticmethod
    def ReLu_(data):
        return (data > 0).astype(float)

    def feedforward_pass(self, x):
        self.h = self.ReLu((x @ self.weights_hidden) + self.bias_hidden)
        o = self.softmax((self.h @ self.weights_output) + self.bias_output)
        return o

    def backward_check(self, x, y, o):
        error = y - o
        #d_out = error * (o * (1 - o))
        d_out = o - y # we have categorical instance
        error_hid = d_out @ self.weights_output.T
        d_hid = error_hid * MLP.ReLu_(self.h)

        #self.weights_output -= (self.h.T @ d_out) * self.lr
        #self.weights_hidden -= (x.T @ d_hid) * self.lr
        #Because we have to do outer (outside) multiplication
        #So we have...

        self.weights_output -= np.outer(self.h, d_out) * self.lr
        self.weights_hidden -= np.outer(x, d_hid) * self.lr

        self.bias_output -= d_out * self.lr
        self.bias_hidden -= d_hid * self.lr

    @staticmethod
    def binary_cross_entropy(y_true, y_pred):
        epsilon = 1e-8  # για να μην έχουμε log(0)
        return -np.mean(y_true * np.log(y_pred + epsilon) + (1 - y_true) * np.log(1 - y_pred + epsilon))

    @staticmethod
    def categorical_cross_entropy(y_true, y_pred):
        epsilon = 1e-8
        return -np.sum(y_true * np.log(y_pred + epsilon))

    def train(self, X, y, epochs=100, verbose=True):
        loss = 0
        for i in tqdm(range(epochs), desc="Training..."):
            for xi, yi in zip(X, y):
                output = self.feedforward_pass(xi)
                self.backward_check(xi, yi, output)
                loss = self.categorical_cross_entropy(np.array(yi), output)

            '''
            if i % 100 == 0 and verbose:
                print(f"Model is on {i} epoch!"
                      f"\nLoss: {loss}")
            '''
        print(f"Loss: {loss:.4f}")


    def predict(self, X, y_test):
        print("\nTESTING STARTED\n")
        predictions = []
        #output = None because we want it to be local
        for x in X:
            output = self.feedforward_pass(x)
            predictions.append(output)
            print("Prediction loss:")
            print(self.categorical_cross_entropy(np.array(y_test), output), end="\n\n")
        predictions = np.argmax(predictions, axis=1)

        accuracy = np.mean(predictions == np.argmax(y_test, axis=1))
        print(f"Accuracy: {accuracy:.2f}", end="\n\n")

        return np.array(predictions)

# 10 δείγματα, καθένα με 5 χαρακτηριστικά

model = MLP(learning_rate=0.01)

x_train, x_test, y_train, y_test = train_test_split(X, y)

model.train(x_train, y_train, 10000, True)
pred = model.predict(x_test, y_test)
print("Prediction:")
print(pred)