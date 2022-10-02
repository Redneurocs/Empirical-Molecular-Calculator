from decimal import Rounded
import os

def clear_console():
        command = 'clear'
        if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
            command = 'cls'
        os.system(command)


while True:

    # The periodic table dictionary; shows the atomic mass of an element
    atom_mass = {
        'h': 1,
        'he': 4,
        'li': 7,
        'be': 9,
        'b': 11,
        'c': 12,
        'n': 14,
        'o': 16,
        'f': 19,
        'ne': 20,
        'na': 23,
        'mg': 24,
        'al': 27,
        'si': 28,
        'p': 31,
        's': 32,
        'cl': 35.5,
        'ar': 40,
        'k': 39,
        'ca': 40,
        'sc': 45,
        'ti': 48,
        'v': 51,
        'cr': 52,
        'mn': 55,
        'fe': 56,
        'co': 59,
        'ni': 58.7,
        'cu': 63.5,
        'zn': 65.4,
        'ga': 69.7,
        'ge': 72.6,
        'as': 75,
        'se': 79,
        'br': 80,
        'kr': 83.7,
        'rb': 85.5,
        'sr': 87.6,
        'y': 89,
        'zr': 91.2,
        'nb': 93,
        'mo': 96,
        'tc': 98,
        'ru': 101,
        'rh': 103,
        'pd': 106.4,
        'ag': 108,
        'cd': 112.4,
        'in': 115,
        'sn': 118.7,
        'sb': 121.8,
        'te': 127.6,
        'i': 125,
        'xe': 131.3,
        'cs': 133,
        'ba': 137.3,
        'la': 139,
        'hf': 178.5,
        'ta': 180.1,
        'w': 184,
        're': 186.2,
        'os': 190.2,
        'ir': 192.2,
        'pt': 195,
        'au': 197,
        'hg': 200.6,
        'tl': 204.4,
        'pb': 207.2,
        'bi': 209,
        'po': 209,
        'at': 210,
        'rn': 222,
        'fr': 223,
        'ra': 226,
        'ac': 227,
        'rf': 261,
        'db': 262,
        'sg': 269,
        'bh': 264,
        'hs': 269,
        'mt': 278,
        'ds': 281,
        'rg': 282,
        'cn': 285,
        'nh': 286,
        'fl': 289,
        'mc': 289,
        'lv': 293,
        'ts': 294,
        'og': 294,
        'ce': 140.1,
        'pr': 141,
        'nd': 144.2,
        'pm': 145,
        'sm': 150.4,
        'eu': 152,
        'gd': 157.25,
        'tb': 159,
        'dy': 162.5,
        'ho': 165,
        'er': 167.26,
        'tm': 169,
        'yb': 173,
        'lu': 175,
        'th': 232,
        'pa': 231,
        'u': 238,
        'np': 237,
        'pu': 244,
        'am': 243,
        'cm': 247,
        'bk': 247,
        'cf': 251,
        'es': 252,
        'fm': 257,
        'md': 258,
        'no': 259,
        'lr': 262
    }

    elements_list = [
        'h',
        'he',
        'li',
        'be',
        'b',
        'c',
        'n',
        'o',
        'f',
        'ne',
        'na',
        'mg',
        'al',
        'si',
        'p',
        's',
        'cl',
        'ar',
        'k',
        'ca',
        'sc',
        'ti',
        'v',
        'cr',
        'mn',
        'fe',
        'co',
        'ni',
        'cu',
        'zn',
        'ga',
        'ge',
        'as',
        'se',
        'br',
        'kr',
        'rb',
        'sr',
        'y',
        'zr',
        'nb',
        'mo',
        'tc',
        'ru',
        'rh',
        'pd',
        'ag',
        'cd',
        'in',
        'sn',
        'sb',
        'te',
        'i',
        'xe',
        'cs',
        'ba',
        'la',
        'hf',
        'ta',
        'w',
        're',
        'os',
        'ir',
        'pt',
        'au',
        'hg',
        'tl',
        'pb',
        'bi',
        'po',
        'at',
        'rn',
        'fr',
        'ra',
        'ac',
        'rf',
        'db',
        'sg',
        'bh',
        'hs',
        'mt',
        'ds',
        'rg',
        'cn',
        'nh',
        'fl',
        'mc',
        'lv',
        'ts',
        'og',
        'ce',
        'pr',
        'nd',
        'pm',
        'sm',
        'eu',
        'gd',
        'tb',
        'dy',
        'ho',
        'er',
        'tm',
        'yb',
        'lu',
        'th',
        'pa',
        'u',
        'np',
        'pu',
        'am',
        'cm',
        'bk',
        'cf',
        'es',
        'fm',
        'md',
        'no',
        'lr'
    ]

    # The function that calculates the formula after putting the element and the percentage
    def calculator():
        element = []
        p_over_w = []
        can_input = True

        clear_console()
        print(title)

        # asks the user to input the element symbol
        while can_input:
                element_symbol = input("Enter the element symbol (press enter when no more element): ").lower()
                if element_symbol in elements_list:
                    element.append(element_symbol)
                elif element_symbol == '':
                    can_input = False
                else:
                    print('Invalid Input')

        clear_console()
        print(title)
        # asks the user to input the percentage of the element
        amount_element = 0
        for i in element:
            searched_element = element[amount_element]

            percentage = float(input("Enter the " + str(searched_element).capitalize() + " element's percentage (e.g. 75.05): "))
            atom_weight = atom_mass[searched_element]

            p_over_w.append(percentage / atom_weight)
            amount_element += 1

        # divides the percentage over the mass searched in the dictionary above
        val_index = 0
        divided_min = []
        for i in p_over_w:
            divided_min.append(p_over_w[val_index] / min(p_over_w))
            val_index += 1

        # important lists for storing information while calculating
        val_index = 0
        rounded_1 = []
        str_rounded_1 = []
        doubled = []
        not_doubled = []
        final = []

        # rounds off the float value in tenths
        for i in divided_min:
            rounded_1.append(round(divided_min[val_index], 1))
            
            # converts the float value to string value
            str_rounded_1.append(str(rounded_1[val_index]))
            val_index += 1

        # disects the string value and checks the tenths if it's .5
        str_index = 0
        for i in str_rounded_1:
            list_of_int = [str(x) for x in str_rounded_1[str_index]]
            
            point_index = list_of_int.index('.')
            
            point_5 = "5"
            str_index += 1

        # if the tenths is .5, value is doubled and rounded off, 
        # else, the value stays the same and rounded off
        if point_5 == list_of_int[point_index + 1]:
            is_point5 = True
            
        else:
            is_point5 = False
            

        if is_point5:
            index_val = 0
            for i in rounded_1:
                doubled.append(round(rounded_1[index_val] * 2))
                final.append(doubled[index_val])
                index_val += 1
                
        elif is_point5 == False:
            index_val = 0
            for i in rounded_1:
                not_doubled.append(round(rounded_1[index_val]))
                final.append(not_doubled[index_val])
                index_val += 1
                
        clear_console()
        print(title)
        # prints the formula
        val_index = 0

        print('Empirical Formula:')
        for i in element:
            print(str(element[val_index]).capitalize() + str(final[val_index]))
            val_index += 1
        
        # calculates and prints the empirical mass
        summation = []
        val_index = 0
        for i in element:
            searched_element = element[val_index]
            atom_weight = atom_mass[searched_element]

            summation.append(atom_weight * final[val_index])
            val_index += 1

        empirical_mass = sum(summation)
        print('The Empirical Mass : %s' %empirical_mass)

        will_ask_molecular = True

        # asks if you want to compute for the molecular formula
        while will_ask_molecular:
            get_molecular = input('Do you want to proceed in getting the molecular formula? Y/N: ').lower()
                
            if get_molecular == 'y':
                
                # calculates the molecular formula
                clear_console()
                print(title)
                molecular_subscripts = []
                val_index = 0
                
                print('The Empirical Mass : %s' %empirical_mass)
                molecular_mass = float(input('Please input the given molecular mass: '))
                mole_multiplier = round(molecular_mass / empirical_mass)
                
                clear_console()
                print(title)
                print('The Molecular Mass: %s' %molecular_mass)

                print('Molecular Formula:')
                for i in element:
                    molecular_subscripts.append(mole_multiplier * final[val_index])
                    print(str(element[val_index]).capitalize() + str(molecular_subscripts[val_index]))
                    val_index += 1
                input('Press Enter to Continue: ')
                will_ask_molecular = False

            elif get_molecular == 'n':
                clear_console()
                print(title)
                input('Press Enter to Continue: ')
                will_ask_molecular = False
            else:
                print('Invalid Input')
                input('Press Enter to Continue: ')
                clear_console()
                print(title)
                print('The Empirical Mass : %s' %empirical_mass)
                
                

    # MENU
    clear_console()
    title = '**************************\n*                        *\n*  Empirical Calculator  *\n*      by Rednuerocs     *\n*                        *\n**************************'
    print(title)
    response = input('Use the Calculator? Y/N: ')
    if response.lower() == 'y':
        calculator()
    elif response.lower() == 'n':
        break
    else:
        print('Invalid Input')
        input('Press Enter to Continue: ')
    
