import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(-1., 3., 100)
u = np.sin(x) + x**2. + 3


x_approximation = np.linspace(-1., 3., 100)
u_approximation = np.sin(x) + x**2. + 3 + np.random.uniform(low=0.01, high=0.1, size=(len(x),))
# np.random.rand(len(x))

x_data = x[10::20]
u_data = u[10::20]

plt.plot(x, u, label="Interpolation")
plt.scatter(x_data, u_data, label="Data points")
plt.plot(x_approximation, u_approximation, label="Approximation")
# plt.vlines(x_data, -10, 10)
plt.axvline(x=0, c="black")
plt.axhline(y=0, c="black")
plt.xlabel("x")
plt.ylabel("u")
plt.legend()
# plt.axes()
# plt.show()
plt.savefig("fig_3_1_data_with_interpolation_and_approximation_functions.png", dpi=300)
