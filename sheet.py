import MealMap
import tkinter as tk
from tkinter import ttk
import pandas as pd

def data_sheet() :
    full_table = MealMap.full_table
    status = []
    for i in range(len(full_table)) :
        status.append('Full')
    data = {
        'Table': full_table,
        'Status': status
    }

    df = pd.DataFrame(data)

    root = tk.Tk()
    root.title("MealMap")

    frame = ttk.Frame(root)
    frame.pack(fill=tk.BOTH, expand=True)

    tree = ttk.Treeview(frame, columns=list(df.columns), show='headings')

    for col in df.columns:
        tree.heading(col, text=col)
        tree.column(col, anchor=tk.CENTER)

    for index, row in df.iterrows():
        tree.insert("", "end", values=list(row))

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    tree.pack(fill=tk.BOTH, expand=True)

    root.mainloop()