from tkinter import *
from tkinter import ttk
from main import create_loot_list, checkBudget, priceFormat, flags


def click():
    encounterCR = comboCR.get()
    campaignSpeed = (comboSpeed.get()).lower()
    treasureType = (comboType.get()).lower()
    try:
        results = create_loot_list(encounterCR,campaignSpeed,treasureType)
    except:
        results = "Error generating loot"
    output.config(state=NORMAL)
    output.delete("1.0", END)
    if results == "Error generating loot":
        output.insert(END, results)
    else:
        for item in sorted(results, key=lambda item: item.name):
            fprice = priceFormat(item.price)
            if item.quantity > 1:
                output.insert(END, "{}x {} ({} each)".format(item.quantity, item.name, fprice) + '\n')
            else:
                output.insert(END, "{} ({})".format(item.name, fprice) + '\n')
        output.insert(END, "\n")

        if int(checkBudget('p')) > 0:
            output.insert(END, "Coins: " + str(checkBudget('p')) + " pp, " + str(checkBudget('g')) + " gp, " +
                          str(checkBudget('s')) + " sp, " + str(checkBudget('c')) + " cp.")
        elif int(checkBudget('g')) > 0:
            output.insert(END, "Coins: " + str(checkBudget('g')) + " gp, " + str(checkBudget('s')) + " sp, " +
                      str(checkBudget('c')) + " cp.")
        elif int(checkBudget('s')) > 0:
            output.insert(END, "Coins: " + str(checkBudget('s')) + " sp, " + str(checkBudget('c')) + " cp.")
        else:
            output.insert(END, "Coins: " + str(checkBudget('c')) + " cp.")
        if len(results) > 22:
            scrollb.grid(row=12, column=4, sticky=NSEW)
        else:
            '''scrollb.grid_forget()'''
    output.config(state=DISABLED)


class SettingsWindow(Toplevel):
    def __init__(self):
        super().__init__(master= app, bg='#84344D')
        self.title("Settings")
        self.geometry("326x485")
        self.focus_force()
        self.grab_set()

        # Title
        Label(self, text='                     ', bg='#84344D', fg='white', font='none 3 bold').grid(row=0, column=0)
        Label(self, text='Settings', bg='#84344D', fg='white', font='none 13 bold').grid(row=1, column=2, columnspan=3,
                                                                                         sticky=NSEW)
        Label(self, text='', bg='#84344D', fg='white', font='none 3 bold').grid(row=2, column=4)

        # Eastern Items Checkbox
        Label(self, text='Eastern Items', bg='#84344D', fg='white', font='none 11 bold').grid(row=3, column=2,
                                                                                              sticky=E)
        self.check_eas = IntVar()
        if flags['set_eas']:
            self.check_eas.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_eas).grid(row=3, column=3)

        # Stone Age Items Checkbox
        Label(self, text='Stone Age Items', bg='#84344D', fg='white', font='none 11 bold').grid(row=4, column=2,
                                                                                                sticky=E)
        self.check_stn = IntVar()
        if flags['set_stn']:
            self.check_stn.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_stn).grid(row=4, column=3)

        # Bronze Age Items Checkbox
        Label(self, text='Bronze Age Items', bg='#84344D', fg='white', font='none 11 bold').grid(row=5, column=2,
                                                                                                 sticky=E)
        self.check_brz = IntVar()
        if flags['set_brz']:
            self.check_brz.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_brz).grid(row=5, column=3)

        # Early Firearms Checkbox
        Label(self, text='Early Firearms', bg='#84344D', fg='white', font='none 11 bold').grid(row=6, column=2,
                                                                                               sticky=E)
        self.check_efire = IntVar()
        if flags['set_efire']:
            self.check_efire.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_efire).grid(row=6, column=3)

        # Advanced Firearms Checkbox
        Label(self, text='Advanced Firearms', bg='#84344D', fg='white', font='none 11 bold').grid(row=7, column=2,
                                                                                                  sticky=E)
        self.check_afire = IntVar()
        if flags['set_afire']:
            self.check_afire.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_afire).grid(row=7, column=3)

        # Modern Firearms Checkbox
        Label(self, text='Modern Firearms', bg='#84344D', fg='white', font='none 11 bold').grid(row=8, column=2,
                                                                                                sticky=E)
        self.check_mfire = IntVar()
        if flags['set_mfire']:
            self.check_mfire.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_mfire).grid(row=8, column=3)

        # Mythic Items Checkbox
        Label(self, text='Mythic Items', bg='#84344D', fg='white', font='none 11 bold').grid(row=9, column=2,
                                                                                             sticky=E)
        self.check_mth = IntVar()
        if flags['set_mth']:
            self.check_mth.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_mth).grid(row=9, column=3)

        # Worldscape Checkbox
        Label(self, text='Setting: Worldscape', bg='#84344D', fg='white', font='none 11 bold').grid(row=10, column=2,
                                                                                                    sticky=E)
        self.check_wdsp = IntVar()
        if flags['set_wdsp']:
            self.check_wdsp.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_wdsp).grid(row=10, column=3)

        # 3.5ed Paizo Items Checkbox
        Label(self, text='3.5 Ed Paizo Items', bg='#84344D', fg='white', font='none 11 bold').grid(row=11, column=2,
                                                                                                   sticky=E)
        self.check_dnd = IntVar()
        if flags['src_dnd']:
            self.check_dnd.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_dnd).grid(row=11, column=3)

        # linebreak
        Label(self, text='', bg='#84344D', fg='white', font='none 3 bold').grid(row=12, column=0)

        # Special Materials Checkbox
        Label(self, text='Use Special Materials', bg='#84344D', fg='white', font='none 11 bold').grid(row=13, column=2,
                                                                                             sticky=E)
        self.check_mats = IntVar()
        if flags['flg_mats']:
            self.check_mats.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_mats).grid(row=13, column=3)

        # Magical Weapons/Armor Generation Checkbox
        Label(self, text='Generate Magical Weapons/Armor', bg='#84344D', fg='white', font='none 11 bold').grid(row=14, column=2,
                                                                                             sticky=E)
        self.check_ench = IntVar()
        if flags['flg_ench']:
            self.check_ench.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_ench).grid(row=14, column=3)

        # Modifications Checkbox
        Label(self, text='Armor/Weapon Modification*', bg='#84344D', fg='white', font='none 11 bold').grid(row=15, column=2,
                                                                                             sticky=E)
        self.check_mods = IntVar()
        if flags['flg_mods']:
            self.check_ench.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_mods).grid(row=15, column=3)

        # linebreak
        Label(self, text='', bg='#84344D', fg='white', font='none 3 bold').grid(row=16, column=0)

        # Cursed Items Checkbox
        Label(self, text='Cursed Items', bg='#84344D', fg='white', font='none 11 bold').grid(row=17, column=2,
                                                                                             sticky=E)
        self.check_cur = IntVar()
        if flags['loot_cur']:
            self.check_cur.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_cur).grid(row=17, column=3)

        # Artifacts Checkbox
        Label(self, text='Artifacts', bg='#84344D', fg='white', font='none 11 bold').grid(row=18, column=2,
                                                                                             sticky=E)
        self.check_art = IntVar()
        if flags['loot_art']:
            self.check_art.set(1)
        Checkbutton(self, bg='#84344D', activebackground='#84344D', variable=self.check_art).grid(row=18, column=3)

        # linebreak
        Label(self, text='', bg='#84344D', fg='white', font='none 3 bold').grid(row=19, column=0)

        #Save Settings button
        Button(self, text='Save Settings', width=8, command=self.savesettings) .grid(row=20, column=2, columnspan=2,
                                                                                     sticky=EW)

    def savesettings(self):
        flags['set_eas'] = bool(self.check_eas.get())
        flags['set_stn'] = bool(self.check_stn.get())
        flags['set_brz'] = bool(self.check_brz.get())
        flags['set_efire'] = bool(self.check_efire.get())
        flags['set_afire'] = bool(self.check_afire.get())
        flags['set_mfire'] = bool(self.check_mfire.get())
        flags['set_mth'] = bool(self.check_mth.get())
        flags['set_wdsp'] = bool(self.check_wdsp.get())
        flags['src_dnd'] = bool(self.check_dnd.get())

        flags['flg_mats'] = bool(self.check_mats.get())
        flags['flg_ench'] = bool(self.check_ench.get())
        flags['flg_mods'] = bool(self.check_mods.get())

        flags['loot_cur'] = bool(self.check_cur.get())
        flags['loot_art'] = bool(self.check_art.get())


# main:
app = Tk()
app.title("Pathfinder Encounter Treasure  Generator V0.1")
app.configure(background='#84344D', bd=20)
app.option_add('*TCombobox*Listbox.font',"none 11")


# create label
Label (app, text=" Rai's Encounter Treasure Generator", bg='#84344D', fg="white",
       font="none 14 bold") .grid(row=0, column=0, columnspan=4, sticky=NS)

# settings button
img = PhotoImage(file='settings_icon.png')
settings = Button(app, image=img, bg='#84344D', activebackground='#84344D', border=0, command=SettingsWindow) \
    .grid(row=10, column=3, sticky=NSEW)


# whitespace
Label (app, text="   ", bg='#84344D', fg='white', font="none 10") .grid(row=0, column=0, sticky=E)
Label (app, text="", bg='#84344D', fg='white', font="none 10") .grid(row=2, column=3, sticky=EW)

# encounter CR dropdown
Label (app, text="Encounter CR:", bg='#84344D', fg='white', font="none 12 bold") .grid(row=3, column=1, sticky=E)
comboCR = ttk.Combobox(app, values=['1/8', '1/6', '1/4', '1/3', '1/2', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
                                    15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30],
                                    font="none 12", state="readonly", width=12)
comboCR.current(5)
comboCR.grid(row=3, column=2, sticky=W)

# whitespace
Label(app, text="   ", bg='#84344D', fg='white', font="none 10") .grid(row=4, column=4, sticky=E)

# campaign speed dropdown
Label(app, text="Campaign Speed:", bg='#84344D', fg='white', font="none 12 bold") .grid(row=5, column=1, sticky=E)
comboSpeed = ttk.Combobox(app, values=['Slow', 'Medium', 'Fast'], font="none 12", state="readonly", width=12)
comboSpeed.current(2)
comboSpeed.grid(row=5, column=2, sticky=W)

# whitespace
Label(app, text="", bg='#84344D', fg='white', font="none 10") .grid(row=6, column=3, sticky=E)

# treasure type dropdown
Label(app, text="Treasure Type:", bg='#84344D', fg='white', font="none 12 bold") .grid(row=7, column=1, sticky=E)
comboType = ttk.Combobox(app, values=['Incidental', 'Standard', 'Double', 'Triple'], font="none 12", state="readonly",
                         width=12)
comboType.current(1)
comboType.grid(row=7, column=2, sticky=W)

# whitespace
Label(app, text="", bg='#84344D', fg='white', font="none 10") .grid(row=8, column=3, sticky=E)

# submit button
Button(app, text="GENERATE", width=10, command=click) .grid(row=10, column=1, columnspan=2, sticky=EW)

# whitespace
Label(app, text="", bg='#84344D', fg='white', font="none 10") .grid(row=11, column=3, sticky=E)

# results box
output = Text(app, wrap=WORD, bg='#B08A95', fg='white', state="normal", font="none 11", relief=GROOVE)
output.grid(row=12, column=0, columnspan=4, sticky=EW)
scrollb = Scrollbar(app, command=output.yview)
scrollb.grid(row=12, column=4, sticky=NSEW)
output['yscrollcommand'] = scrollb.set



##### run the main loop
app.mainloop()