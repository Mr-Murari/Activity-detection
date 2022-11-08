import tkinter as tk
import os

def write_text():
    os.system('error.py')
def option():
    os.system('read.py')

parent = tk.Tk()
frame = tk.Frame(parent)

frame.pack()



text_disp= tk.Button(frame, 
                   text="LIVE",
                    fg="red",
                   command=write_text
                   )

text_disp.pack(side=tk.LEFT)

exit_button = tk.Button(frame,
                   text="RECORDED",
                   fg="green",
                   command=option)
exit_button.pack(side=tk.RIGHT)

parent.mainloop()

