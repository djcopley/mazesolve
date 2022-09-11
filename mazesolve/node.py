class Node:
    def __init__(self, pos):
        self.pos = pos
        self.edges = []

    def __str__(self):
        return f"Node {str(self.pos)}"

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if (isinstance(other, Node) and self.pos == other.pos) or (isinstance(other, tuple) and self.pos == other):
            return True
        else:
            return False

    def __contains__(self, item):
        return self == item

    def add_edge(self, other):
        if other not in self.edges:
            self.edges.append(other)
        if self not in other.edges:
            other.edges.append(self)
