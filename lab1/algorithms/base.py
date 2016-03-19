class BeenarTree(object):

    @staticmethod
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
