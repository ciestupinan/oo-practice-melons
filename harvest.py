from pprint import pprint

############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""
        
        self.pairings.append(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code


def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    muskmelon = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    muskmelon.add_pairing('mint')
    all_melon_types.append(muskmelon)

    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    casaba.add_pairing('strawberries')
    casaba.add_pairing('mint')
    all_melon_types.append(casaba)

    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    crenshaw.add_pairing('proscuitto')
    all_melon_types.append(crenshaw)

    yellow_watermellon = MelonType('yw', 2013, 'yellow', False, True, 'Yellow Watermelon')
    yellow_watermellon.add_pairing('ice cream')
    all_melon_types.append(yellow_watermellon)

    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print('{} pairs with'.format(melon.name))
        for pairing in melon.pairings:
            print('- {}'.format(pairing))

    return None


def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    dict_melons = {}

    for melon in melon_types:
        dict_melons[melon.code] = {
        'Name':melon.name, 'First Harvest': melon.first_harvest,
        'Color': melon.color, 'Seedless': str(melon.is_seedless), 'Bestseller': str(melon.is_bestseller)
        }

    return dict_melons


#melon_types = make_melon_types()
#print_pairing_info(melon_types)
#print('\n')
#pprint(make_melon_type_lookup(melon_types))

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    def __init__(self, melon_type, shape_rating, color_rating, field, harvested_by):
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self.field = field
        self.harvested_by = harvested_by

    def is_sellable(self):
        """True is melon is sellable.

            Melon is sellable is shape rating AND color rating are greater than 5
            AND not harvested from field 3"""
        return self.shape_rating > 5 and self.color_rating > 5 and self.field != 3
        

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    melons_by_id = make_melon_type_lookup(melon_types)
    melons = []

    melon_1 = Melon(melons_by_id['yw'], 8, 7, 2, 'Sheila')
    melons.append(melon_1)

    melon_2 = Melon(melons_by_id['yw'], 3, 4, 2, 'Shelia')
    melons.append(melon_2)

    melon_3 = Melon(melons_by_id['yw'], 9, 8, 3, 'Shelia')
    melons.append(melon_3)

    melon_4 = Melon(melons_by_id['cas'], 10, 6, 35, 'Shelia')
    melons.append(melon_4)

    melon_5 = Melon(melons_by_id['cren'], 8, 9, 35, 'Michael')
    melons.append(melon_5)
    
    melon_6 = Melon(melons_by_id['cren'], 8, 2, 35, 'Michael')
    melons.append(melon_6)

    melon_7 = Melon(melons_by_id['cren'], 2, 3, 4, 'Michael')
    melons.append(melon_7)

    melon_8 = Melon(melons_by_id['musk'], 6, 7, 4, 'Michael')
    melons.append(melon_8)

    melon_9 = Melon(melons_by_id['yw'], 7, 10, 3, 'Shelia')
    melons.append(melon_9)

    return melons


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    for melon in melons:
        if melon.is_sellable():
            sellable = "(CAN BE SOLD)"
        else:
            sellable = "(NOT SELLABLE)"

        print('Harvested by {} from Field {} {}'.format(melon.harvested_by, melon.field, sellable))

#print('\n')
#melons = make_melons(melon_types)
#get_sellability_report(melons)



def make_melons_from_file(filename):
    with open(filename) as file:
        """ Create melon objects for each line in the file."""
        
        melon_types = make_melon_types()
        melons_by_id = make_melon_type_lookup(melon_types)

        melons = []

        for line in file:
            
            lst = line.split(" ")
            
            shape_rating = int(lst[1])
            color_rating = int(lst[3])
            code = lst[5]
            field = int(lst[11])
            harvested_by = lst[8]
            
            melons_by_id = make_melon_type_lookup(melon_types)
            
            melon = Melon(melons_by_id[code], shape_rating, color_rating, field, harvested_by)
            melons.append(melon)

        return melons


melons = make_melons_from_file("harvest_log.txt")
pprint(melons)