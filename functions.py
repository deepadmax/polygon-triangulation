import numpy as np


def angles_to_points(lengths, angles):
    if len(lengths) != len(angles):
        raise ValueError('lengths and angles must be the same size')

    points = [(0, 0)]
    
    for length, angle in zip(lengths, angles):
        x = np.sin(angle) * length
        y = np.cos(angle) * length

        new_point = (
            points[-1][0] + x,
            points[-1][1] + y
        )

        points.append(new_point)

    return points


def generate_convex_polygon(n=3):
    maximum_angles = (n - 2) * 180

    lengths = np.random.uniform(low=1, high=5, size=(n,))
    angles = np.random.uniform(low=1, high=179, size=(n,))

    print(lengths, len(lengths))
    print(angles, len(angles))
    
    angles_sum = np.sum(angles)
    ratio = maximum_angles / angles_sum
    angles *= ratio

    # test
    lengths = [1]*n
    angles = [maximum_angles / n]*n
    
    # Rotate angles relatively to previous ones
    for i in range(n - 1):
        angles[i + 1] += angles[i]

    lengths = np.array(lengths)
    angles = np.array(angles)

    return lengths, angles