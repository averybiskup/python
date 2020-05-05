import matplotlib.pyplot as plt

x = [0.5, 1, 1.5,2,2.5,3,3.5,4]
y = [0.002,0.004,0.006,0.008,0.01,0.012,0.014,0.016]

plt.grid(b=None, which='major', axis='both')
plt.scatter(x, y)
plt.show()
