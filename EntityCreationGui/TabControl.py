import tkinter as tk
import tkinter.ttk as ttk
import BasicSetupTab

if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    basicsetup = BasicSetupTab.BasicSetup(root, padx=6, pady=6)
    note.add(basicsetup, text='Basics')
    note.grid()
    root.mainloop()
