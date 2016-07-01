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

if __name__ == '__main__':
    root = tk.Tk()
    note = ttk.Notebook(root)
    religionsetup = ReligionSetup(root, padx=6, pady=6)
    note.add(religionsetup, text='Flavor')
    note.grid()
    root.mainloop()
