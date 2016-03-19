import tkFont
from Tkinter import *
from tkintertable import TableCanvas

from lab1.algorithms.dfs import DepthFirstSearch
from lab1.algorithms.bfs import BreadthFirstSearch


def get_top():
    """
    Obtaining the top from which to start crawling
    """
    top_from_entry = starting_vertex.get()
    return int(top_from_entry) if top_from_entry else 1


def print_output_log(obj, current_lable):
    """
    Data output in your own label
    """
    for index, string in enumerate(obj.log):
        current_lable.insert(index, string)

    if hasattr(obj, 'dfs'):
        result = obj.visited
    else:
        result = obj.BFS

    current_lable.insert(len(obj.log) + 1, 'Result: ' + ', '.join([str(i) for i in result]))


def dfs_results():
    obj = DepthFirstSearch()
    top = get_top()

    data = obj.transfer_data(table.model.data)
    obj.dfs(top, data)

    print_output_log(obj, lable_dfs_result)


def bfs_results():
    obj = BreadthFirstSearch()
    top = get_top()

    data = obj.transfer_data(table.model.data)
    obj.bfs(top, data)

    print_output_log(obj, lable_bfs_result)

root = Tk()
font_style = tkFont.Font(family='Monospaced', size=9)
root.title(string='Lab 1 - Workarounds graphs')
root.maxsize(width=555, height=580)
root.minsize(width=555, height=580)

tframe = Frame(master=root)
tframe.grid(column=0, row=0, padx=5, pady=5)

table = TableCanvas(tframe, rows=1, cols=3)
table.createTableFrame()

add_row_button = Button(text='Add row', command=table.addRow, font=font_style)
delete_row_button = Button(text='Delete row', command=table.deleteRow, font=font_style)

dfs_result_button = Button(text='DFS', command=dfs_results, font=font_style)
bfs_result_button = Button(text='BFS', command=bfs_results, font=font_style)

starting_vertex = Entry(root)
lable = Label(root, text='Starting vertex:', font=font_style)

lable_dfs_result = Listbox(root)
lable_bfs_result = Listbox(root)

lable.grid(column=0, row=1, padx=5, pady=5, sticky=W)
starting_vertex.grid(column=0, row=1, padx=5, pady=5,)

add_row_button.grid(column=0, row=2, padx=5, pady=5, sticky=W)
delete_row_button.grid(column=0, row=2, padx=5, pady=5)

dfs_result_button.grid(column=0, row=3, sticky=W, padx=5, pady=5)
bfs_result_button.grid(column=0, row=3, sticky=E, padx=5, pady=5)

lable_dfs_result.grid(column=0, row=4, sticky=W, padx=5, pady=5)
lable_bfs_result.grid(column=0, row=4, sticky=E, padx=5, pady=5)

mainloop()
