import numpy as np

x = np.array([20, 30, 40, 50], dtype=float)
y = np.array([20, 40, 60, 80], dtype=float)

def mf(x, c):
    return np.exp(-((x - c) ** 2) / 100)

# Initial parameters
c1 = 25 
c2 = 45  

for epoch in range(100):

    low = mf(x, c1)
    high = mf(x, c2)

    w1 = low / (low + high)
    w2 = high / (low + high)

    y_pred = w1 * 20 + w2 * 80

    error = y - y_pred

    c1 = c1 - 0.01 * np.mean(error * (x - c1))
    c2 = c2 + 0.01 * np.mean(error * (x - c2))

test = 35

low = mf(test, c1)
high = mf(test, c2)

w1 = low / (low + high)
w2 = high / (low + high)

output = w1 * 20 + w2 * 80

print("Temperature:", test)
print("Predicted Fan Speed:", round(output, 2))