"""RANDOM LOOT GENERATOR PF1E STARTER PROJECT"""

import json
from copy import deepcopy as deepcopy
from random import randint, choices, choice
from fractions import Fraction
from math import floor
from configparser import ConfigParser

'''Global Variables'''
lootBudget = 1
cashBudget = float(lootBudget / 10)
encounterLoot = {}
encounterLootList = []
lootlist = []
itemlist = []
materialslist = []
enchantmentlist = []
fulllist = []
templist = []
config = ConfigParser()

lfrequency = []
pfrequency = []
sfrequency = []
wfrequency = []
list_wench = []
list_rench = []
list_aench = []
list_sench = []
list_mench = []
list_mods = []

potionlist = []
scrolllist = []
wandlist = []
errorCount = 0

'''object lists'''
list_nmi = []
list_nma = []
list_nmw = []
list_nmu = []
list_ma = []
list_mw = []
list_mu = []
list_st = []
list_ro = []
list_ri = []
list_wie = []
list_wis = []

list_cur = []
list_art = []

list_pot = []
list_wnd = []
list_scr = []

### config ###
config.read('config.ini')


class Item:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])
            self.quantity = 1
            self.is_Mwk = False
            self.enchant_cost = 0
            self.l_itemEnch = []
            self.material = ""
            self.forename = ""

    def updateprice(self, num):
        self.price = float(self.price) + float(num)

    def composite(self):
        roll = randint(1, 6)
        self.name = self.name.replace("+", "[+" + str(roll - 1) + "]")
        self.price = int(self.price) * roll

    def ammoquantity(self):
        roll = randint(2, 50)
        self.name = self.name.replace("*", "- (" + str(roll) + ")")
        self.price = float(self.price) * float(roll)
        self.aquantity = roll

    def slayingtype(self):
        listtypes = ['Aberration', 'Animal', 'Construct', 'Dragon', 'Fey', 'Humanoid (Aquatic)',
                     'Humanoid (Dwarf)', 'Humanoid (Elf)', 'Humanoid (Giant)', 'Humanoid (Gnoll)',
                     'Humanoid (Gnomes)', 'Humanoid (Goblinoid)', 'Humanoid (Halfling)', 'Humanoid (Human)',
                     'Humanoid (Reptilian)', 'Humanoids (Orc)', 'Magical Beast', 'Monstrous Humanoid', 'Ooze',
                     'Outsider (Air)', 'Outsider (Chaotic)', 'Outsider (Earth)', 'Outsider (Evil)',
                     'Outsider (Fire)', 'Outsider (Good)', 'Outsider (Lawful)', 'Outsider (Water)', 'Plant',
                     'Undead', 'Vermin']
        lweights = [5, 4, 7, 11, 5, 1, 2, 2, 7, 1, 1, 3, 1, 4, 3, 3, 5, 5, 2, 1, 3, 1, 3, 1, 3, 3, 1, 2, 8, 2]

        ctype = choices(listtypes, lweights, k=1)[0]
        self.name = self.name.replace('Slaying Arrow ^', 'Arrow of ' + ctype + ' Slaying')

    def __repr__(self):
        return "Name: " + self.name + "  Price: " + str(self.price) + " gp" + "  Weight: " + str(
            self.weight) + " lb" + \
               "  Slot: " + self.slot + "  Frequency: " + str(self.frequency) + "  Source: " + self.source


class Spelltoitem:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])
            self.price = 0
            self.weight = 0
            self.material = ""
            self.is_Mwk = False

    def calculate_potion_price(self):
        if self.min_spell_level == '0':
            self.price = 25
        elif self.min_spell_level == '1':
            self.price = 50
        elif self.min_spell_level == '2':
            if self.caster == "9th-P":
                self.price = 300
            else:
                self.price = 400
        elif self.min_spell_level == '3':
            if self.caster == "9th-P":
                self.price = 750
            elif self.caster == "9th-S":
                self.price = 900
            else:
                self.price = 1050
        else:
            print("Potion generation failed on" + self.name)

    def calculate_wand_price(self):
        if self.min_spell_level == '0':
            self.price = 375
        elif self.min_spell_level == '1':
            self.price = 750
        elif self.min_spell_level == '2':
            if self.caster == "9th-P":
                self.price = 4500
            else:
                self.price = 6000
        elif self.min_spell_level == '3':
            if self.caster == "9th-P":
                self.price = 11250
            elif self.caster == "9th-S":
                self.price = 13500
            else:
                self.price = 15750
        elif self.min_spell_level == '4':
            if self.caster == "9th-P":
                self.price = 21000
            elif self.caster == "9th-S":
                self.price = 24000
            else:
                self.price = 30000
        else:
            print("Wand generation failed on" + self.name)

    def calculate_scroll_price(self):
        cost_9p = {'0': 12.5, '1': 25, '2': 150, '3': 375, '4': 700, '5': 1125, '6': 1650, '7': 2275, '8': 3000,
                   '9': 3825}
        cost_9s = {'0': 12.5, '1': 25, '2': 200, '3': 450, '4': 800, '5': 1250, '6': 1800, '7': 2450, '8': 3200,
                   '9': 4050}
        cost_6 = {'0': 12.5, '1': 25, '2': 200, '3': 525, '4': 1000, '5': 1625, '6': 2400}
        cost_4 = {'1': 25, '2': 200, '3': 525, '4': 1000}

        if self.caster == "9th-P":
            self.price = cost_9p[self.min_spell_level]
        elif self.caster == "9th-S":
            self.price = cost_9s[self.min_spell_level]
        elif self.caster == "6th":
            self.price = cost_6[self.min_spell_level]
        elif self.caster == "4th":
            self.price = cost_4[self.min_spell_level]
        else:
            print("Error generating scroll price")

    def name_pot(self):
        self.forename = "Potion of "

    def name_wand(self):
        self.forename = "Wand of "

    def name_scroll(self):
        self.forename = "Scroll of "

    def __repr__(self):
        return "Name: " + self.forename + self.name + " -  Price: " + str(self.price) + " gp"


class Material:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])


class Enchantment:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])

    def __repr__(self):
        return "Name: " + self.name + " -  Price: " + str(self.base_price) + " gp, + magic level:" + self.magic_level


class Modification:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])


class Subtype:
    def __init__(self, dictionary):
        for key in dictionary:
            setattr(self, key, dictionary[key])


def add_material(item):
    """choose material"""
    if randint(1, 100) > 80:
        wdict = {'Light Melee': 'lweapon_price', 'One-Handed Melee': 'oweapon_price', 'Two-Handed Melee':
            'tweapon_price', 'Ranged': 'tweapon_price', 'One-Handed Firearms': 'oweapon_price',
                 'Two-Handed Firearms': 'tweapon_price', 'Siege': 'tweapon_price', 'Explosives': 'oweapon_price',
                 'Unarmed': 'lweapon_price'}
        adict = {'Light Armor': 'larmor_price', 'Medium Armor': 'marmor_price', 'Heavy Armor': 'harmor_price',
                 'Shield': 'shield_price'}

        filtered_matlist = []
        if item.type in ("Light Melee", "One-Handed Melee", "Two-Handed Melee", "Ranged", "One-Handed Firearms",
                         "Two-Handed Firearms", "Siege", "Explosives", "Unarmed"):
            for x in materialslist:
                if hasattr(x, wdict[item.type]):
                    filtered_matlist.append(x)
        elif item.type in ("Light Armor", "Medium Armor", "Heavy Armor", "Shield"):
            for x in materialslist:
                if hasattr(x, adict[item.type]):
                    filtered_matlist.append(x)
        elif item.category == 'Nonmagical Ammunition':
            for x in materialslist:
                if hasattr(x, 'ammu_price'):
                    filtered_matlist.append(x)

        if hasattr(item, 'is_metal'):
            for x in filtered_matlist:
                if not hasattr(x, 'metal'):
                    filtered_matlist.remove(x)
        elif hasattr(item, 'is_wood'):
            for x in filtered_matlist:
                if not hasattr(x, 'wood'):
                    filtered_matlist.remove(x)
        elif hasattr(item, 'is_stone'):
            for x in filtered_matlist:
                if not hasattr(x, 'stone'):
                    filtered_matlist.remove(x)
        elif hasattr(item, 'is_leather'):
            for x in filtered_matlist:
                if not hasattr(x, 'leather-cloth'):
                    filtered_matlist.remove(x)

        """creates rarity list based on json"""
        material_rarity = []
        for x in filtered_matlist:
            material_rarity.append(int(x.rarity))

        """rolls material for item"""
        tempmaterial = choices(filtered_matlist, material_rarity, k=1)[0]
        chosenmaterial = deepcopy(tempmaterial)

        """assigns name of material as field in item class for rolled item"""
        item.material = chosenmaterial.name + " "
        if hasattr(chosenmaterial, 'is_Mwk'):
            item.is_Mwk = True

        item.mat = chosenmaterial

        """updates price for chosen item  based on material"""
        if item.type in ("Light Melee", "One-Handed Melee", "Two-Handed Melee", "Ranged", "One-Handed Firearms",
                         "Two-Handed Firearms", "Siege", "Explosives", "Unarmed"):
            if chosenmaterial.lweapon_price == 'special':
                '''Cold Iron Weapons'''
                if chosenmaterial.name == 'Cold Iron':
                    if item.is_Mwk is True:
                        item.price = ((float(item.price) - 300) * 2) + 300
                    else:
                        item.price = float(item.price) * 2
                    item.enchant_cost = 2000
                    '''Darkwood Weapons'''
                elif chosenmaterial.name == 'Darkwood':
                    item.price = float(item.price) + (10 * float(item.weight.replace(' lbs.', '').replace(' lb.',
                                                                                                          ''))) + 300
                    item.weight = str(float(item.weight.replace(' lbs.', '').replace(' lb.', '')) / 2) + " lbs."
                    '''Paueliel Weapons'''
                elif chosenmaterial.name == 'Paueliel':
                    item.price = (float(item.price) + (10 * float(item.weight.replace(' lbs.', '').replace(' lb.', '')))
                                  + 300) * 2.5
                    item.weight = str(float(item.weight.replace(' lbs.', '').replace(' lb.', '')) / 2) + " lbs."
                    '''Sunsilver Weapons'''
                elif chosenmaterial.name == 'Sunsilver':
                    item.price = float(item.price) + (
                            25 * float(item.weight.replace(' lbs.', '').replace(' lb.', ''))) + 300
                    '''Greenwood Weapons'''
                elif chosenmaterial.name == 'Greenwood':
                    item.price = float(item.price) + (
                            50 * float(item.weight.replace(' lbs.', '').replace(' lb.', ''))) + 300
                    '''Blackwood Weapons'''
                elif chosenmaterial.name == 'Blackwood':
                    item.price = float(item.price) + (
                            20 * float(item.weight.replace(' lbs.', '').replace(' lb.', ''))) + 300
                    '''Nexavaran Steel Weapons'''
                elif chosenmaterial.name == 'Nexavaran Steel':
                    if item.is_Mwk is True:
                        item.price = ((float(item.price) - 300) * 1.5) + 300
                    else:
                        item.price = float(item.price) * 1.5
                    item.enchant_cost = 3000
                    '''Pyre Steel Weapons'''
                elif chosenmaterial.name == 'Pyre Steel':
                    if item.is_Mwk is True:
                        item.price = ((float(item.price) - 300) * 2) + 300
                    else:
                        item.price = float(item.price) * 2

            elif item.type == "Unarmed":
                item.price = float(item.price) + float(chosenmaterial.lweapon_price)
            elif item.type == "Light Melee":
                item.price = float(item.price) + float(chosenmaterial.lweapon_price)
            elif item.type == "One-Handed Melee":
                item.price = float(item.price) + float(chosenmaterial.oweapon_price)
            elif item.type == "Two-Handed Melee":
                item.price = float(item.price) + float(chosenmaterial.tweapon_price)
            elif item.type == "Ranged":
                item.price = float(item.price) + float(chosenmaterial.tweapon_price)
            elif item.type == "One-Handed Firearms":
                item.price = float(item.price) + float(chosenmaterial.oweapon_price)
            elif item.type == "Two-Handed Firearms":
                item.price = float(item.price) + float(chosenmaterial.tweapon_price)

        elif item.type in ("Light Armor", "Medium Armor", "Heavy Armor", "Shield"):
            if chosenmaterial.larmor_price == 'special':
                '''Darkwood Armor'''
                if chosenmaterial.name == 'Darkwood':
                    item.price = float(item.price) + (10 * float(item.weight.replace(' lbs.', '').replace(' lb.', ''))) \
                                 + 150
                    item.weight = str(float(item.weight.replace(' lbs.', '').replace(' lb.', '')) / 2) + " lbs."
                    ''' Dragonhide Armor'''
                elif chosenmaterial.name == 'Dragonhide':
                    if item.is_Mwk is True:
                        item.price = float(item.price) * 2
                    else:
                        item.price = (float(item.price) + 150) * 2
                        '''Paueliel Armor'''
                elif chosenmaterial.name == 'Paueliel':
                    item.price = (float(item.price) + (10 * float(item.weight.replace(' lbs.', '').replace(' lb.', '')))
                                  + 150) * 2.5
                    '''Sunsilver Armor'''
                elif chosenmaterial.name == 'Sunsilver':
                    item.price = float(item.price) + (
                            25 * float(item.weight.replace(' lbs.', '').replace(' lb.', ''))) + 150
                    '''Greenwood Armor'''
                elif chosenmaterial.name == 'Greenwood':
                    item.price = float(item.price) + (
                            50 * float(item.weight.replace(' lbs.', '').replace(' lb.', ''))) + 150
                    '''Griffon Mane Armor'''
                elif chosenmaterial.name == 'Griffon Mane':
                    if item.type == 'Light Armor':
                        item.price = float(item.price) + 200
                    else:
                        add_material(item)
                    '''Blackwood Armor'''
                elif chosenmaterial.name == 'Blackwood':
                    item.price = float(item.price) + (
                            20 * float(item.weight.replace(' lbs.', '').replace(' lb.', ''))) + 150

            elif item.type == "Light Armor":
                item.price = float(item.price) + float(chosenmaterial.larmor_price)
            elif item.type == "Medium Armor":
                item.price = float(item.price) + float(chosenmaterial.marmor_price)
            elif item.type == "Heavy Armor":
                item.price = float(item.price) + float(chosenmaterial.harmor_price)
            elif item.type == "Shield":
                item.price = float(item.price) + float(chosenmaterial.shield_price)

        elif item.category == 'Nonmagical Ammunition':
            if chosenmaterial.ammu_price == 'special':
                if chosenmaterial.name == 'Cold Iron':
                    if item.is_Mwk is True:
                        item.price = (float(item.price) - (300 * item.quantity / 50) * 2) + (300 * item.quantity / 50)
                    else:
                        item.price = float(item.price) * 2
                    item.enchant_cost = 2000
                elif chosenmaterial.name == 'Darkwood':
                    item.price = float(item.price) + (10 * float(item.weight.replace(' lbs.', '').replace(' lb.', ''))) \
                                 + (300 * item.quantity / 50)
                    item.weight = str(float(item.weight.replace(' lbs.', '').replace(' lb.', '')) / 2) + " lbs."
                elif chosenmaterial.name == 'Paueliel':
                    item.price = (float(item.price) + (10 * float(item.weight.replace(' lbs.', '').replace(' lb.', '')))
                                  + (300 * item.quantity / 50)) * 2.5
                    item.weight = str(float(item.weight.replace(' lbs.', '').replace(' lb.', '')) / 2) + " lbs."
                elif chosenmaterial.name == 'Sunsilver':
                    item.price = float(item.price) + (25 * float(item.weight.replace(
                        ' lbs.', '').replace(' lb.', ''))) + (300 * item.quantity / 50)
                elif chosenmaterial.name == 'Blackwood':
                    item.price = float(item.price) + (20 * float(item.weight.replace(
                        ' lbs.', '').replace(' lb.', ''))) + (300 * item.quantity / 50)
                elif chosenmaterial.name == 'Nexavaran Steel':
                    if item.is_Mwk is True:
                        item.price = ((float(item.price) - (300 * item.quantity / 50)) * 1.5) + (300 * item.quantity /
                                                                                                 50)
                    else:
                        item.price = float(item.price) * 1.5
                    item.enchant_cost = 3000
                elif chosenmaterial.name == 'Pyre Steel':
                    if item.is_Mwk is True:
                        item.price = ((float(item.price) - (300 * item.quantity / 50)) * 2) + (300 * item.quantity / 50)
                    else:
                        item.price = float(item.price) * 2

            else:
                item.price = float(item.price) + (float(chosenmaterial.ammu_price) * float(item.quantity))


def magicalitem(item):
    global templist
    """roll masterwork/magic level"""
    if randint(1, 100) > 60:
        if item.is_Mwk is True:
            '''check item isn't already mwk by default'''
            return
        else:
            if item.category == "Nonmagical Weapons":
                item.price = float(item.price) + 300.0
            elif item.category == "Nonmagical Armor":
                item.price = float(item.price) + 150.0
            elif item.category == "Nonmagical Ammunition":
                item.price = float(item.price) + (300 * item.quantity / 50)

        if hasattr(item, 'setting'):
            if item.setting == 'Modern Firearms' or item.setting == 'Worldscape':
                return

        magiclevel = choices([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 30, 25, 20, 15, 10, 5, 4, 3, 2, 1], k=1)[0]

        mweapon_prices = {1: 2000, 2: 8000, 3: 18000, 4: 32000, 5: 50000, 6: 72000, 7: 98000, 8: 128000, 9: 162000,
                          10: 200000}
        marmor_prices = {1: 1000, 2: 4000, 3: 9000, 4: 16000, 5: 25000, 6: 36000, 7: 49000, 8: 64000, 9: 81000,
                         10: 100000}

        templist = []
        with open('Resources/enchantments.json') as j:
            data = json.load(j)
            if item.type == 'Light Melee' or item.type == 'One-Handed Melee' or item.type == 'Two-Handed Melee' \
                    or item.type == 'Unarmed':
                templist = [Enchantment(i) for i in data["melee weapon enchantments"]]
                if config.getboolean('flags', 'set_mth'):
                    templist = templist + [Enchantment(i) for i in data["mythic weapon enchantments"]]

                if item.type == 'Light Melee':
                    for x in templist:
                        if not hasattr(x, 'light_weapon'):
                            templist.remove(x)

                if item.type == 'Two-handed Melee':
                    for x in templist:
                        if hasattr(x, 'onehand'):
                            templist.remove(x)

                if not hasattr(item, 'blunt'):
                    """remove brawling, disruption, smashing, legbreaker, obliviating, quaking"""
                    for x in templist:
                        if hasattr(x, 'blunt') and not hasattr(x, 'slashing') and not hasattr(x, 'piercing'):
                            templist.remove(x)

                if not hasattr(item, 'slashing') and not hasattr(item, 'piercing'):
                    """remove keen, bloodsong, vampiric, culling"""
                    for x in templist:
                        if hasattr(x, 'slashing') and hasattr(x, 'piercing') and not hasattr(x, 'blunt'):
                            templist.remove(x)

                if not hasattr(item, 'blunt') and not hasattr(item, 'slashing'):
                    """remove underwater"""
                    for x in templist:
                        if hasattr(x, 'slashing') and hasattr(x, 'blunt') and not hasattr(x, 'piercing'):
                            templist.remove(x)

                if not hasattr(item, 'slashing'):
                    """remove vorpal, injecting, prehensile"""
                    for x in templist:
                        if hasattr(x, 'slashing') and not hasattr(x, 'piercing') and not hasattr(x, 'blunt'):
                            templist.remove(x)

                if not hasattr(item, 'piercing'):
                    """remove flamboyant, ow, sticky"""
                    for x in templist:
                        if hasattr(x, 'piercing') and not hasattr(item, 'slashing') and not hasattr(item, 'blunt'):
                            templist.remove(x)

                if not hasattr(item, 'finessable'):
                    for x in templist:
                        if hasattr(x, 'finesse'):
                            templist.remove(x)

                if not hasattr(item, 'reach'):
                    for x in templist:
                        if hasattr(x,'req_feature'):
                            templist.remove(x)

                if not hasattr(item, 'nonlethal'):
                    for x in templist:
                        if hasattr(x, 'nonlethal'):
                            templist.remove(x)

                for x in templist:
                    '''remove catalytic from base list'''
                    if hasattr(x, 'req_enchant'):
                        templist.remove(x)

                for x in templist:
                    '''remove brawling/inspired/prehensile'''
                    if hasattr(x, 'weaponlist'):
                        if item.name.lower() not in x.weaponlist:
                            if not hasattr(x, 'req_type'):
                                templist.remove(x)
                            elif hasattr(x, 'req_type') and not item.proficiency == 'Simple':
                                templist.remove(x)


            elif item.type == 'Ranged':
                if item.ranged_type == 'bow' or item.ranged_type == 'crossbow':
                    templist = [Enchantment(i) for i in data["ranged weapon enchantments"]]
                    if config.getboolean('flags', 'set_mth'):
                        templist = templist + [Enchantment(i) for i in data["mythic weapon enchantments"]]
                    for x in templist:
                        if hasattr(x, 'bow'):
                            templist2 = [x]
                        if not hasattr(x, 'crossbow'):
                            templist.remove(x)
                        '''composite check'''
                    if item.name.find('+') != -1:
                        templist = templist + templist2

                elif item.ranged_type == 'thrown':
                    templist = [Enchantment(i) for i in data["ranged weapon enchantments"]]
                    if config.getboolean('flags', 'set_mth'):
                        templist = templist + [Enchantment(i) for i in data["mythic weapon enchantments"]]
                    for x in templist:
                        if not hasattr(x, 'thrown'):
                            templist.remove(x)

                elif item.ranged_type == 'other':
                    templist = [Enchantment(i) for i in data["ranged weapon enchantments"]]
                    if config.getboolean('flags', 'set_mth'):
                        templist = templist + [Enchantment(i) for i in data["mythic weapon enchantments"]]
                    for x in templist:
                        if not hasattr(x, 'other'):
                            templist.remove(x)

                for x in templist:
                    '''remove catalytic from base list'''
                    if hasattr(x, 'req_enchant'):
                        templist.remove(x)
                    if hasattr(x, 'weaponlist'):
                        if item.name.lower() not in x.weaponlist:
                            if not hasattr(x, 'req_type'):
                                templist.remove(x)
                            elif hasattr(x, 'req_type') and not item.proficiency == 'Simple':
                                templist.remove(x)

                if not hasattr(item, 'piercing'):
                    for x in templist:
                        if hasattr(x, 'piercing'):
                            templist.remove(x)

            elif item.type == 'One-Handed Firearms' or item.type == 'Two-Handed Firearms':
                if item.ranged_type == 'firearms':
                    templist = [Enchantment(i) for i in data["ranged weapon enchantments"]]
                    if config.getboolean('flags', 'set_mth'):
                        templist = templist + [Enchantment(i) for i in data["mythic weapon enchantments"]]
                    for x in templist:
                        if not hasattr(x, 'firearms'):
                            templist.remove(x)

                for x in templist:
                    '''remove catalytic from base list'''
                    if hasattr(x, 'req_enchant'):
                        templist.remove(x)

                if not hasattr(item, 'piercing'):
                    for x in templist:
                        if hasattr(x, 'piercing'):
                            templist.remove(x)

            elif item.type == 'ammo':
                templist = [Enchantment(i) for i in data["ranged weapon enchantments"]]
                if config.getboolean('flags', 'set_mth'):
                    templist = templist + [Enchantment(i) for i in data["mythic weapon enchantments"]]
                for x in templist:
                    if not hasattr(x, 'ammunition'):
                        templist.remove(x)

                for x in templist:
                    '''remove catalytic from base list'''
                    if hasattr(x, 'req_enchant'):
                        templist.remove(x)

                if 'cartridge' not in item.name.lower():
                    for x in templist:
                        if hasattr(x, 'is_cartridge'):
                            templist.remove(x)

            elif item.slot == 'Armor':
                templist = [Enchantment(i) for i in data["armor enchantments"]]
                if config.getboolean('flags', 'set_mth'):
                    templist = templist + [Enchantment(i) for i in data["mythic armor enchantments"]]

                if not hasattr(item, 'is_leather'):
                    for x in templist:
                        if hasattr(x, 'is_leather'):
                            templist.remove(x)

                if not hasattr(item, 'is_padded'):
                    for x in templist:
                        if hasattr(x, 'is_padded'):
                            templist.remove(x)

                if item.name not in 'Full Plate, Hellknight Half-Plate, Hellknight Leather, Hellknight Plate, ' \
                                    'Dragonhide Plate, Gray Maiden Plate, Dwarven Plate':
                    for x in templist:
                        if hasattr(x, 'is_fullplate'):
                            templist.remove(x)

            elif item.slot == 'Shield':
                templist = [Enchantment(i) for i in data["shield enchantments"]]
                if config.getboolean('flags', 'set_mth'):
                    templist = templist + [Enchantment(i) for i in data["mythic shield enchantments"]]
                for e in templist:
                    if not hasattr(e, item.shield_type):
                        templist.remove(e)

                for x in templist:
                    '''remove spellrending from base list'''
                    if hasattr(x, 'req_enchant'):
                        templist.remove(x)


        if magiclevel == 0:
            item.name = "Masterwork " + item.name
        elif magiclevel == 1:
            item.magic = "+1 "
            item.price = item.price + 2000
            item.price = item.price + item.enchant_cost
            item.magical = True
        else:
            item.l_itemEnch = []
            magicbudget = magiclevel - 1
            originallevel = magiclevel
            item.magicbudget = magicbudget
            while magicbudget > 4:
                assignenchant(item)
                magicbudget = item.magicbudget

            roll = randint(1, 10)
            while magicbudget > 0 and roll > 3:
                assignenchant(item)
                magicbudget = item.magicbudget
                roll = randint(1, 5)

            magiclevel = originallevel - (originallevel - magicbudget - 1)
            item.magic = "+" + str(magiclevel) + " "
            if item.type in ("Light Melee", "One-Handed Melee", "Two-Handed Melee", "Ranged", "One-Handed Firearms",
                             "Two-Handed Firearms", "Siege", "Explosives", "Unarmed"):
                item.price = item.price + mweapon_prices[originallevel]
            elif item.type in ("Light Armor", "Medium Armor", "Heavy Armor", "Shield"):
                item.price = item.price + marmor_prices[originallevel]
            elif item.type in ("ammo"):
                item.price = item.price + (mweapon_prices[originallevel] / 50 * item.quantity)
            item.price = item.price + item.enchant_cost
            item.magical = True
            templist = deepcopy(enchantmentlist)


def assignenchant(i):
    """chooses an enchant from templist to put on the item, and then removes the enchant from templist
    so that 1 item cannot get the same enchant multiple times."""
    efrequency = []

    for x in i.l_itemEnch:
        if x.name == 'Corrosive' or x.name == 'Corrosive Burst':
            with open('Resources/enchantments.json') as j:
                data = json.load(j)
            if i.type in 'Light Melee, One-Handed Melee, Two-Handed Melee, Unarmed':
                templist.append(Enchantment(data["melee weapon enchantments"][99]))
            elif i.type in 'Ranged, One-Handed Firearms, Two-Handed Firearms':
                templist.append(Enchantment(data["ranged weapon enchantments"][64]))

        if x.name == 'Catalytic':
            for e in templist:
                if e.name == 'Catalytic':
                    templist.remove(e)

    for x in i.l_itemEnch:
        if 'Spell resistance' in x.name:
            with open('Resources/enchantments.json') as j:
                data = json.load(j)
            if i.type == 'Shield':
                templist.append(Enchantment(data["shield enchantments"][38]))

        if x.name == 'Spellrending':
            for e in templist:
                if e.name == 'Spellrending':
                    templist.remove(e)

    for x in templist:
        efrequency.append(int(x.frequency))
    chosenenchant = choices(templist, efrequency, k=1)[0]

    if int(chosenenchant.magic_level) <= i.magicbudget:
        with open('Resources/subtypes.json') as j:
            data = json.load(j)
        '''humanoid bane/misery'''
        if chosenenchant.name in 'Humanoid Bane, Humanoid Misery, Humanoid Withstanding':
            hsubtypes = [Subtype(i) for i in data['Humanoid']]
            sfrequency = []
            for x in hsubtypes:
                sfrequency.append(int(x.frequency))

            hBane = choices(hsubtypes, sfrequency, k=1)[0]
            chosenenchant.name = chosenenchant.name + ' (' + hBane.name + ')'

            '''outsider bane/misery'''
        elif chosenenchant.name in 'Outsider Bane, Outsider Misery, Outsider Withstanding':
            osubtypes = [Subtype(i) for i in data['Outsider']]
            sfrequency = []
            for x in osubtypes:
                sfrequency.append(int(x.frequency))

            oBane = choices(osubtypes, sfrequency, k=1)[0]
            chosenenchant.name = chosenenchant.name + ' (' + oBane.name + ')'

        elif chosenenchant.name == 'Deceiving':
            asubtypes = [Subtype(i) for i in data['Alignments']]
            sfrequency = []
            for x in asubtypes:
                sfrequency.append(int(x.frequency))

            dAlignment = choices(asubtypes, sfrequency, k=1)[0]
            chosenenchant.name = chosenenchant.name + ' (' + dAlignment.name + ')'

        elif chosenenchant.name == 'Blood-Hunting':
            bsubtypes = [Subtype(i) for i in data['Bloodlines']]
            sfrequency = []
            for x in bsubtypes:
                sfrequency.append(int(x.frequency))

            bLine = choices(bsubtypes, sfrequency, k=1)[0]
            chosenenchant.name = chosenenchant.name + ' (' + bLine.name + ')'

        elif chosenenchant.name == 'Spirit-Hunting':
            ssubtypes = [Subtype(i) for i in data['Mysteries']]
            sfrequency = []
            for x in ssubtypes:
                sfrequency.append(int(x.frequency))

            sMystery = choices(ssubtypes, sfrequency, k=1)[0]
            chosenenchant.name = chosenenchant.name + ' (' + sMystery.name + ')'

        elif chosenenchant.name == 'Runeforged':
            rsubtypes = [Subtype(i) for i in data['Runeforged']]
            sfrequency = []
            for x in rsubtypes:
                sfrequency.append(int(x.frequency))

            rSin = choices(rsubtypes, sfrequency, k=1)[0]
            chosenenchant.name = chosenenchant.name + ' (' + rSin.name + ')'

        elif chosenenchant.name == 'Training':
            tsubtypes = [Subtype(i) for i in data['Training Feats']]
            sfrequency = []
            for x in tsubtypes:
                if hasattr(x, 'req_type'):
                    if hasattr(i, 'proficiency'):
                        if i.proficiency != 'Exotic':
                            x.frequency = 0
                if hasattr(x, 'excl_ench'):
                    for y in i.l_itemEnch:
                        if y.name in 'Keen':
                            x.frequency = 0
            for x in tsubtypes:
                sfrequency.append(int(x.frequency))

            tFeat = choices(tsubtypes, sfrequency, k=1)[0]
            chosenenchant.name = chosenenchant.name + ' (' + tFeat.name + ')'

        elif chosenenchant.name in 'Patriotic, Treasonous':
            psubtypes = [Subtype(i) for i in data['Nationalities']]
            sfrequency = []
            for x in psubtypes:
                sfrequency.append(int(x.frequency))

            pNation = choices(psubtypes, sfrequency, k=1)[0]
            chosenenchant.name = chosenenchant.name + ' (' + pNation.name + ')'

        i.l_itemEnch.append(chosenenchant)
        i.magicbudget = i.magicbudget - int(chosenenchant.magic_level)

        if hasattr(chosenenchant, 'shared'):
            for x in templist:
                if hasattr(x, 'shared'):
                    if chosenenchant.shared == x.shared:
                        templist.remove(x)
        else:
            templist.remove(chosenenchant)
        if chosenenchant.name == 'Adaptive':
            complvllist = [' [+0]', ' [+1]', ' [+2]', ' [+3]', ' [+4]', ' [+5]']
            for x in complvllist:
                i.name = i.name.replace(x, '')
        try:
            if i.type == 'ammo':
                i.price = float(i.price) + (float(chosenenchant.base_price) / 50 * i.quantity)
            else:
                i.price = float(i.price) + float(chosenenchant.base_price)
        except:
            i.price = i.price
    else:
        assignenchant(i)


def assignmod(i):
    list_mods = []
    with open('Resources/modifications.json') as j:
        data = json.load(j)

    if i.category == 'Nonmagical Weapons':
        for m in data['weapon modifications']:
            list_mods.append(Modification(m))
        for m in list_mods:
            if i.type not in ('Light Melee', 'One-Handed Melee', 'Two-Handed Melee', 'Ranged', 'Unarmed',
                              'One-Handed Firearms', 'Two-Handed Firearms'):
                if hasattr(m, 'type1'):
                    list_mods.remove(m)
            if not hasattr(i, 'blunt'):
                if m.damage_type == 'B':
                    list_mods.remove(m)

            if not hasattr(i, 'piercing') and not hasattr(i, 'slashing'):
                if m.damage_type == 'P, S':
                    list_mods.remove(m)

    elif i.category == 'Nonmagical Ammunition':
        for m in data['weapon modifications']:
            list_mods.append(Modification(m))
        for x in list_mods:
            if not hasattr(x, 'type2'):
                list_mods.remove(x)

    elif i.category == 'Nonmagical Armor':
        for m in data['armor modifications']:
            list_mods.append(Modification(m))
        for m in list_mods:
            if not hasattr(i, 'is_metal'):
                if hasattr(m, 'type'):
                    list_mods.remove(m)

    chosenMod = choice(list_mods)
    i.mod = chosenMod
    i.modded = True
    i.weight = str(float(i.weight.replace("s", "").replace(" lb.", "")) + int(chosenMod.weight)) + " lbs."
    if hasattr(i, 'magical'):
        i.price = float(i.price) + (float(chosenMod.price) * 1.5)
    else:
        i.price = float(i.price) + float(chosenMod.price)


def calculate_budget(enCR, cSpeed, tType):
    global lootBudget
    global cashBudget
    global encounterCR
    global campaignSpeed
    global treasureType
    global eCR

    '''if eCR is 1 or higher, convert to integer for table accuracy below'''
    if enCR == '1/8' or enCR == '1/6' or enCR == '1/4' or enCR == '1/3' or enCR == '1/2':
        eCR = enCR
    else:
        eCR = int(enCR)

    '''tables for deciding loot budget based on eCR and cSpeed given'''
    slowCR = {'1/8': 20, '1/6': 30, '1/4': 40, '1/3': 55, '1/2': 85, 1: 170, 2: 350, 3: 550, 4: 750, 5: 1000, 6: 1350,
              7: 1750, 8: 2200, 9: 2850, 10: 3650, 11: 4650, 12: 6000, 13: 7750, 14: 10000, 15: 13000, 16: 16500,
              17: 22000, 18: 28000, 19: 35000, 20: 44000, 21: 55000, 22: 69000, 23: 85000, 24: 102000, 25: 125000,
              26: 150000, 27: 175000, 28: 205000, 29: 240000, 30: 280000}
    mediumCR = {'1/8': 35, '1/6': 45, '1/4': 65, '1/3': 85, '1/2': 130, 1: 260, 2: 550, 3: 800, 4: 1150, 5: 1550,
                6: 2000, 7: 2600, 8: 3350, 9: 4250, 10: 5450, 11: 7000, 12: 9000, 13: 11600, 14: 15000, 15: 19500,
                16: 25000, 17: 32000, 18: 41000, 19: 53000, 20: 67000, 21: 84000, 22: 104000, 23: 127000, 24: 155000,
                25: 185000, 26: 220000, 27: 260000, 28: 305000, 29: 360000, 30: 420000}
    fastCR = {'1/8': 50, '1/6': 65, '1/4': 100, '1/3': 135, '1/2': 200, 1: 400, 2: 800, 3: 1200, 4: 1700, 5: 2300,
              6: 3000, 7: 3900, 8: 5000, 9: 6400, 10: 8200, 11: 10500, 12: 13500, 13: 17500, 14: 22000, 15: 29000,
              16: 38000, 17: 48000, 18: 62000, 19: 79000, 20: 100000, 21: 125000, 22: 155000, 23: 190000, 24: 230000,
              25: 275000, 26: 330000, 27: 390000, 28: 460000, 29: 540000, 30: 630000}

    if cSpeed == "slow":
        lootBudget = slowCR[eCR]
    elif cSpeed == "medium":
        lootBudget = mediumCR[eCR]
    elif cSpeed == "fast":
        lootBudget = fastCR[eCR]

    if type(eCR) == str:
        eCR = float(Fraction(eCR))

    type_mod = {'incidental': 0.5, 'standard': 1.0, 'double': 2.0, 'triple': 3.0}
    lootBudget = float(lootBudget) * type_mod[tType]
    cashBudget = float(lootBudget) / 100 * randint(5, max(5, 30))


def load_items():
    global lootlist, potionlist, wandlist, scrolllist, lfrequency, pfrequency, wfrequency, sfrequency

    lootlist = []
    potionlist = []
    wandlist = []
    scrolllist = []
    lfrequency = []
    pfrequency = []
    wfrequency = []
    sfrequency = []

    config.read('config.ini')

    if config.getboolean('flags', 'loot_nmi'):
        lootlist.extend(list_nmi)
    if config.getboolean('flags', 'loot_nma'):
        lootlist.extend(list_nma)
    if config.getboolean('flags', 'loot_nmw'):
        lootlist.extend(list_nmw)
    if config.getboolean('flags', 'loot_nmu'):
        lootlist.extend(list_nmu)
    if config.getboolean('flags', 'loot_ma'):
        lootlist.extend(list_ma)
    if config.getboolean('flags', 'loot_mw'):
        lootlist.extend(list_mw)
    if config.getboolean('flags', 'loot_mu'):
        lootlist.extend(list_mu)
    if config.getboolean('flags', 'loot_st'):
        lootlist.extend(list_st)
    if config.getboolean('flags', 'loot_ro'):
        lootlist.extend(list_ro)
    if config.getboolean('flags', 'loot_ri'):
        lootlist.extend(list_ri)
    if config.getboolean('flags', 'loot_wie'):
        lootlist.extend(list_wie)
    if config.getboolean('flags', 'loot_wis'):
        lootlist.extend(list_wis)
    if config.getboolean('flags', 'loot_cur'):
        lootlist.extend(list_cur)
    if config.getboolean('flags', 'loot_art'):
        lootlist.extend(list_art)

    ''' running the same remove loop 3 times because it appears to not catch everything each time'''
    n = 0
    while n < 3:
        for x in lootlist:
            if hasattr(x, 'setting'):
                if not config.getboolean('flags', 'set_brz'):
                    if x.setting == 'Bronze Age':
                        lootlist.remove(x)
                if not config.getboolean('flags', 'set_stn'):
                    if x.setting == 'Stone Age':
                        lootlist.remove(x)
                if not config.getboolean('flags', 'set_eas'):
                    if x.setting == 'Eastern':
                        lootlist.remove(x)
                if not config.getboolean('flags', 'set_mth'):
                    if x.setting == 'Mythic':
                        lootlist.remove(x)
                if not config.getboolean('flags', 'set_efire'):
                    if x.setting == 'Early Firearms':
                        lootlist.remove(x)
                if not config.getboolean('flags', 'set_afire'):
                    if x.setting == 'Advanced Firearms':
                        lootlist.remove(x)
                if not config.getboolean('flags', 'set_mfire'):
                    if x.setting == 'Modern Firearms':
                        lootlist.remove(x)
                if not config.getboolean('flags', 'set_wdsp'):
                    if x.setting == 'Worldscape':
                        lootlist.remove(x)
        n += 1

    for x in lootlist:
        lfrequency.append(int(x.frequency))

    if config.getboolean('flags', 'loot_pot'):
        potionlist.extend(list_pot)
    for x in potionlist:
        pfrequency.append(int(x.frequency))
    if config.getboolean('flags', 'loot_wnd'):
        wandlist.extend(list_wnd)
    for x in wandlist:
        wfrequency.append(int(x.frequency))
    if config.getboolean('flags', 'loot_scr'):
        scrolllist.extend(list_scr)
    for x in scrolllist:
        sfrequency.append(int(x.frequency))

    for x in templist:
        if x.type == 'melee':
            list_wench.append(x)
        if x.type == 'ranged':
            list_rench.append(x)
        if x.type == 'armor':
            list_aench.append(x)
        if x.type == 'shield':
            list_sench.append(x)

    print("")
    print("")
    print("Picking from a list of", len(lootlist) + len(potionlist) + len(wandlist) + len(scrolllist), "items.")


def random_item():
    global lootBudget
    global cashBudget
    global errorCount

    '''first rolls to see which list to choose from'''
    roll = randint(1, 100)
    if roll > 90 and config.getboolean('flags', 'loot_pot'):
        chosen_item = choices(potionlist, pfrequency, k=1)[0]
        chosen_item = deepcopy(chosen_item)
        chosen_item.category = 'Potions'
    elif 91 > roll > 86 and config.getboolean('flags', 'loot_wnd'):
        chosen_item = choices(wandlist, wfrequency, k=1)[0]
        '''roll number of charges on wand (max 50, original price based on 50)'''
        charges = randint(10, 50)
        chosen_item = deepcopy(chosen_item)
        chosen_item.name = chosen_item.name + " (" + str(charges) + " charges)"
        chosen_item.price = int(chosen_item.price / 50 * charges)
        chosen_item.category = 'Wands'
    elif 87 > roll > 83 and config.getboolean('flags', 'loot_scr'):
        chosen_item = choices(scrolllist, sfrequency, k=1)[0]
        chosen_item = deepcopy(chosen_item)
        chosen_item.category = 'Scrolls'
    else:
        chosen_item = choices(lootlist, lfrequency, k=1)[0]
        chosen_item = deepcopy(chosen_item)
    errorCount = errorCount + 1
    if errorCount > 1000:
        return encounterLoot

    if chosen_item.category == 'Nonmagical Weapons' or chosen_item.category == 'Nonmagical Armor' or \
            chosen_item.category == 'Nonmagical Ammunition':
        if "+" in chosen_item.name:
            chosen_item.composite()
        if "*" in chosen_item.name:
            chosen_item.ammoquantity()
        if config.getboolean('flags', 'flg_mats'):
            if not hasattr(chosen_item, 'has_material'):
                add_material(chosen_item)
        if config.getboolean('flags', 'flg_ench'):
            magicalitem(chosen_item)

    if config.getboolean('flags', 'flg_mods'):
        if chosen_item.category == 'Nonmagical Weapons' or chosen_item.category == 'Nonmagical Armor' or \
                chosen_item.category == 'Nonmagical Ammunition':
            if randint(1, 100) > 94:
                assignmod(chosen_item)
    if chosen_item.name == 'Slaying Arrow ^' or chosen_item.name == 'Greater Slaying Arrow ^':
        chosen_item.slayingtype()
    '''checks if item would break budget, and then assigns to encounterLoot. 
    If item would break budget program runs again.'''
    if lootBudget - float(chosen_item.price) > 0:
        lootBudget = lootBudget - float(chosen_item.price)
        chosen_item.fmod = modFormat(chosen_item)
        chosen_item.fench = enchFormat(chosen_item)

        chosen_item.check = str("{}{}{}{}{}".format(chosen_item.fench, chosen_item.fmod, chosen_item.material,
                                                  chosen_item.forename, chosen_item.name))
        for x in encounterLootList:
            if hasattr(x, 'aquantity'):
                if chosen_item.category == 'Nonmagical Ammunition':
                    if x.check.split('- (')[0] == chosen_item.check.split('- (')[0]:
                        aq = x.name.split('- (')[1].split(')')[0]
                        x.name = x.name.replace(aq, str(x.aquantity + chosen_item.aquantity))
                        x.aquantity = int(aq) + chosen_item.aquantity
                        x.price = x.price + chosen_item.price
                        return encounterLoot

            elif chosen_item.check == x.check:
                x.quantity += 1
                return encounterLoot

        chosen_item.quantity = 1
        encounterLootList.append(chosen_item)
        errorCount = 0
    else:
        random_item()

    return encounterLoot


def create_loot_list(enCR, cSpeed, tType):
    global lootBudget
    global cashBudget
    global encounterLootList
    global encounterLoot

    encounterLootList = []
    load_items()
    calculate_budget(enCR, cSpeed, tType)

    print("Initial Budget:", int(lootBudget))
    print("Cash Breakpoint:", int(cashBudget))

    while lootBudget > cashBudget and len(encounterLootList) < config.getint('flags', 'max_items'):
        random_item()

    splitBudget()
    return encounterLootList


def checkBudget(x):
    if x == 'p':
        return platBudget
    elif x == 'g':
        return goldBudget
    elif x == 's':
        return silvBudget
    elif x == 'c':
        return coppBudget


def splitBudget():
    global lootBudget
    global platBudget
    global goldBudget
    global silvBudget
    global coppBudget
    global eCR

    if eCR < 1:
        eCR = 1
    if lootBudget > 300:
        platBudget = int(lootBudget * float(3 * eCR) / 1000)
        goldBudget = lootBudget - (10 * platBudget)
    else:
        platBudget = 0
        goldBudget = lootBudget

    coppRoll = randint(1, 10 * eCR)
    silvRoll = randint(1, 10 * eCR)

    coppBudget = int(floor(10 * (10 * goldBudget % 1)) + coppRoll)
    silvBudget = int(floor(10 * (goldBudget % 1)) + silvRoll)
    goldBudget = int(goldBudget - (silvBudget / 10) - (coppBudget / 100))


def priceFormat(p):
    if float(p) % 1 == 0.0:
        price = str(int(p)) + ' gp'
    elif round(float(p) % 1, 2) == round(float(p) % 1, 1):
        price = str(floor(float(p))) + ' gp ' + str(floor(float(p) * 10) - floor(float(p)) * 10) + ' sp'
    else:
        price = str(floor(float(p))) + ' gp ' + str(floor(float(p) * 10) - floor(float(p)) * 10) + ' sp ' + \
                str(floor(float(p) * 100) - floor(float(p) * 10) * 10) + ' cp'
    return price


def enchFormat(i):
    i.enchname = ""
    if hasattr(i, 'l_itemEnch'):
        for n in i.l_itemEnch:
            i.enchname = i.enchname + "[" + n.name + "] "
    if hasattr(i, 'magic'):
        i.enchname = i.magic + "" + i.enchname + ""
    elif i.is_Mwk:
        i.enchname = "Masterwork "
    return i.enchname


def modFormat(i):
    i.modname = ""
    if hasattr(i, 'mod'):
        i.modname = '{' + i.mod.name + '}'
    return i.modname


def startup():
    global itemlist, list_nmi, list_nma, list_nmw, list_nmu, list_ma, list_mw, list_mu, list_st, list_ro, list_wie, \
        list_wis, list_cur, list_art, list_pot, list_ri

    with open('Resources/items.json') as j:
        data = json.load(j)
        list_nmi = [Item(i) for i in data["Nonmagical Items"]]
        list_nma = [Item(i) for i in data["Nonmagical Armor"]]
        list_nmw = [Item(i) for i in data["Nonmagical Weapons"]]
        list_nmu = [Item(i) for i in data["Nonmagical Ammunition"]]
        list_ma = [Item(i) for i in data["Magical Armor"]]
        list_mw = [Item(i) for i in data["Magical Weapons"]]
        list_mu = [Item(i) for i in data["Magical Ammunition"]]
        list_st = [Item(i) for i in data["Staves"]]
        list_ro = [Item(i) for i in data["Rods"]]
        list_ri = [Item(i) for i in data["Rings"]]
        list_wie = [Item(i) for i in data["Wondrous Items (Equipment)"]]
        list_wis = [Item(i) for i in data["Wondrous Items (Slotless)"]]
        list_cur = [Item(i) for i in data["Cursed Items"]]

    with open('Resources/spells.json') as j:
        data = json.load(j)

        for i in data["spelllist"]:
            if i.get("ispotion"):
                list_pot.append(Spelltoitem(i))
            if i.get("iswand"):
                list_wnd.append(Spelltoitem(i))
            if i.get("isscroll"):
                list_scr.append(Spelltoitem(i))

        for i in list_pot:
            i.calculate_potion_price()
            i.name_pot()

        for i in list_wnd:
            i.calculate_wand_price()
            i.name_wand()

        for i in list_scr:
            i.calculate_scroll_price()
            i.name_scroll()

    with open('Resources/materials.json') as j:
        data = json.load(j)
        for i in data["Core"]:
            materialslist.append(Material(i))
        for i in data["Adventurers Armory"]:
            materialslist.append(Material(i))
        for i in data["Ultimate Equipment"]:
            materialslist.append(Material(i))
        for i in data["Player Companion"]:
            materialslist.append(Material(i))
        for i in data["Adventure Path"]:
            materialslist.append(Material(i))
        for i in data["Distant Realms Campaign Setting"]:
            materialslist.append(Material(i))
        for i in data["Comic Book"]:
            materialslist.append(Material(i))


startup()
