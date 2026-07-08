import tkinter as tk
def click():
    print("hello dileep")

window = tk.Tk()

button = tk.Button(window , text="click")
command=click()

button.pack()
window.mainloop()