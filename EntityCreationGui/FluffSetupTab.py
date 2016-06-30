import tkinter as tk
import tkinter.ttk as ttk
import FlavorSetupTab


class FluffSetup(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        note = ttk.Notebook(self)
        flavorsetup = FlavorSetupTab.FlavorSetup(self, padx=6, pady=6)
        note.add(flavorsetup, text='Flavor')
        note.grid()

if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    fluffsetup = FluffSetup(root, padx=6, pady=6)
    note.add(fluffsetup, text='Fluff')
    note.grid()
    root.mainloop()
