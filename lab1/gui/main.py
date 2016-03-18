from Tkinter import *
from tkintertable import TableCanvas

from lab1.algorithms.breadth_first_search import transfer_data


def collect_data():
    transfer_data(table.model.data)

root = Tk()

tframe = Frame(master=root)
tframe.grid(column=0, row=0)

table = TableCanvas(tframe, rows=1, cols=3)
table.createTableFrame()

add_row_button = Button(text='Add row', command=table.addRow)
delete_row_button = Button(text='Delete row', command=table.deleteRow)
calculate_button = Button(text='Calculate results', command=collect_data)

add_row_button.grid(column=0, row=1)
delete_row_button.grid(column=0, row=2)
calculate_button.grid(column=1, row=0)

mainloop()
