import tkinter as tk
import random

window = tk.Tk()


def randomi():
    title.configure(text=str(random.randint(int(inp1.get()),int(inp2.get()))))
    

window.title("RNG")
window.geometry("300x100")
title = tk.Label(window, text="Enter a lower and upper boundary.")
inp1 = tk.Entry(window)
inp2 = tk.Entry(window)
button = tk.Button(window, text="RNG!", command=randomi)
title.pack()
inp1.pack()
inp2.pack()
button.pack()




window.mainloop()
