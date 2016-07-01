import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst


class ReligionSetup(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # RELIGION
        self.religionlabel = tk.Label(self, justify='left', text='Religion:')
        self.religionlabel.grid(row=0, column=0)
        self.religionvar = tk.IntVar()
        self.religionforce = tk.Radiobutton(
            self, text='Region Force', variable=self.religionvar, value=0)
        self.religionforce.grid(row=0, column=1)
        self.religionpantheon = tk.Radiobutton(
            self, text='Pantheon', variable=self.religionvar, value=1)
        self.religionpantheon.grid(row=0, column=2)

if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    religionsetup = ReligionSetup(root, padx=6, pady=6)
    note.add(religionsetup, text='Flavor')
    note.grid()
    root.mainloop()
