import numpy as np

N = 250
X = np.random.randint(0, 101, size=(N, N))
Y = np.random.randint(0, 101, size=(N, N+1))

result = np.dot(X, Y)

for r in result:
    print(r)