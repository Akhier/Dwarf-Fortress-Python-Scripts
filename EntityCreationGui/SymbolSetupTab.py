import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst


class SymbolSetup(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.symbolnounlist = [
            'ALL', 'REMAINING', 'BATTLE', 'BRIDGE', 'CIV', 'LIBRARY',
            'MILITARY_UNIT', 'RELIGION', 'ROAD', 'SIEGE', 'SITE',
            'TEMPLE', 'TUNNEL', 'VESSEL', 'WALL', 'WAR']
        self.symbollist = [
            'FLOWERY', 'NATURE', 'PRIMITIVE', 'HOLY', 'EVIL', 'NEGATOR',
            'MAGIC', 'VIOLENT', 'PEACE', 'UGLY', 'DEATH', 'OLD', 'SUBORDINATE',
            'LEADER', 'NEW', 'DOMESTIC', 'MYTHIC', 'ARTIFICE', 'COLOR',
            'MYSTERY', 'NEGATIVE', 'ROMANTIC', 'ASSERTIVE', 'AQUATIC',
            'PROTECT', 'RESTRAIN', 'THOUGHT', 'WILD', 'NAME_SWAMP',
            'NAME_DESERT', 'NAME_FOREST', 'NAME_MOUNTAINS', 'NAME_OCEAN',
            'NAME_GLACIER', 'NAME_TUNDRA', 'NAME_GRASSLAND', 'NAME_HILLS',
            'NAME_REGION', 'NAME_CAVE', 'EARTH', 'NAME_LAKE',
            'NAME_ENTITY_KINGDOM', 'NAME_ENTITY_TOWN_FOUNDER', 'GOOD',
            'NAME_CONTINENT', 'NAME_ISLAND', 'NAME_ISLAND_SMALL', 'NAME_PEAK',
            'NAME_VOLCANO', 'NAME_COMMON_RELIGION', 'BALANCE', 'BOUNDARY',
            'DANCE', 'DARKNESS', 'LIGHT', 'ORDER', 'FESTIVAL', 'FAMILY',
            'FIRE', 'FOOD', 'FREEDOM', 'GAMES', 'LUCK', 'MUSIC', 'SKY',
            'SILENCE', 'TRADE', 'TRAVEL', 'TRUTH', 'WEALTH',
            'NAME_BUILDING_TEMPLE', 'NAME_BUILDING_KEEP', 'NAME_WAR',
            'NAME_BATTLE', 'NAME_SIEGE', 'NAME_ROAD', 'NAME_TUNNEL',
            'NAME_BRIDGE', 'NAME_WALL', 'NAME_BUILDING_TOMB',
            'NAME_BUILDING_LIBRARY', 'NAME_FESTIVAL']

        # SELECT_SYMBOL
        self.symboldict = {}
        self.setsymbol = tk.Button(self, text='Set Symbol',
                                   command=lambda: self.add_symbol())
        self.setsymbol.grid(row=0, column=0, sticky=('w', 'e'))
        self.symbolnoun = ttk.Combobox(self, values=self.symbolnounlist)
        self.symbolnoun.grid(row=1, column=0, sticky=('w', 'e'))
        self.symbolnoun.set('ALL')
        self.symbol = ttk.Combobox(self, values=self.symbollist)
        self.symbol.grid(row=2, column=0, sticky=('w', 'e'))
        self.symbol.set('FLOWERY')
        self.removesymbol = tk.Button(self, text='Remove Symbol',
                                      command=lambda: self.remove_symbol())
        self.removesymbol.grid(row=3, column=0, sticky=('w', 'e'))
        self.symbols = tkst.ScrolledText(self, state='disabled', height=5,
                                         width=50, wrap=tk.WORD)
        self.symbols.grid(row=0, column=1, rowspan=4,
                          columnspan=4, sticky=('w', 'e'))

        # SUBSELECT_SYMBOL
        self.subsymboldict = {}
        self.setsubsymbol = tk.Button(self, text='Set SubSymbol',
                                      command=lambda: self.add_subsymbol())
        self.setsubsymbol.grid(row=4, column=0, sticky=('w', 'e'))
        self.subsymbolnoun = ttk.Combobox(self, values=self.symbolnounlist)
        self.subsymbolnoun.grid(row=5, column=0, sticky=('w', 'e'))
        self.subsymbolnoun.set('ALL')
        self.subsymbollist = []
        self.subsymbol = ttk.Combobox(self, values=self.subsymbollist)
        self.subsymbol.grid(row=6, column=0, sticky=('w', 'e'))
        self.removesubsymbol = tk.Button(
            self, text='Remove SubSymbol',
            command=lambda: self.remove_subsymbol())
        self.removesubsymbol.grid(row=7, column=0, sticky=('w', 'e'))
        self.subsymbols = tkst.ScrolledText(self, state='disabled', height=5,
                                            width=50, wrap=tk.WORD)
        self.subsymbols.grid(row=4, column=1, rowspan=4,
                             columnspan=4, sticky=('w', 'e'))

        # SELECT_SYMBOL
        self.cullsymboldict = {}
        self.setcullsymbol = tk.Button(self, text='Set Cull Symbol',
                                       command=lambda: self.add_cullsymbol())
        self.setcullsymbol.grid(row=8, column=0, sticky=('w', 'e'))
        self.cullsymbolnoun = ttk.Combobox(self, values=self.symbolnounlist)
        self.cullsymbolnoun.grid(row=9, column=0, sticky=('w', 'e'))
        self.cullsymbolnoun.set('ALL')
        self.cullsymbol = ttk.Combobox(self, values=self.symbollist)
        self.cullsymbol.grid(row=10, column=0, sticky=('w', 'e'))
        self.cullsymbol.set('FLOWERY')
        self.removecullsymbol = tk.Button(
            self, text='Remove Cull Symbol',
            command=lambda: self.remove_cullsymbol())
        self.removecullsymbol.grid(row=11, column=0, sticky=('w', 'e'))
        self.cullsymbols = tkst.ScrolledText(self, state='disabled', height=5,
                                             width=50, wrap=tk.WORD)
        self.cullsymbols.grid(row=8, column=1, rowspan=4,
                              columnspan=4, sticky=('w', 'e'))

    def add_symbol(self):
        self.symboldict[self.symbol.get()] = self.symbolnoun.get()
        self.fill_symbols()
        if self.symbol.get() not in self.subsymbollist:
            self.subsymbollist.append(self.symbol.get())
            self.subsymbol.config(values=self.subsymbollist)
            self.subsymbol.set(self.symbol.get())

    def remove_symbol(self):
        if self.symbol.get() in self.symboldict:
            self.symboldict.pop(self.symbol.get(), None)
        self.fill_symbols()
        if self.symbol.get() in self.subsymbollist:
            self.subsymbol.set('')
            self.subsymbollist.remove(self.symbol.get())
            self.subsymbol.config(values=self.subsymbollist)
            if self.symbol.get() in self.subsymboldict:
                self.subsymboldict.pop(self.symbol.get(), None)
                self.fill_subsymbols()

    def fill_symbols(self):
        string = ''
        for key, value in self.symboldict.items():
            string = string + value + ':' + key + ' '
        self.symbols.config(state='normal')
        self.symbols.delete('1.0', tk.END)
        self.symbols.insert('1.0', string)
        self.symbols.config(state='disabled')

    def add_subsymbol(self):
        if self.subsymbol.get() is not '':
            self.subsymboldict[self.subsymbol.get()] = self.subsymbolnoun.get()
            self.fill_subsymbols()

    def remove_subsymbol(self):
        if self.subsymbol.get() in self.subsymboldict:
            self.subsymboldict.pop(self.subsymbol.get(), None)
            self.fill_subsymbols()

    def fill_subsymbols(self):
        string = ''
        for key, value in self.subsymboldict.items():
            string = string + value + ':' + key + ' '
        self.subsymbols.config(state='normal')
        self.subsymbols.delete('1.0', tk.END)
        self.subsymbols.insert('1.0', string)
        self.subsymbols.config(state='disabled')

    def add_cullsymbol(self):
        self.cullsymboldict[self.cullsymbol.get()] = self.cullsymbolnoun.get()
        self.fill_cullsymbols()

    def remove_cullsymbol(self):
        if self.cullsymbol.get() in self.cullsymboldict:
            self.cullsymboldict.pop(self.cullsymbol.get(), None)
        self.fill_cullsymbols()

    def fill_cullsymbols(self):
        string = ''
        for key, value in self.cullsymboldict.items():
            string = string + value + ':' + key + ' '
        self.cullsymbols.config(state='normal')
        self.cullsymbols.delete('1.0', tk.END)
        self.cullsymbols.insert('1.0', string)
        self.cullsymbols.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    symbolsetup = SymbolSetup(root, padx=6, pady=6)
    note.add(symbolsetup, text='Flavor')
    note.grid()
    root.mainloop()
