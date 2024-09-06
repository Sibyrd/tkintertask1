import tkinter as tk

window = tk.Tk()


def conv():
    title.configure(text=str(int(inp1.get())*0.76))
    

window.title("Currency Converter")
window.geometry("300x100")
title = tk.Label(window, text="Enter USD.")
inp1 = tk.Entry(window)
button = tk.Button(window, text="Convert!", command=conv)
title.pack()
inp1.pack()
button.pack()




window.mainloop()
