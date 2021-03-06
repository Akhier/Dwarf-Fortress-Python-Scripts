import tkinter as tk
import tkinter.ttk as ttk
import tkinter.scrolledtext as tkst


class ReligionSetup(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.spherelist = [
            'AGRICULTURE', 'ANIMALS', 'ART', 'BALANCE', 'BEAUTY', 'BIRTH',
            'BLIGHT', 'BOUNDARIES', 'CAVERNS', 'CHAOS', 'CHARITY', 'CHILDREN',
            'COASTS', 'CONSOLATION', 'COURAGE', 'CRAFTS', 'CREATION', 'DANCE',
            'DARKNESS', 'DAWN', 'DAY', 'DEATH', 'DEFORMITY', 'DEPRAVITY',
            'DISCIPLINE', 'DISEASE', 'DREAMS', 'DUSK', 'DUTY', 'EARTH',
            'FAMILY', 'FAME', 'FATE', 'FERTILITY', 'FESTIVALS', 'FIRE', 'FISH',
            'FISHING', 'FOOD', 'FORGIVENESS', 'FORTRESSES', 'FREEDOM',
            'GAMBLING', 'GAMES', 'GENEROSITY', 'HAPPINESS', 'HEALING',
            'HOSPITALITY', 'HUNTING', 'INSPIRATION', 'JEALOUSY', 'JEWELS',
            'JUSTICE', 'LABOR', 'LAKES', 'LAWS', 'LIES', 'LIGHT', 'LIGHTNING',
            'LONGEVITY', 'LOVE', 'LOYALTY', 'LUCK', 'LUST', 'MARRIAGE',
            'MERCY', 'METALS', 'MINERALS', 'MISERY', 'MIST', 'MOON',
            'MOUNTAINS', 'MUCK', 'MURDER', 'MUSIC', 'NATURE', 'NIGHT',
            'NIGHTMARES', 'OATHS', 'OCEANS', 'ORDER', 'PAINTING', 'PEACE',
            'PERSUASION', 'PLANTS', 'POETRY', 'PREGNANCY', 'RAIN', 'RAINBOWS',
            'REBIRTH', 'REVELRY', 'REVENGE', 'RIVERS', 'RULERSHIP', 'RUMORS',
            'SACRIFICE', 'SALT', 'SCHOLARSHIP', 'SEASONS', 'SILENCE', 'SKY',
            'SONG', 'SPEECH', 'STARS', 'STORMS', 'STRENGTH', 'SUICIDE', 'SUN',
            'THEFT', 'THRALLDOM', 'THUNDER', 'TORTURE', 'TRADE', 'TRAVELERS',
            'TREACHERY', 'TREES', 'TRICKERY', 'TRUTH', 'TWILIGHT', 'VALOR',
            'VICTORY', 'VOLCANOS', 'WAR', 'WATER', 'WEALTH', 'WEATHER', 'WIND',
            'WISDOM', 'WRITING', 'YOUTH']
        self.opposingspheredict = {
            'SPHERE_BEAUTY': ['SPHERE_BLIGHT', 'SPHERE_DEFORMITY',
                              'SPHERE_DISEASE', 'SPHERE_MUCK'],
            'SPHERE_BLIGHT': ['SPHERE_BEAUTY', 'SPHERE_FOOD',
                              'SPHERE_FERTILITY', 'SPHERE_HEALING'],
            'SPHERE_CHAOS': ['SPHERE_DISCIPLINE', 'SPHERE_ORDER',
                             'SPHERE_LAWS'],
            'SPHERE_CHARITY': ['SPHERE_JEALOUSY'],
            'SPHERE_CONSOLATION': ['SPHERE_MISERY'],
            'SPHERE_DARKNESS': ['SPHERE_DAWN', 'SPHERE_DAY', 'SPHERE_LIGHT',
                                'SPHERE_TWILIGHT', 'SPHERE_SUN'],
            'SPHERE_DAWN': ['SPHERE_NIGHT', 'SPHERE_DAY', 'SPHERE_DARKNESS'],
            'SPHERE_DAY': ['SPHERE_DARKNESS', 'SPHERE_NIGHT', 'SPHERE_DAWN',
                           'SPHERE_DUSK', 'SPHERE_DREAMS',
                           'SPHERE_NIGHTMARES', 'SPHERE_TWILIGHT'],
            'SPHERE_DEATH': ['SPHERE_HEALING', 'SPHERE_LONGEVITY',
                             'SPHERE_YOUTH'],
            'SPHERE_DEFORMITY': ['SPHERE_BEAUTY'],
            'SPHERE_DEPRAVITY': ['SPHERE_LAWS'],
            'SPHERE_DISCIPLINE': ['SPHERE_CHAOS'],
            'SPHERE_DISEASE': ['SPHERE_BEAUTY', 'SPHERE_HEALING'],
            'SPHERE_DREAMS': ['SPHERE_DAY'],
            'SPHERE_DUSK': ['SPHERE_NIGHT', 'SPHERE_DAY'],
            'SPHERE_FAME': ['SPHERE_SILENCE'],
            'SPHERE_FATE': ['SPHERE_LUCK'],
            'SPHERE_FERTILITY': ['SPHERE_BLIGHT'],
            'SPHERE_FESTIVALS': ['SPHERE_MISERY'],
            'SPHERE_FIRE': ['SPHERE_WATER', 'SPHERE_OCEANS',
                            'SPHERE_LAKES', 'SPHERE_RIVERS'],
            'SPHERE_FOOD': ['SPHERE_BLIGHT'],
            'SPHERE_FORGIVENESS': ['SPHERE_REVENGE'],
            'SPHERE_FREEDOM': ['SPHERE_ORDER'],
            'SPHERE_HAPPINESS': ['SPHERE_MISERY'],
            'SPHERE_HEALING': ['SPHERE_DISEASE', 'SPHERE_BLIGHT',
                               'SPHERE_DEATH'],
            'SPHERE_JEALOUSY': ['SPHERE_CHARITY'],
            'SPHERE_LAKES': ['SPHERE_FIRE'],
            'SPHERE_LAWS': ['SPHERE_CHAOS', 'SPHERE_DEPRAVITY',
                            'SPHERE_MURDER', 'SPHERE_THEFT'],
            'SPHERE_LIES': ['SPHERE_TRUTH'],
            'SPHERE_LIGHT': ['SPHERE_DARKNESS', 'SPHERE_TWILIGHT'],
            'SPHERE_LONGEVITY': ['SPHERE_DEATH'],
            'SPHERE_LOYALTY': ['SPHERE_TREACHERY'],
            'SPHERE_LUCK': ['SPHERE_FATE'],
            'SPHERE_MERCY': ['SPHERE_REVENGE'],
            'SPHERE_MISERY': ['SPHERE_CONSOLATION', 'SPHERE_FESTIVALS',
                              'SPHERE_REVELRY', 'SPHERE_HAPPINESS'],
            'SPHERE_MUCK': ['SPHERE_BEAUTY'],
            'SPHERE_MURDER': ['SPHERE_LAWS'],
            'SPHERE_MUSIC': ['SPHERE_SILENCE'],
            'SPHERE_NIGHT': ['SPHERE_DAY', 'SPHERE_DAWN',
                             'SPHERE_DUSK', 'SPHERE_TWILIGHT'],
            'SPHERE_NIGHTMARES': ['SPHERE_DAY'],
            'SPHERE_OATHS': ['SPHERE_TREACHERY'],
            'SPHERE_OCEANS': ['SPHERE_FIRE'],
            'SPHERE_ORDER': ['SPHERE_CHAOS', 'SPHERE_FREEDOM'],
            'SPHERE_REVELRY': ['SPHERE_MISERY'],
            'SPHERE_REVENGE': ['SPHERE_FORGIVENESS', 'SPHERE_MERCY'],
            'SPHERE_RIVERS': ['SPHERE_FIRE'],
            'SPHERE_SACRIFICE': ['SPHERE_WEALTH'],
            'SPHERE_SILENCE': ['SPHERE_FAME', 'SPHERE_MUSIC'],
            'SPHERE_SUN': ['SPHERE_DARKNESS'],
            'SPHERE_THEFT': ['SPHERE_LAWS', 'SPHERE_TRADE'],
            'SPHERE_TRADE': ['SPHERE_THEFT'],
            'SPHERE_TREACHERY': ['SPHERE_LOYALTY', 'SPHERE_OATHS'],
            'SPHERE_TRICKERY': ['SPHERE_TRUTH'],
            'SPHERE_TRUTH': ['SPHERE_LIES', 'SPHERE_TRICKERY'],
            'SPHERE_TWILIGHT': ['SPHERE_LIGHT', 'SPHERE_DARKNESS',
                                'SPHERE_DAY', 'SPHERE_NIGHT'],
            'SPHERE_WATER': ['SPHERE_FIRE'],
            'SPHERE_WEALTH': ['SPHERE_SACRIFICE'],
            'SPHERE_YOUTH': ['SPHERE_DEATH']}

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

        # RELIGION_SPHERE
        self.curspherelist = list(self.spherelist)
        self.selectedspheres = []
        self.setsphere = tk.Button(self, text='Set Sphere',
                                   command=lambda: self.add_sphere())
        self.setsphere.grid(row=1, column=0, sticky=('w', 'e'))
        self.sphere = ttk.Combobox(self, values=self.curspherelist)
        self.sphere.grid(row=2, column=0, sticky=('w', 'e'))
        self.sphere.set('AGRICULTURE')
        self.removesphere = tk.Button(self, text='Remove Sphere',
                                      command=lambda: self.remove_sphere())
        self.removesphere.grid(row=3, column=0, sticky=('w', 'e'))
        self.spheres = tkst.ScrolledText(self, state='disabled', height=4,
                                         width=50, wrap=tk.WORD)
        self.spheres.grid(row=1, column=1, rowspan=4,
                          columnspan=3, sticky=('w', 'e'))

    def add_sphere(self):
        if self.sphere.get() not in self.selectedspheres:
            self.selectedspheres.append(self.sphere.get())
            self.fill_spheres()

    def remove_sphere(self):
        if self.sphere.get() in self.selectedspheres:
            self.selectedspheres.remove(self.sphere.get())
            self.fill_spheres()

    def fill_spheres(self):
        string = ''
        self.selectedspheres.sort()
        for value in self.selectedspheres:
            if string is '':
                string = value
            else:
                string = string + ', ' + value
        self.spheres.config(state='normal')
        self.spheres.delete('1.0', tk.END)
        self.spheres.insert('1.0', string)
        self.spheres.config(state='disabled')

if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    religionsetup = ReligionSetup(root, padx=6, pady=6)
    note.add(religionsetup, text='Flavor')
    note.grid()
    root.mainloop()
