import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst
# combinedbiomes = {8660801552382:'ALL_MAIN', 268435454:'ANY_LAND', 268435440:'NOT_FREEZING', 29826816:'ANY_TROPICAL', 29761280:'ANY_TROPICAL_BROADLEAF', 8176:'ANY_WETLAND', 3719408:'ANY_TEMPERATE', 3703024:'ANY_TEMPERATE_BROADLEAF', 8658654068736:'ANY_LAKE', 135291469824:'ANY_POOL', 554153860399104:'ANY_RIVER', 507904:'ANY_FOREST', 240:'ANY_TEMPERATE_WETLAND', 7936:'ANY_TROPICAL_WETLAND', 234881024:'ANY_DESERT', 1879048192:'ANY_OCEAN', 962072674304:'ANY_TEMPERATE_LAKE', 61572651155456:'ANY_TEMPERATE_RIVER', 458752:'ANY_TROPICAL_FOREST', 7696581394432:'ANY_TROPICAL_LAKE', 492581209243648:'ANY_TROPICAL_RIVER', 1792:'ANY_TROPICAL_SWAMP', 4718592:'ANY_GRASSLAND', 9437184:'ANY_SAVANNA', 18874368:'ANY_SHRUBLAND', 49152:'ANY_TEMPERATE_FOREST', 192:'ANY_TEMPERATE_MARSH', 48:'ANY_TEMPERATE_SWAMP', 6144:'ANY_TROPICAL_MARSH'}
# singlebiomemask = {'MOUNTAIN':1<<1, 'GLACIER':1<<2, 'TUNDRA':1<<3, 'SWAMP_TEMPERATE_FRESHWATER':1<<4, 'SWAMP_TEMPERATE_SALTWATER':1<<5, 'MARSH_TEMPERATE_FRESHWATER':1<<6, 'MARSH_TEMPERATE_SALTWATER':1<<7, 'SWAMP_TROPICAL_FRESHWATER':1<<8, 'SWAMP_TROPICAL_SALTWATER':1<<9, 'SWAMP_MANGROVE':1<<10, 'MARSH_TROPICAL_FRESHWATER':1<<11, 'MARSH_TROPICAL_SALTWATER':1<<12, 'FOREST_TAIGA':1<<13, 'FOREST_TEMPERATE_CONIFER':1<<14, 'FOREST_TEMPERATE_BROADLEAF':1<<15, 'FOREST_TROPICAL_CONIFER':1<<16, 'FOREST_TROPICAL_DRY_BROADLEAF':1<<17, 'FOREST_TROPICAL_MOIST_BROADLEAF':1<<18, 'GRASSLAND_TEMPERATE':1<<19, 'SAVANNA_TEMPERATE':1<<20, 'SHRUBLAND_TEMPERATE':1<<21, 'GRASSLAND_TROPICAL':1<<22, 'SAVANNA_TROPICAL':1<<23, 'SHRUBLAND_TROPICAL':1<<24, 'DESERT_BADLAND':1<<25, 'DESERT_ROCK':1<<26, 'DESERT_SAND':1<<27, 'OCEAN_TROPICAL':1<<28, 'OCEAN_TEMPERATE':1<<29, 'OCEAN_ARCTIC':1<<30, 'POOL_TEMPERATE_FRESHWATER':1<<31, 'POOL_TEMPERATE_BRACKISHWATER':1<<32, 'POOL_TEMPERATE_SALTWATER':1<<33, 'POOL_TROPICAL_FRESHWATER':1<<34, 'POOL_TROPICAL_BRACKISHWATER':1<<35, 'POOL_TROPICAL_SALTWATER':1<<36, 'LAKE_TEMPERATE_FRESHWATER':1<<37, 'LAKE_TEMPERATE_BRACKISHWATER':1<<38, 'LAKE_TEMPERATE_SALTWATER':1<<39, 'LAKE_TROPICAL_FRESHWATER':1<<40, 'LAKE_TROPICAL_BRACKISHWATER':1<<41, 'LAKE_TROPICAL_SALTWATER':1<<42, 'RIVER_TEMPERATE_FRESHWATER':1<<43, 'RIVER_TEMPERATE_BRACKISHWATER':1<<44, 'RIVER_TEMPERATE_SALTWATER':1<<45, 'RIVER_TROPICAL_FRESHWATER':1<<46, 'RIVER_TROPICAL_BRACKISHWATER':1<<47, 'RIVER_TROPICAL_SALTWATER':1<<48, 'SUBTERRANEAN_WATER':1<<49, 'SUBTERRANEAN_CHASM':1<<50, 'SUBTERRANEAN_LAVA':1<<51}


class BasicSetup(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.singlebiomelist = ['MOUNTAIN', 'MARSH_TEMPERATE_FRESHWATER', 'SWAMP_TROPICAL_SALTWATER', 'MARSH_TROPICAL_SALTWATER',
                                'FOREST_TEMPERATE_BROADLEAF', 'FOREST_TROPICAL_MOIST_BROADLEAF', 'SHRUBLAND_TEMPERATE',
                                'DESERT_BADLAND', 'OCEAN_ARCTIC', 'POOL_TEMPERATE_SALTWATER', 'POOL_TROPICAL_SALTWATER',
                                'LAKE_TEMPERATE_SALTWATER', 'LAKE_TROPICAL_SALTWATER', 'RIVER_TEMPERATE_SALTWATER',
                                'RIVER_TROPICAL_SALTWATER', 'GLACIER', 'MARSH_TEMPERATE_SALTWATER', 'SWAMP_MANGROVE',
                                'FOREST_TAIGA', 'FOREST_TROPICAL_CONIFER', 'GRASSLAND_TEMPERATE', 'GRASSLAND_TROPICAL',
                                'DESERT_ROCK', 'POOL_TEMPERATE_FRESHWATER', 'POOL_TROPICAL_FRESHWATER', 'LAKE_TEMPERATE_FRESHWATER',
                                'LAKE_TROPICAL_FRESHWATER', 'RIVER_TEMPERATE_FRESHWATER', 'RIVER_TROPICAL_FRESHWATER',
                                'SUBTERRANEAN_WATER', 'TUNDRA', 'SWAMP_TROPICAL_FRESHWATER', 'MARSH_TROPICAL_FRESHWATER',
                                'FOREST_TEMPERATE_CONIFER', 'FOREST_TROPICAL_DRY_BROADLEAF', 'SAVANNA_TEMPERATE',
                                'SAVANNA_TROPICAL', 'DESERT_SAND', 'POOL_TEMPERATE_BRACKISHWATER', 'POOL_TROPICAL_BRACKISHWATER',
                                'LAKE_TEMPERATE_BRACKISHWATER', 'LAKE_TROPICAL_BRACKISHWATER', 'RIVER_TEMPERATE_BRACKISHWATER',
                                'RIVER_TROPICAL_BRACKISHWATER', 'SUBTERRANEAN_CHASM', 'SWAMP_TEMPERATE_FRESHWATER',
                                'SHRUBLAND_TROPICAL', 'OCEAN_TROPICAL', 'SUBTERRANEAN_LAVA', 'SWAMP_TEMPERATE_SALTWATER',
                                'OCEAN_TEMPERATE']
        self.sitetypelist = ['DARK_FORTRESS', 'CAVE', 'CAVE_DETAILED', 'TREE_CITY', 'CITY']

        # OUTSIDER_CONTROLLABLE
        self.outcon = tk.IntVar()
        self.outsidercontrollable = tk.Checkbutton(self, variable=self.outcon,
                                                   text='Outsider '
                                                   'Controllable',
                                                   command=lambda:
                                                   self.toggle_alladvtier())
        self.outsidercontrollable.grid(row=0, column=0, sticky='w')

        # SITE_CONTROLLABLE
        self.sitecon = tk.IntVar()
        self.sitecontrollable = tk.Checkbutton(self, variable=self.sitecon,
                                               text='Site Controllable')
        self.sitecontrollable.grid(row=0, column=1, sticky='w')

        # ADVENTURE_TIER
        self.advtiernum = tk.Spinbox(self, from_=1, to=9001)
        self.advtiercheck = tk.IntVar()
        self.advtier = tk.Checkbutton(self, variable=self.advtiercheck,
                                      text='Adventure Tier',
                                      command=lambda: self.toggle_advtier())
        self.advtier.grid(row=1, column=0, sticky='w')
        self.advtiernum.delete(0, 'end')
        self.advtiernum.insert(0, 4)
        self.advtiernum.configure(state='disabled')
        self.advtiernum.grid(row=1, column=1, sticky='w')

        # CREATURE
        self.creaturelabel = tk.Label(self, justify='left', text='Creature:').grid(row=1, column=2, sticky='e')
        self.creature = ''
        self.creatureentry = tk.Entry(self, textvariable=self.creature).grid(row=1, column=3, sticky='w')

        # START_BIOME|EXCLUSIVE_START_BIOME
        self.startinglist = []
        self.startbiome = ttk.Combobox(self, values=self.singlebiomelist)
        self.startbiome.grid(row=3, column=0, sticky=('w', 'e'))
        self.startbiome.set('MOUNTAIN')
        self.startbiomes = tkst.ScrolledText(self, state='disabled', height=4, width=50, wrap=tk.WORD)
        self.startbiomes.grid(row=2, column=1, columnspan=3, rowspan=3, sticky=('w', 'e'))
        self.setstartbiome = tk.Button(self, text='Set Start Biome',
                                       command=lambda biome=self.startbiome, biomes=self.startbiomes,
                                       list=self.startinglist: self.add_biome(biome, biomes, list))
        self.setstartbiome.grid(row=2, column=0, sticky=('w', 'e'))
        self.removestartbiome = tk.Button(self, text='Remove Start Biome',
                                          command=lambda biome=self.startbiome, biomes=self.startbiomes,
                                          list=self.startinglist: self.remove_biome(biome, biomes, list))
        self.removestartbiome.grid(row=4, column=0, sticky=('w', 'e'))

        # SETTLEMENT_BIOME
        self.settlementlist = []
        self.settlementbiome = ttk.Combobox(self, values=self.singlebiomelist)
        self.settlementbiome.grid(row=6, column=0, sticky=('w', 'e'))
        self.settlementbiome.set('MOUNTAIN')
        self.settlementbiomes = tkst.ScrolledText(self, state='disabled', height=4, width=50, wrap=tk.WORD)
        self.settlementbiomes.grid(row=5, column=1, columnspan=3, rowspan=3, sticky=('w', 'e'))
        self.setsettlementbiome = tk.Button(self, text='Set Settlement Biome',
                                            command=lambda settlementbiome=self.settlementbiome, settlementbiomes=self.settlementbiomes,
                                            list=self.settlementlist: self.add_settlementbiome(settlementbiome, settlementbiomes, list))
        self.setsettlementbiome.grid(row=5, column=0, sticky=('w', 'e'))
        self.removesettlementbiome = tk.Button(self, text='Remove Settlement Biome',
                                               command=lambda settlementbiome=self.settlementbiome, settlementbiomes=self.settlementbiomes,
                                               list=self.settlementlist: self.remove_settlementbiome(settlementbiome, settlementbiomes, list))
        self.removesettlementbiome.grid(row=7, column=0, sticky=('w', 'e'))

        # BIOME_SUPPORT
        self.supporteddict = {}
        self.frequencyofbiome = tk.Spinbox(self, from_=0, to=10, justify='center')
        self.frequencyofbiome.grid(row=10, column=0, sticky=('w', 'e'))
        self.supportedbiome = ttk.Combobox(self, values=self.singlebiomelist)
        self.supportedbiome.grid(row=9, column=0, sticky=('w', 'e'))
        self.supportedbiome.set('MOUNTAIN')
        self.supportedbiomes = tkst.ScrolledText(self, state='disabled', height=5, width=50, wrap=tk.WORD)
        self.supportedbiomes.grid(row=8, column=1, columnspan=3, rowspan=4, sticky=('w', 'e'))
        self.setsupportedbiome = tk.Button(self, text='Set Supported Biome',
                                           command=lambda: self.add_supportedbiome())
        self.setsupportedbiome.grid(row=8, column=0, sticky=('w', 'e'))
        self.removesupportedbiome = tk.Button(self, text='Remove Supported Biome',
                                              command=lambda: self.remove_supportedbiome())
        self.removesupportedbiome.grid(row=11, column=0, sticky=('w', 'e'))

        # DEFAULT_SITE_TYPE
        tk.Label(self, text='Default Site Type:   ', justify='left').grid(row=12, column=1, sticky='e')
        self.defaultsite = ttk.Combobox(self, values=self.sitetypelist)
        self.defaultsite.grid(row=12, column=2, sticky='w')

        # SITE_TOLERANCE
        self.ToLi = tk.IntVar()
        self.sitetolerancedict = {}
        self.sites = ttk.Combobox(self, values=self.sitetypelist)
        self.sites.grid(row=14, column=0, sticky=('w', 'e'))
        self.sites.set('DARK_FORTRESS')
        self.like = ttk.Radiobutton(self, text='LIKES', variable=self.ToLi, value=1)
        self.like.grid(row=15, column=0, sticky=('w'))
        self.tolerate = ttk.Radiobutton(self, text='TOLERATES', variable=self.ToLi, value=2)
        self.tolerate.grid(row=15, column=0, sticky=('e'))
        self.ToLi.set(1)
        self.toleratedsites = tkst.ScrolledText(self, state='disabled', height=3, width=50, wrap=tk.WORD)
        self.toleratedsites.grid(row=14, column=2, columnspan=2, rowspan=2, sticky=('w', 'e'))
        self.setsitetolerance = tk.Button(self, text='Set Site Tolerance',
                                          command=lambda: self.add_sitetolerance())
        self.setsitetolerance.grid(row=14, column=1, sticky=('w', 'e'))
        self.removesitetolerance = tk.Button(self, text='Remove Site Tolerance',
                                             command=lambda: self.remove_sitetolerance())
        self.removesitetolerance.grid(row=15, column=1, sticky=('w', 'e'))

        # WORLD_CONSTRUCTION
        self.constructionlabel = tk.Label(self, justify='center', text='World Construction Options').grid(row=16, column=0, columnspan=4, sticky=('w', 'e'))
        self.roads = tk.IntVar()
        self.roadconstruction = tk.Checkbutton(self, variable=self.roads, text='ROAD')
        self.roadconstruction.grid(row=17, column=0, sticky='w')
        self.tunnels = tk.IntVar()
        self.tunnelconstruction = tk.Checkbutton(self, variable=self.tunnels, text='TUNNEL')
        self.tunnelconstruction.grid(row=17, column=1, sticky='w')
        self.bridges = tk.IntVar()
        self.bridgeconstruction = tk.Checkbutton(self, variable=self.bridges, text='BRIDGE')
        self.bridgeconstruction.grid(row=17, column=2, sticky='w')
        self.walls = tk.IntVar()
        self.wallconstruction = tk.Checkbutton(self, variable=self.walls, text='WALL')
        self.wallconstruction.grid(row=17, column=3, sticky='w')

        # POPULATION
        self.maxpoplabel = tk.Label(self, justify='center', text='MAX_POP_NUMBER').grid(row=18, column=0, sticky=('w', 'e'))
        self.maxpop = tk.Spinbox(self, from_=0, to=9999999999999, justify='center')
        self.maxpop.grid(row=19, column=0, sticky=('w', 'e'))
        self.maxpop.delete(0, 'end')
        self.maxpop.insert(0, 500)
        self.maxsitepoplabel = tk.Label(self, justify='center', text='MAX_SITE_POP_NUMBER').grid(row=18, column=1, sticky=('w', 'e'))
        self.maxsitepop = tk.Spinbox(self, from_=0, to=9999999999999, justify='center')
        self.maxsitepop.grid(row=19, column=1, sticky=('w', 'e'))
        self.maxsitepop.delete(0, 'end')
        self.maxsitepop.insert(0, 200)
        self.maxstartingcivlabel = tk.Label(self, justify='center', text='MAX_STARTING_CIV_NUMBER').grid(row=18, column=2, sticky=('w', 'e'))
        self.maxstartingciv = tk.Spinbox(self, from_=0, to=300, justify='center')
        self.maxstartingciv.grid(row=19, column=2, sticky=('w', 'e'))
        self.maxstartingciv.delete(0, 1)
        self.maxstartingciv.insert(0, 3)

    def toggle_alladvtier(self):
        if self.outcon.get():
            self.advtier.configure(state='disabled')
            self.advtiernum.configure(state='disabled')
        else:
            self.advtier.configure(state='normal')
            self.toggle_advtier()

    def toggle_advtier(self):
        if self.advtiercheck.get():
            self.advtiernum.configure(state='normal')
        else:
            self.advtiernum.configure(state='disabled')

    def fill_biomes(self, biomes, list):
        biomes.config(state='normal')
        biomes.delete('1.0', tk.END)
        biomes.insert('1.0', str(list).strip('[]'))
        biomes.config(state='disabled')

    def add_biome(self, biome, biomes, list):
        if biome.get() not in list:
            list.append(biome.get())
            self.fill_biomes(biomes, list)

    def remove_biome(self, biome, biomes, list):
        if biome.get() in list:
            list.remove(biome.get())
            self.fill_biomes(biomes, list)

    def fill_settlementbiomes(self, settlementbiomes, list):
        settlementbiomes.config(state='normal')
        settlementbiomes.delete('1.0', tk.END)
        settlementbiomes.insert('1.0', str(list).strip('[]'))
        settlementbiomes.config(state='disabled')

    def add_settlementbiome(self, settlementbiome, settlementbiomes, list):
        if settlementbiome.get() not in list:
            list.append(settlementbiome.get())
            self.fill_settlementbiomes(settlementbiomes, list)

    def remove_settlementbiome(self, settlementbiome, settlementbiomes, list):
        if settlementbiome.get() in list:
            list.remove(settlementbiome.get())
            self.fill_settlementbiomes(settlementbiomes, list)

    def fill_supportedbiomes(self):
        string = ''
        for key, value in self.supporteddict.items():
            string = string + key + ':' + value + ' '

        self.supportedbiomes.config(state='normal')
        self.supportedbiomes.delete('1.0', tk.END)
        self.supportedbiomes.insert('1.0', string)
        self.supportedbiomes.config(state='disabled')

    def add_supportedbiome(self):
        self.supporteddict[self.supportedbiome.get()] = self.frequencyofbiome.get()

        self.fill_supportedbiomes()

    def remove_supportedbiome(self):
        if self.supportedbiome.get() in self.supporteddict:
            self.supporteddict.pop(self.supportedbiome.get(), None)

        self.fill_supportedbiomes()

    def fill_sitetolerances(self):
        string = ''
        for key, value in self.sitetolerancedict.items():
            string = string + key + ':' + value + ' '

        self.toleratedsites.config(state='normal')
        self.toleratedsites.delete('1.0', tk.END)
        self.toleratedsites.insert('1.0', string)
        self.toleratedsites.config(state='disabled')

    def add_sitetolerance(self):
        if self.ToLi.get() == 1:
            self.sitetolerancedict[self.sites.get()] = 'LIKES'
        else:
            self.sitetolerancedict[self.sites.get()] = 'TOLERATES'

        self.fill_sitetolerances()

    def remove_sitetolerance(self):
        if self.sites.get() in self.sitetolerancedict:
            self.sitetolerancedict.pop(self.sites.get(), None)

        self.fill_sitetolerances()

if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    basicsetup = BasicSetup(root, padx=6, pady=6)
    note.add(basicsetup, text='Basics')
    note.grid()
    root.mainloop()
