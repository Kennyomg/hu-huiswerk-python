import tkinter as tk

# if you are still working under a Python 2 version,
# comment out the previous line and uncomment the following line
# import Tkinter as tk


def write_slogan():
    print("Tkinter is easy to use!")


root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame,
                   text="QUIT",
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="Hello",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()
