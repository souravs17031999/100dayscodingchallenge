# Given a screen of colors like MS paint, and each position is filled with pixel values
# Then, we need to take a input coordinate and fill all the adjacent nodes connected to it
# like some kind of filling the identified boundary which is denoted by pixel values being
# adjacent to each other (top, bottom, left, right adjacency).
# We need to devise recursive approach for doing this.
# ALso, we have visualized the final results also.

import matplotlib.pyplot as plt

def FloodFill(mat, x, y, prev, curr):
    rows, cols = len(mat), len(mat[0])
    if x < 0 or y < 0 or x >= rows or y >= cols or mat[x][y] != prev or mat[x][y] == curr:
        return

    mat[x][y] = curr

    FloodFill(mat, x + 1, y, prev, curr)
    FloodFill(mat, x - 1, y, prev, curr)
    FloodFill(mat, x, y + 1, prev, curr)
    FloodFill(mat, x, y - 1, prev, curr)


def pretty_print(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end = " ")
        print()

if __name__ == '__main__':
    screen = [
        [1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 1, 0, 0],
        [1, 0, 0, 1, 1, 0, 1, 1],
        [1, 2, 2, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 0, 1, 0],
        [1, 1, 1, 2, 2, 2, 2, 0],
        [1, 1, 1, 1, 1, 2, 1, 1],
        [1, 1, 1, 1, 1, 2, 2, 1]
        ]

    x, y = 4, 4
    prev = screen[x][y]
    new_color = 100
    print(f"Previous color at given coordinate : ({x}, {y}) is {prev}")
    print(f"New coloe given is : {new_color}")
    plt.imshow(screen)
    plt.show()

    FloodFill(screen, x, y, prev, new_color)
    pretty_print(screen)
    plt.imshow(screen)
    plt.show()
