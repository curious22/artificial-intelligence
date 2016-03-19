from Tkinter import *
from tkintertable import TableCanvas

from lab1.algorithms.dfs import DepthFirstSearch


def calculate_results():
    obj = DepthFirstSearch()

    top_from_entry = starting_vertex.get()
    top = int(top_from_entry) if top_from_entry else 1

    data = obj.transfer_data(table.model.data)
    obj.dfs(top, data)

    for index, string in enumerate(obj.log):
        lable_dfs_result.insert(index, string)
    lable_dfs_result.insert(len(obj.log) + 1, 'Result: ' + ', '.join([str(i) for i in obj.visited]))

root = Tk()
root.title(string='Lab 1')
root.maxsize(width=555, height=545)
root.minsize(width=555, height=545)

tframe = Frame(master=root)
tframe.grid(column=0, row=0, padx=5, pady=5)

table = TableCanvas(tframe, rows=1, cols=3)
table.createTableFrame()

add_row_button = Button(text='Add row', command=table.addRow)
delete_row_button = Button(text='Delete row', command=table.deleteRow)
calculate_button = Button(text='Calculate', command=calculate_results)
starting_vertex = Entry(root)
lable = Label(root, text='Starting vertex')
lable_dfs_result = Listbox(root)

lable.grid(column=0, row=1, padx=5, pady=5, sticky=W)
starting_vertex.grid(column=0, row=1, padx=5, pady=5,)
add_row_button.grid(column=0, row=2, padx=5, pady=5, sticky=W)
delete_row_button.grid(column=0, row=2, padx=5, pady=5)
calculate_button.grid(column=0, row=2, sticky=E, padx=5, pady=5)
lable_dfs_result.grid(column=0, row=3, sticky=W+E+N+S, padx=5, pady=5)

mainloop()
