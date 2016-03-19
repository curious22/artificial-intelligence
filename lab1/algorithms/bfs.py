from lab1.algorithms.base import BeenarTree


class BreadthFirstSearch(BeenarTree):

    def __init__(self):
        BeenarTree.__init__(self)
        self.visited = set()
        self.Q = []
        self.BFS = []
        self.log = []

    def bfs(self, v, data):
        """
        Breadth First Search
        """
        if v in self.visited:
            return

        self.visited.add(v)
        self.BFS.append(v)
        self.log.append('Vertex = {}'.format(v))

        for i in data[v]:
            if i not in self.visited:
                self.Q.append(i)

        while self.Q:
            self.bfs(self.Q.pop(0), data)

if __name__ == '__main__':
    inc = {
        1: {1: 2, 2: 8},
        2: {1: 1, 2: 3, 3: 8},
        3: {1: 2, 2: 4, 3: 8},
        4: {1: 3, 2: 7, 3: 9},
        5: {1: 6, 2: 7},
        6: {1: 5},
        7: {1: 4, 2: 5, 3: 8},
        8: {1: 1, 2: 2, 3: 3, 4: 7},
        9: {1: 4},
    }
    obj = BreadthFirstSearch()
    data = obj.transfer_data(inc)
    obj.bfs(1, data)
    print obj.BFS

