import numpy as np
import matplotlib.pyplot as plt

# Zad1

x = np.arange(20, 41, 1)
s = 1 / x
plt.plot(x, s, label="1/x")

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("Wykres funkcji 1/x")

plt.legend()
plt.axis([20, 40, 0.02, 0.05])
plt.show()

# Zad2

x = np.arange(20, 41, 1)
s = 1 / x
plt.plot(x, s, 'bo--', label="1/x")

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("Wykres funkcji 1/x")

plt.legend()
plt.axis([20, 40, 0.02, 0.05])
plt.show()

# Zad3

x = np.arange(0, 46, 0.1)
a = np.sin(x)
s = np.cos(x)

plt.plot(x, a, label="sin(x)")
plt.plot(x, s, label="cos(x)")

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("Wykres funkcji sinus oraz cosinus")

plt.legend()

plt.show()

# Zad4

x = np.arange(0, 46, 0.1)
a = np.sin(x)
s = np.sin(x) * -1 - 2

plt.plot(x, a, label="sin(x)")
plt.plot(x, s, label="sin(x)")

# plt.axis([0, 45, -1, 1])

plt.xlabel("x")
plt.ylabel("f(x)")

plt.title("Wykres funkcji sinus, sinus")

plt.legend()

plt.show()
