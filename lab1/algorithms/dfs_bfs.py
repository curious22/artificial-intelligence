def transfer_data(dict_data):
    """
    Transfer data from dictionary to the matrix
    """
    result = {}
    for index, col in enumerate(sorted(dict_data.keys())):
        row_data = []
        for row in sorted(dict_data[col]):
            row_data.append(int(dict_data[col][row]))
        result[index + 1] = row_data

    return result

visited = set()
log = []


def dfs(v, data):
    """
    Depth First Search - DFS
    """
    log.append('Current top - {};'.format(v))
    if v in visited:
        return
    visited.add(v)
    for i in data[v]:
        if i not in visited:
            dfs(i, data)


if __name__ == '__main__':
    test = {
        1: {1: 5},
        2: {1: 3},
        3: {1: 5, 2: 2},
        4: {1: 5},
        5: {1: 4, 2: 1, 3: 3},
    }
    data = transfer_data(test)

    start = 1
    dfs(start, data)
    print(visited)
