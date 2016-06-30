import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst


class FlavorSetup(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # CURRENCY
        self.currencydict = {}
        self.currencymat = ''
        self.currencymaterial = tk.Entry(self, textvariable=self.currencymat)
        self.currencymaterial.grid(row=1, column=0, sticky='w')
        self.currencymaterial.insert(0, 'inorganic material')
        self.currencyvalue = tk.Spinbox(self, from_=0, to=9999999999999,
                                        justify='center')
        self.currencyvalue.grid(row=2, column=0, sticky=('w', 'e'))
        self.currencyvalue.delete(0, 'end')
        self.currencyvalue.insert(0, 'value')
        self.currencydisplay = tkst.ScrolledText(self, state='disabled',
                                                 height=5, width=50,
                                                 wrap=tk.WORD)
        self.currencydisplay.grid(row=0, column=1, columnspan=3,
                                  rowspan=4, sticky=('w', 'e'))
        self.addcurrencytype = tk.Button(self, text='Add Currency Type',
                                         command=lambda: self.add_currencytype(
                                         ))
        self.addcurrencytype.grid(row=0, column=0, sticky=('w', 'e'))
        self.removecurrencytype = tk.Button(self, text='Remove Currency Type',
                                            command=lambda:
                                            self.remove_currenctytype())
        self.removecurrencytype.grid(row=3, column=0, sticky=('w', 'e'))

        # CURRENCY_BY_YEAR
        self.curby = tk.IntVar()
        self.currencybyyear = tk.Checkbutton(self, variable=self.curby,
                                             text='Currency by Year')
        self.currencybyyear.grid(row=4, column=0, sticky='w')

        # TRANSLATION
        self.translationlabel = tk.Label(self, justify='left',
                                         text='Translation:')
        self.translationlabel.grid(row=4, column=1, sticky='e')
        self.translation = ''
        self.translationentry = tk.Entry(self, textvariable=self.translation)
        self.translationentry.grid(row=4, column=2, sticky='w')
        self.translationentry.insert(0, 'DWARF')

        # FRIENDLY_COLOR
        self.friendlycolorlabel = tk.Label(self, justify='left',
                                           text='Friendly Color (f/b):')
        self.friendlycolorlabel.grid(row=5, column=0, sticky='w')
        self.forefriendlycolor = tk.Spinbox(self, from_=0, to=7,
                                            justify='center')
        self.forefriendlycolor.grid(row=5, column=1, sticky='w')
        self.forefriendlycolor.delete(0, 'end')
        self.forefriendlycolor.insert(0, 7)
        self.backfriendlycolor = tk.Spinbox(self, from_=0, to=7,
                                            justify='center')
        self.backfriendlycolor.grid(row=5, column=2, sticky='w')
        self.backfriendlycolor.delete(0, 'end')
        self.backfriendlycolor.insert(0, 0)
        self.brightfore = tk.IntVar()
        self.brightforefriendlycolor = tk.Checkbutton(
            self, variable=self.brightfore, text='Bright Fore Color')
        self.brightforefriendlycolor.grid(row=5, column=3, sticky='w')

    def add_currencytype(self):
        self.curmat = self.currencymaterial.get()
        self.currencydict[self.curmat] = self.currencyvalue.get()

        self.fill_currencytypes()

    def remove_currenctytype(self):
        if self.currencymaterial.get() in self.currencydict:
            self.currencydict.pop(self.currencymaterial.get(), None)

        self.fill_currencytypes()

    def fill_currencytypes(self):
        string = ''
        for key, value in self.currencydict.items():
            string = string + key + ':' + value + ' '

        self.currencydisplay.config(state='normal')
        self.currencydisplay.delete('1.0', tk.END)
        self.currencydisplay.insert('1.0', string)
        self.currencydisplay.config(state='disabled')


if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    flavorsetup = FlavorSetup(root, padx=6, pady=6)
    note.add(flavorsetup, text='Flavor')
    note.grid()
    root.mainloop()
