import numpy as np
import control.matlab as ml
import matplotlib.pyplot as plt
 
num = np.array([2, 0])
den = np.polymul(np.array([0.5, 1]), np.array([0.25, 1]))
den = np.polymul(den, np.array([0.25, 1]))

g = ml.tf(num, den)
print(g)
print(ml.pole(g))
print(ml.zero(g))

mag, phase, w = ml.bode(g)
plt.show()
