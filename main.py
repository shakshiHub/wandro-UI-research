import os
os.environ['TK_SILENCE_DEPRECATION'] = '1'

import tkinter as tk

# vars
w, h = 1000, 500

# create main window
root = tk.Tk()
root.title("carplay-interface")
root.configure(bg='black')

# logic for centering main window on screen
x = (root.winfo_screenwidth() - w) // 2
y = (root.winfo_screenheight() - h) // 2
root.geometry(f"{w}x{h}+{x}+{y}")


# keeping main window open
root.mainloop()