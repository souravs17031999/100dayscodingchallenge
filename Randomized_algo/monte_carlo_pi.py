# Program to estimate value of pi using monte-carlo method.
# Monte-carlo method is one of the randomized algorithms which uses some kind of randomness
# in computational algorithms. It relies on random sampling to obtain numerical results.

import random

INTERVAL = 5000

circle_points, square_points = 0, 0

for i in range(INTERVAL * 2):

    range_x = random.uniform(-1, 1)
    range_y = random.uniform(-1, 1)

    origin_dist = range_x ** 2 + range_y ** 2
    if origin_dist <= 1:
        circle_points += 1

    square_points += 1

    if i % 50 == 0:
        print(f"Value of pi after {i} iterations: {(4 * circle_points) / square_points}")


print(f"Final value of pi : {(4 * circle_points) / square_points}")
