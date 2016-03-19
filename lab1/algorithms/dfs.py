from base import BeenarTree


class DepthFirstSearch(BeenarTree):
    def __init__(self):
        BeenarTree.__init__(self)
        self.visited = set()
        self.log = []

    def dfs(self, v, data):
        """
        Depth First Search - DFS
        """
        self.log.append('Current top - {};'.format(v))
        if v in self.visited:
            return
        self.visited.add(v)
        for i in data[v]:
            if i not in self.visited:
                self.dfs(i, data)

if __name__ == "__main__":
    test = {
        1: {1: 5},
        2: {1: 3},
        3: {1: 5, 2: 2},
        4: {1: 5},
        5: {1: 4, 2: 1, 3: 3},
    }
    obj = DepthFirstSearch()
    data = obj.transfer_data(test)
    obj.dfs(3, data)
    print obj.log, obj.visited
