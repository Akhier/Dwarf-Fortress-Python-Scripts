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


if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    symbolsetup = SymbolSetup(root, padx=6, pady=6)
    note.add(symbolsetup, text='Flavor')
    note.grid()
    root.mainloop()
