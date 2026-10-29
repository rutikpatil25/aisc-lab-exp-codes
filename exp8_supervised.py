import numpy as np

class SupervisedPerceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)
        self.bias = 0.0
        self.lr = learning_rate
        
    def activation(self, x):
        return 1 if x >= 0 else 0
        
    def predict(self, inputs):
        return self.activation(np.dot(inputs, self.weights) + self.bias)
        
    def train(self, X, y, epochs=10):
        print("--- Training Supervised Perceptron ---")
        for epoch in range(epochs):
            total_error = 0
            for inputs, target in zip(X, y):
                prediction = self.predict(inputs)
                error = target - prediction
                total_error += abs(error)
                self.weights += self.lr * error * inputs
                self.bias += self.lr * error
            print(f"Epoch {epoch+1} | Total Error: {total_error}")
            if total_error == 0:
                break

class UnsupervisedHebbian:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.zeros(input_size)
        self.bias = 0.0
        self.lr = learning_rate
        
    def activation(self, x):
        return 1 if x >= 0 else -1
        
    def predict(self, inputs):
        return self.activation(np.dot(inputs, self.weights) + self.bias)
        
    def train(self, X, epochs=5):
        print("\n--- Training Unsupervised Hebbian ---")
        for epoch in range(epochs):
            for inputs in X:
                output = self.predict(inputs) 
                self.weights += self.lr * inputs * output
                self.bias += self.lr * output
            print(f"Epoch {epoch+1} | Weights: {self.weights} | Bias: {self.bias}")

if __name__ == "__main__":
    X_sup = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_sup = np.array([0, 0, 0, 1])
    
    model_sup = SupervisedPerceptron(input_size=2)
    model_sup.train(X_sup, y_sup, epochs=10)
    
    print("\nSupervised Inference:")
    for inputs in X_sup:
        print(f"Input: {inputs} -> Output: {model_sup.predict(inputs)}")
        
    X_unsup = np.array([[1, 1], [-1, -1], [1, 1]])
    
    model_unsup = UnsupervisedHebbian(input_size=2)
    model_unsup.train(X_unsup, epochs=3)
    
    print("\nUnsupervised Inference:")
    test_patterns = np.array([[1, 1], [-1, -1], [1, -1], [-1, 1]])
    for pattern in test_patterns:
        print(f"Pattern: {pattern} -> Cluster: {model_unsup.predict(pattern)}")
