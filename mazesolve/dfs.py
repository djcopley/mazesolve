from .maze import Maze


class MazeSearchDFS:
    """
    MazeSearch has a maze object that it will search through
    """

    def __init__(self, maze: Maze):
        self.maze = maze

    def search(self):
        """
        One directional search

        :return: Solution path
        """
        def explore(node, path):
            if node == self.maze.finish:
                return node,

            result = None
            for edge in node.edges:
                if edge not in path:
                    result = explore(edge, path + (node,))
                if result:
                    break

            return (node,) + result if result else None

        return explore(self.maze.start, tuple())
