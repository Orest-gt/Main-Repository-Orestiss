from tqdm import tqdm
import numpy as np

# Φόρτωση δεδομένων
training_data = np.load("training_data.npz")

class MLP:
    def __init__(self, input_size, hidden_size, output_size, learning_rate=0.01):
        self.lr = learning_rate
        # Αρχικοποίηση βαρών και biases
        self.weights_input_to_hidden = np.random.randn(input_size, hidden_size) * self.lr
        self.weights_hidden_to_output = np.random.randn(hidden_size, output_size) * self.lr
        self.bias_hidden = np.zeros(hidden_size)
        self.bias_output = np.zeros(output_size)

    @staticmethod
    def relu(x):
        return np.maximum(0, x)

    @staticmethod
    def d_relu(x):
        return (x > 0).astype(float)

    @staticmethod
    def sigmoid(x):
        return 1 / (1 + np.exp(-x))

    @staticmethod
    def d_sigmoid(x):
        return x * (1 - x)

    def forward(self, x):
        # Από input -> hidden
        self.hidden_output = self.relu((x @ self.weights_input_to_hidden) + self.bias_hidden)
        # Από hidden -> output
        self.output = self.sigmoid((self.hidden_output @ self.weights_hidden_to_output) + self.bias_output)
        return self.output

    def backward(self, x, y, output):
        # Σφάλμα εξόδου
        error = y - output
        d_output = error * self.d_sigmoid(output)

        # Σφάλμα για κρυφό layer
        error_hidden = d_output @ self.weights_hidden_to_output.T
        d_hidden = error_hidden * self.d_relu(self.hidden_output)

        # Ενημέρωση βαρών & bias
        self.weights_hidden_to_output += np.outer(self.hidden_output, d_output) * self.lr
        self.weights_input_to_hidden += np.outer(x, d_hidden) * self.lr
        self.bias_output += d_output * self.lr
        self.bias_hidden += d_hidden * self.lr

    def train(self, X, y, epochs=1000, verbose=True):
        for epoch in tqdm(range(epochs), desc="Training..."):
            for xi, yi in zip(X, y):
                output = self.forward(xi)
                self.backward(xi, yi, output)

            if verbose and epoch % 100 == 0:
                predictions = np.array([self.forward(xi) for xi in X])
                loss = np.mean((y - predictions) ** 2)
                print(f"Epoch: {epoch}\nLoss: {loss:.4f}")

# Φόρτωση δεδομένων
X = training_data["X"]
y = training_data["y"]

# Αν χρειάζεται reshape το y
if y.ndim == 1:
    y = y.reshape(-1, 1)

epochs = int(input("Epochs: "))
model = MLP(input_size=10, hidden_size=30, output_size=1, learning_rate=0.01)
model.train(X, y, epochs=epochs)
