import tkinter as tk
import tkinter.ttk as ttk
import BasicSetupTab
import FluffSetupTab

if __name__ == '__main__':
    root = tk.Tk()
    root.wm_title('Entity Editor')
    note = ttk.Notebook(root)
    basicsetup = BasicSetupTab.BasicSetup(root, padx=6, pady=6)
    note.add(basicsetup, text='Basics')
    note.grid()
    fluffsetup = FluffSetupTab.FluffSetup(root, padx=6, pady=6)
    note.add(fluffsetup, text='Fluff')
    note.grid()
    root.mainloop()
