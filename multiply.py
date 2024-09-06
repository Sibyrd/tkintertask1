import tkinter as tk

window = tk.Tk()


def multiply():
    title.configure(text=str(int(inp1.get())*int(inp2.get())))

window.title("Multiplication Program")
window.geometry("300x100")
title = tk.Label(window, text="Multiplication")
inp1 = tk.Entry(window)
inp2 = tk.Entry(window)
button = tk.Button(window, text="Multiply!", command=multiply)
title.pack()
inp1.pack()
inp2.pack()
button.pack()




window.mainloop()
