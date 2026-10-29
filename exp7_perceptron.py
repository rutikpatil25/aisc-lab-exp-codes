import numpy as np

class Perceptron:
    def __init__(self, input_size, lr=0.1, epochs=20):
        self.weights = np.zeros(input_size)
        self.bias = 0.0
        self.lr = lr
        self.epochs = epochs

    def activation(self, x):
        # Step activation function
        return 1 if x >= 0 else 0

    def predict(self, x):
        z = np.dot(x, self.weights) + self.bias
        return self.activation(z)

    def train(self, X, y):
        for epoch in range(self.epochs):
            total_error = 0

            for xi, target in zip(X, y):
                pred = self.predict(xi)
                error = target - pred

                self.weights += self.lr * error * xi
                self.bias += self.lr * error

                total_error += abs(error)

            print("Epoch:", epoch + 1, "Error:", total_error)


# AND gate dataset
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0, 0, 0, 1])

# Create perceptron
p = Perceptron(input_size=2, lr=0.1, epochs=20)

# Train
p.train(X, y)

# Test
print("\nPredictions:")
for x in X:
    print(x, "=>", p.predict(x))