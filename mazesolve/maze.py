import numpy as np

from .node import Node


def distance(pos1, pos2):
    # Distance between 2 points
    return (abs(pos1[0] - pos2[0]) ** 2 + abs(pos1[1] - pos2[1]) ** 2) ** (1 / 2)


class Maze:
    """
    Maze base class.
    """

    def __init__(self, image, x_coords, y_coords, start_point, finish_point):
        self.image = image
        self.nodes = []
        self._construct_graph(x_coords, y_coords, start_point, finish_point)

    def _construct_graph(self, x_coords, y_coords, start_point, finish_point):
        # Generate nodes from top left to bottom right
        for row, y_pos in enumerate(y_coords):
            self.nodes.append([])
            for col, x_pos in enumerate(x_coords):
                # Generate new node
                node = Node((x_pos, y_pos))
                self.nodes[-1].append(node)

                # Check if a path exists between previous node (left and up) and connect graph

                # Check node to the left
                if col - 1 >= 0:
                    other = self.nodes[row][col - 1]
                    if self._path_exists_between(node, other):
                        node.add_edge(other)

                # Check node above
                if row - 1 >= 0:
                    other = self.nodes[row - 1][col]
                    if self._path_exists_between(node, other):
                        node.add_edge(other)
        self.start = self._get_node_by_pos(start_point)
        self.finish = self._get_node_by_pos(finish_point)

    def _get_node_by_pos(self, pos):
        """
        Returns closest node to a given x,y position

        :param pos: x, y
        :return: node at position
        """
        closest_node = None
        for row in self.nodes:
            for node in row:
                if closest_node is None or distance(node.pos, closest_node.pos) > distance(node.pos, pos):
                    closest_node = node

        return closest_node

    def _path_exists_between(self, node1, node2):
        """
        Method checks to see if any black walls exist between two nodes

        :param node1: first node
        :param node2: second node
        :return: true if path exists between nodes
        """
        # Configurable: number of steps between each point to check
        n_steps = 20
        pos1 = tuple(map(int, node1.pos))
        pos2 = tuple(map(int, node2.pos))

        # Must be either vertical or lateral
        if pos1[0] == pos2[0]:
            x = [pos1[0]]
            y = np.linspace(pos1[1], pos2[1], n_steps, dtype=int)
        else:
            x = np.linspace(pos1[0], pos2[0], n_steps, dtype=int)
            y = [pos1[1]]

        for x_px in x:
            for y_px in y:
                # Pixels must be normalized (0 to 1)
                thresh = 2
                if sum(self.image[y_px][x_px]) < thresh:
                    return False

        return True
