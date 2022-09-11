import time

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

from .maze import Maze
from .dfs import MazeSearchDFS


def msg_usr(s):
    """
    Send the user a string message

    :param s: string
    :return: None
    """
    print(s)
    plt.title(s, fontsize=12)
    plt.draw()


def calibrate_maze(rows, cols):
    """
    Function returns an array of x coordinates and y coordinates

    :param rows: number of rows
    :param cols: number of columns
    :return: array of x and y coordinates
    """
    msg_usr('You will define the corners of the maze, click to begin')

    plt.waitforbuttonpress()

    # Loop through get user input
    while True:
        pts = []
        while len(pts) < 4:
            msg_usr('Select the 4 corners with the mouse')
            pts = np.asarray(plt.ginput(4, timeout=-1))
            if len(pts) < 4:
                msg_usr('Too few points, starting over')
                time.sleep(1)  # Wait a second

        # Set equal to x and y of first pt (left, right, up down)

        x = sorted([x[0] for x in pts])
        y = sorted(y[1] for y in pts)

        x_lbound = (x[0] + x[1]) / 2
        x_ubound = (x[2] + x[3]) / 2
        y_lbound = (y[0] + y[1]) / 2
        y_ubound = (y[2] + y[3]) / 2

        # Draw a "+" in each box
        x_coords = np.linspace(x_lbound, x_ubound, cols)
        y_coords = np.linspace(y_lbound, y_ubound, rows)
        ids = []
        for row in y_coords:
            for col in x_coords:
                ids.append(plt.text(col, row, "+", color="b", verticalalignment="center", horizontalalignment="center"))

        msg_usr('Does this look correct? Press space for yes, mouse click for no')

        # Wait for buttton click
        btn_clk = plt.waitforbuttonpress()

        # Remove the "+" indicators
        for markers in ids:
            markers.remove()

        if btn_clk:
            break

    # Return bounds of maze
    return x_coords, y_coords


def get_start_finish():
    msg_usr('You will define the start and finish of the maze, click to begin')

    plt.waitforbuttonpress()

    pts = []
    while len(pts) < 2:
        msg_usr('Select the start and finish with the mouse')
        pts = np.asarray(plt.ginput(2, timeout=-1))
        if len(pts) < 2:
            msg_usr('Too few points, starting over')
            time.sleep(1)  # Wait a second

    # Return bounds of maze
    return pts


def main():
    filename = input("Enter the filepath of the maze image: ")
    rows = int(input("Enter the number of rows in the maze: "))
    cols = int(input("Enter the number of columns in the maze: "))
    img = mpimg.imread(filename)

    plt.imshow(img)

    x_coords, y_coords = calibrate_maze(rows, cols)
    start_point, finish_point = get_start_finish()

    maze = Maze(img, x_coords, y_coords, start_point, finish_point)
    ms = MazeSearchDFS(maze)

    solution = ms.search()

    msg_usr("Maze solution:")

    plt.plot([node.pos[0] for node in solution], [node.pos[1] for node in solution], color="r")

    plt.show()


if __name__ == '__main__':
    main()
