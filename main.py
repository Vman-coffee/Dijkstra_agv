import numpy as np


class Vertex:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y


class Edge:
    def __init__(self, head, rear, cost):
        self.head = head
        self.rear = rear
        self.cost = cost


class Map:
    def __init__(self):
        self.vertexes = None  # Vertex
        self.edges = None  # list:[(vertex1,vertex2,cost),]

        self.travel_v = 2
        self.rotate_v = 10/180*np.pi

    def add_vertex(self, name, x, y):
        vertex = Vertex(name, x, y)
        self.vertexes.append(vertex)

    def add_edge(self, head, rear, cost=None):
        if self.find_vertex(head) is None or self.find_vertex(rear) is None:
            print("add edge failed,vertex doesn't exist.")
            return
        if cost is not None:
            edge = Edge(head, rear, cost)
            self.edges.append(edge)
            return
        else:

            cost = np.sqrt()




    def is_vertex_exist(self, vertex):
        if vertex in self.vertexes:
            return True
        return False

    def is_edge_exist(self, edge):
        if edge in self.edges:
            return True
        return False

    def find_vertex(self, name):
        for vertex in self.vertexes:
            if vertex.name == name:
                return vertex
        return None

    def get_shortest_path(self, beg_id, end_id):
        if self.find_vertex(beg_id) is None or self.find_vertex(end_id) is None:
            print("get shortest path failed,vertex doesn't exit.")
            return None


if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
