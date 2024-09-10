import MealMap
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

def main() :
    labels = ['Full', 'Empty']
    full_table = MealMap.full_table
    sizes = [(len(full_table)), (50 - (len(full_table)))]

    root = tk.Tk()
    root.title("MealMap")

    fig, ax = plt.subplots(figsize=(6, 6))

    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)

    ax.axis('equal')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


    root.mainloop()