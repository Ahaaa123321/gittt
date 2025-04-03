import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def unit_impulse():
    n = np.arange(-10, 11)
    x = np.zeros(len(n))
    x[n == 0] = 1
    plot_signal(n, x, 'Unit Impulse Signal')


def unit_step():
    n = np.arange(-10, 11)
    x = np.zeros(len(n))
    x[n >= 0] = 1
    plot_signal(n, x, 'Unit Step Signal')


def rectangular_pulse():
    n = np.arange(-10, 11)
    x = np.zeros(len(n))
    x[np.logical_and(n >= -2, n <= 2)] = 1
    plot_signal(n, x, 'Rectangular Pulse Signal')


def plot_signal(n, x, title):
    fig = plt.Figure(figsize=(6, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.stem(n, x)
    ax.set_title(title)
    ax.set_xlabel('n')
    ax.set_ylabel('x[n]')

    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().grid(row=1, column=0, columnspan=3)


root = tk.Tk()
root.title("Discrete Signals")

btn_impulse = tk.Button(root, text="Unit Impulse", command=unit_impulse)
btn_impulse.grid(row=0, column=0)

btn_step = tk.Button(root, text="Unit Step", command=unit_step)
btn_step.grid(row=0, column=1)

btn_rect = tk.Button(root, text="Rectangular Pulse", command=rectangular_pulse)
btn_rect.grid(row=0, column=2)

root.mainloop()
    