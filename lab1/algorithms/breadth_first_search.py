from pprint import pprint


def transfer_data(dict_data):
    """
    Transfer data from dictionary to the matrix
    """
    result = []
    for col in sorted(dict_data.keys()):
        row_data = []
        for row in sorted(dict_data[col]):
            row_data.append(int(dict_data[col][row]))
        result.append(row_data)

    pprint(result)


if __name__ == '__main__':
    test = {
        10: {'1': '7', '3': '9', '2': '8'},
        1: {'1': '1', '3': '3', '2': '2'},
        6: {'1': '4', '3': '6', '2': '5'}
    }
    transfer_data(test)
