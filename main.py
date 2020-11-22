import matplotlib.pyplot as plt

from functions import *


lengths, angles = generate_convex_polygon(n=9)
points = angles_to_points(lengths, angles)

print(len(lengths), len(angles))

X, Y = zip(*points)

plt.scatter(X, Y, c='r')
plt.show()