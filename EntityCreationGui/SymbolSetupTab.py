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

    def add_symbol(self):
        self.symboldict[self.symbol.get()] = self.symbolnoun.get()
        self.fill_symbols()

    def remove_symbol(self):
        if self.symbol.get() in self.symboldict:
            self.symboldict.pop(self.supportedbiome.get(), None)
        self.fill_symbols()

    def fill_symbols(self):
        string = ''
        for key, value in self.symboldict.items():
            string = string + value + ':' + key + ' '
        self.symbols.config(state='normal')
        self.symbols.delete('1.0', tk.END)
        self.symbols.insert('1.0', string)
        self.symbols.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    symbolsetup = SymbolSetup(root, padx=6, pady=6)
    note.add(symbolsetup, text='Flavor')
    note.grid()
    root.mainloop()
