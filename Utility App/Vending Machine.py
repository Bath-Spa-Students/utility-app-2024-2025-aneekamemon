
# Vending Machine - Aneeka Memon


# The title for the vending machine 

# This design has been taken from the ASCII art webpage

print ("\n\n")      # Creating space for a cleaner look...

    #       INFO ON THE TITLE TEXT:

    # 1. Printing 4 spaces further to the right allows for a cleaner look, as it pushes the title towards the center. 

    # 2. Lines have been added to create a appealing design...

    # 3. The design consists of of greater and lesser sign symbols as well as the equal sign symbol which stretches up-to 160 spaces

    # 4. A vertical bar pushed 5 spaces to the right has been added to the title to put the title text into a box...

print ( " "*4 + "<" + "="*160 + ">" )
print ("""\
    |                                                                                                                                                                |
    |    ██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ░█████╗░████████╗  ████████╗██╗░░██╗███████╗  ░█████╗░░█████╗░██████╗░███╗░░██╗███████╗██████╗░    |
    |    ██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ██╔══██╗╚══██╔══╝  ╚══██╔══╝██║░░██║██╔════╝  ██╔══██╗██╔══██╗██╔══██╗████╗░██║██╔════╝██╔══██╗    |
    |    ╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ███████║░░░██║░░░  ░░░██║░░░███████║█████╗░░  ██║░░╚═╝██║░░██║██████╔╝██╔██╗██║█████╗░░██████╔╝    |
    |    ░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██╔══██║░░░██║░░░  ░░░██║░░░██╔══██║██╔══╝░░  ██║░░██╗██║░░██║██╔══██╗██║╚████║██╔══╝░░██╔══██╗    |
    |    ░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░░██║░░░██║░░░  ░░░██║░░░██║░░██║███████╗  ╚█████╔╝╚█████╔╝██║░░██║██║░╚███║███████╗██║░░██║    |  
    |    ░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░╚═╝░░░╚═╝░░░  ░░░╚═╝░░░╚═╝░░╚═╝╚══════╝  ░╚════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚══╝╚══════╝╚═╝░░╚═╝    |
    |                                                                                                                                                                |  """)
print (" "*4 + "<" + "="*160 + ">")
print ("\n\n")



# Defining a dictionary which contains different items categorised by 1. Snacks, 2. Drinks, 3. Specialties.

# The items dictionary 

# For now the dictionary contains three main categories for the items; the product name, it's price, and the amount of stock that is available. 

# A tag system is also incorporated into the dictionaries, which will later come in handy when a filter is added to allow users to find items quicker.  -->

# A code system is added to ease the action of selecting items in the inventory. 


#   The main tags allocated to the items are: Gluten Free, Sugar Free, Diabetes Friendly, and Vegan.       <--


items = {

    "Snacks": {             # Start of the Snacks category 

        "Chocolate Bars": {
            1: {"code" : "SC1" , "name" : "Snickers", "price": 3.50, "stock" : 7  },
            2: {"code" : "SC2" , "name" : "KitKat", "price": 2.50, "stock" : 4 },
            3: {"code" : "SC3" , "name" : "Hershey's", "price": 2.00, "stock" : 10 },
            4: {"code" : "SC4" , "name" : "Milky Way", "price": 1.99, "stock" : 9 },
            },

        "Chips": {
            5: {"code" : "C1" , "name" : "Lay's (Classic)", "price": 1.00, "stock" : 5, "tags": ["Gluten Free"] },
            6: {"code" : "C2" , "name" : "Lay's (BBQ)", "price": 1.00, "stock" : 1  },
            7: {"code" : "C3" , "name" : "Lay's (Sour Cream)", "price": 2.00, "stock" : 3  },
            8: {"code" : "C4" , "name" : "Lay's (Salt & Vinegar)", "price": 2.00, "stock" : 7, "tags": ["Gluten Free"]  },
            9: {"code" : "C5" , "name" : "Pringles (Classic)", "price": 2.00, "stock" : 5  },
            10: {"code" : "C6" , "name" : "Pringles (Hot & BBQ)", "price": 2.00, "stock" : 4  },
            11: {"code" : "C7" , "name" : "Pringles (Cheddar Jalepeno)", "price": 3.00, "stock" : 10  },
            12: {"code" : "C8" , "name" : "Cheetos (Classic)", "price": 1.00, "stock" : 15 },
            13: {"code" : "C9" , "name" : "Cheetos (Flamin' Hot)", "price": 1.00, "stock" : 1 },
            14: {"code" : "C10" , "name" : "Ruffles (Originals)", "price": 3.00, "stock" : 1, "tags": ["Vegan"] },
            15: {"code" : "C11" , "name" : "Chips Omani", "price": 5.00, "stock" : 13, "tags": ["Gluten Free, Diabetes Friendly"] },
        },

        "Crackers & Cookies": {
            16: {"code" : "CC1" , "name" : "Ritz", "price": 1.50, "stock" : 3 },
            17: {"code" : "CC2" , "name" : "Oreos", "price": 2.50, "stock" : 5 },
            18: {"code" : "CC3" , "name" : "Cheez-Its", "price": 1.00, "stock" : 1 },
            19: {"code" : "CC4" , "name" : "Nutter Butterz", "price": 3.50, "stock" : 9 },
        },

        "Candy": {
            20: {"code" : "CA1" , "name" : "M&Ms", "price": 4.50, "stock" : 15 },
            21: {"code" : "CA2" , "name" : "M&Ms (Peanuts)", "price": 5.00, "stock" : 1 },
            22: {"code" : "CA3" , "name" : "Skittles", "price": 4.50, "stock" : 0 },
            23: {"code" : "CA4" , "name" : "Skittles (Sour)", "price": 5.50, "stock" : 2 },
            24: {"code" : "CA5" , "name" : "Juicy Fruitz", "price": 0.50, "stock" : 30 },
            25: {"code" : "CA26" , "name" : "Starbursts", "price": 2.75, "stock" : 8 },
        },
    },      # End of the Snacks category 




    "Drinks": {     # Start of the Drinks category 

        "water": {
            26: {"code" : "W1" , "name" : "Water", "price": 0.99, "stock" : 0, "tags": ["Gluten Free, Sugar Free"]},
            27: {"code" : "W3" , "name" : "Water (Sparkling)", "price": 3.99, "stock" : 5, "tags": ["Gluten Free"] },
            28: {"code" : "W2" , "name" : "Vitamin Water", "price": 4.25, "stock" : 1, "tags": ["Gluten Free, Sugar Free"] },
        },

        "Energy Drinks": {
            29: {"code" : "EE1" , "name" : "Red bull", "price": 7.25, "stock" : 0, "tags": ["Gluten Free"] },
            30: {"code" : "EE2" , "name" : "Red bull (Cherry)", "price": 7.99, "stock" : 1, "tags": ["Gluten Free"] },
            31: {"code" : "EE3" , "name" : "MONSTER ENERGY", "price": 9.65, "stock" : 1 },
        },

        "Soda & Soft Drinks": {
            32: {"code" : "SS1" , "name" : "Coke", "price": 2.00, "stock" : 0 },
            33: {"code" : "SS2" , "name" : "Pepsi", "price": 2.00, "stock" : 2 },
            34: {"code" : "SS3" , "name" : "Spite", "price": 2.00, "stock" : 3, "tags": ["Gluten Free"] },
            35: {"code" : "SS4" , "name" : "Dr. Pepper", "price": 4.00, "stock" : 1, "tags": ["Gluten Free"] },
            36: {"code" : "SS5" , "name" : "Mountain Dew", "price": 2.00, "stock" : 6 },
            37: {"code" : "SS6" , "name" : "Fanta", "price": 2.00, "stock" : 4 },
            38: {"code" : "SS7" , "name" : "Diet Coke", "price": 3.00, "stock" : 1, "tags": ["Sugar Free"] },
            39: {"code" : "SS8" , "name" : "Diet Pepsi", "price": 3.00, "stock" : 5, "tags": ["Sugar Free"]  },
            40: {"code" : "SS9" , "name" : "Diet Dew", "price": 3.00, "stock" : 3, "tags": ["Sugar Free"]  },
        },

        "Sports Hydration": {
            41: {"code" : "H1" , "name" : "Gatorade", "price": 5.05, "stock" : 5 },
        },

        "Ice Tea": {
            42: {"code" : "T1" , "name" : "Gold Peak Tea", "price": 3.45, "stock" : 2, "tags": ["Sugar Free"]  },
            43: {"code" : "T2" , "name" : "Lipton Ice Tea (Peach)", "price": 3.75, "stock" : 5 },
            44: {"code" : "T3" , "name" : "Lipton Ice Tea (Lemon)", "price": 3.75, "stock" : 0 },
            45: {"code" : "T4" , "name" : "Lipton Ice Tea (Strawberry Blast)", "price": 2.75, "stock" : 0 },
        },

        "Fruit Juice": {
            46: {"code" : "F1" , "name" : "Tropicana Mango Juice", "price": 2.00, "stock" : 10 },
            47: {"code" : "F2" , "name" : "Newman's Orange Juice", "price": 2.00, "stock" : 1 },
            48: {"code" : "F3" , "name" : "Minute Made Peach", "price": 4.00, "stock" : 0 },
            49: {"code" : "F4" , "name" : "Simply Lemonade", "price": 6.00, "stock" : 1, "tags": ["Sugar Free"]  },
        },

        "coffee": {
            50: {"code" : "CO1" , "name" : "Coffee (Hot)", "price": 4.00, "stock" : 0, "tags": ["Sugar Free"]  },
            51: {"code" : "CO2" , "name" : "Coffee (Iced)", "price": 6.00, "stock" : 1, "tags": ["Sugar Free"]  },
        },
    },          # End of the Drinks category 




    "Specialties": {   # Start of the Specialties category 

        "Healthy Options": {

            "Energy & Granola Bars": {
                52: {"code" : "EG1" , "name" : "Clif Bar", "price": 1.00, "stock" : 4 },
                53: {"code" : "EG2" , "name" : "Nature Valley", "price": 3.99, "stock" : 2, "tags": ["Vegan"] },
                54: {"code" : "EG3" , "name" : "Kind Granola Bar", "price": 3.00, "stock" : 0 },
                55: {"code" : "EG4" , "name" : "Lara Bar", "price": 2.00, "stock" : 1, "tags": ["Gluten Free"] },
            },

            "Jerky & Meat Snacks": {
                56: {"code" : "JM1" , "name" : "Slim Jim", "price": 6.00, "stock" : 7, "tags": ["Gluten Free"] },
                57: {"code" : "JM2" , "name" : "Jack Link's", "price": 6.59, "stock" : 3, "tags": ["Gluten Free"] },
                58: {"code" : "JM3" , "name" : "Perky Jerky", "price": 7.99, "stock" : 2, "tags": ["Gluten Free"] },
                59: {"code" : "JM4" , "name" : "Oberto", "price": 11.75, "stock" : 1, "tags": ["Vegan, Gluten Free"] },
            },
        },

        "Instant Noodles": {
            60: {"code" : "IN1" , "name" : "Chicken Cup Noodles", "price": 4.00, "stock" : 4, "tags": ["Gluten Free"] },
            61: {"code" : "IN2" , "name" : "Beef Cup Noodles", "price": 4.00, "stock" : 2, "tags": ["Gluten Free"] },
            62: {"code" : "IN3" , "name" : "Curry Cup Noodles", "price": 4.75, "stock" : 2 },
            63: {"code" : "IN4" , "name" : "Chili Cup Noodles", "price": 4.00, "stock" : 0 },
            64: {"code" : "IN5" , "name" : "Mushroom Cup Noodles", "price": 5.29, "stock" : 6, "tags": ["Vegan"] },
            65: {"code" : "IN6" , "name" : "Shrimp Cup Noodles", "price": 4.00, "stock" : 1, "tags": ["Gluten Free"] },
        },

        "Sandwiches and Wraps": {

            "Sandwiches": {
                66: {"code" : "SW1" , "name" : "Chicken Sandwich", "price": 3.75, "stock" : 0, "tags": ["Gluten Free"] },
                67: {"code" : "SW2" , "name" : "Seafood Sandwich", "price": 2.75, "stock" : 4, "tags": ["Gluten Free"] },
                68: {"code" : "SW3" , "name" : "Beef Sandwich", "price": 4.99, "stock" : 2, "tags": ["Gluten Free"] },
                69: {"code" : "SW4" , "name" : "Cheese Sandwich", "price": 1.99, "stock" : 4 },
                70: {"code" : "SW5" , "name" : "Salmon Sandwich", "price": 6.75, "stock" : 1, "tags": ["Gluten Free"] },
            },

            "Wraps": {
                71: {"code" : "WP1" , "name" : "Grilled Wrap", "price": 3.00, "stock" : 1, "tags": ["Vegan"] },
                72: {"code" : "WP2" , "name" : "Tuna Wrap", "price": 1.00, "stock" : 8, "tags": ["Gluten Free"] },
                73: {"code" : "WP3" , "name" : "Chicken Wrap", "price": 5.00, "stock" : 3, "tags": ["Gluten Free"] },
                74: {"code" : "WP4" , "name" : "Spud Wrap", "price": 2.30, "stock" : 2 },
            },
        },

        "Fruit Cups": {
            74: {"code" : "FC1" , "name" : "Watermelon Cup", "price": 7.00, "stock" : 3, "tags": ["Vegan"] },
            75: {"code" : "FC2" , "name" : "Pineapple Cup", "price": 8.00, "stock" : 1, "tags": ["Vegan"] },
            76: {"code" : "FC3" , "name" : "Orange Cup", "price": 5.00, "stock" : 8, "tags": ["Vegan"] },
            77: {"code" : "FC4" , "name" : "Kiwi Cup", "price": 8.00, "stock" : 2, "tags": ["Vegan"] },
            78: {"code" : "FC5" , "name" : "Mango Cup", "price": 9.99, "stock" : 4, "tags": ["Vegan"] },
            79: {"code" : "FC6" , "name" : "Pomogranate Cup", "price": 9.99, "stock" : 1, "tags": ["Vegan"] },
            },

        "Dried Fruit Packets": {
            80: {"code" : "DF1" , "name" : "Walnut Packet", "price": 5.25, "stock" : 5, "tags": ["Vegan, Sugar Free"] },
            81: {"code" : "DF2" , "name" : "Pistachios Packet", "price": 6.25, "stock" : 2, "tags": ["Vegan, Sugar Free"] },
            82: {"code" : "DF3" , "name" : "Almond Packet", "price": 5.25, "stock" : 0, "tags": ["Vegan, Sugar Free"] },
            83: {"code" : "DF4" , "name" : "Cashews Packet", "price": 6.25, "stock" : 1, "tags": ["Vegan, Sugar Free"] },
            84: {"code" : "DF5" , "name" : "Dried Apricots Packet", "price": 8.99, "stock" : 5 },
            85: {"code" : "DF6" , "name" : "Dried Figs Packet", "price": 8.99, "stock" : 9 },
            },
    },          # End of the Specialties category 

    }       # End of the Specialties category 
    


# To format specific colors onto the terminal texts, the usage of ANSI escape codes is implemented.




print("\n\n")

    
def snacks_display():
        
        print (("""\033[1;34;30m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\
                            §=======================================================§
                            |                \033[1;34;95mVending at The Corner.\033[0m                 |
                            |                                                       |
                            |           Select a \033[1;34;31msubcategory\033[0m of \033[4;34;92mSnacks\033[0m:             |
                            |                                                       |
                            |                \033[1;34;92m1.\033[0m \033[7;34;33mChocolate Bars\033[0m                      |
                            |                                                       |
                            |                \033[1;34;92m2.\033[0m \033[7;34;33mChips\033[0m                               |
                            |                                                       |
                            |                \033[1;34;92m3.\033[0m \033[7;34;33mCrackers & Cookies\033[0m                  |
                            |                                                       |
                            |                \033[1;34;92m4.\033[0m \033[7;34;33mCandy\033[0m                               |
                            |                                                       |
                            §=======================================================§
""")
        

def drinks_display():
        
        print (("""\033[1;34;30m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\
                            §=======================================================§
                            |                \033[1;34;95mVending at The Corner.\033[0m                 |
                            |                                                       |
                            |           Select a \033[1;34;31msubcategory\033[0m of \033[4;34;92mDrinks\033[0m:             |
                            |                                                       |
                            |                \033[1;34;92m1.\033[0m \033[7;34;33mWater\033[0m                               |
                            |                                                       |
                            |                \033[1;34;92m2.\033[0m \033[7;34;33mEnergy Drinks\033[0m                       |
                            |                                                       |
                            |                \033[1;34;92m3.\033[0m \033[7;34;33mSoda & Soft Drinks\033[0m                  |
                            |                                                       |
                            |                \033[1;34;92m4.\033[0m \033[7;34;33mSports Hydration\033[0m                    |
                            |                                                       |
                            |                \033[1;34;92m5.\033[0m \033[7;34;33mIce Tea\033[0m                             |
                            |                                                       |
                            |                \033[1;34;92m6.\033[0m \033[7;34;33mFruit Juice\033[0m                         |
                            |                                                       |
                            |                \033[1;34;92m7.\033[0m \033[7;34;33mCoffee\033[0m                              |
                            |                                                       |
                            §=======================================================§
""")


def spec_display():
        
        print (("""\033[1;34;30m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\
                            §=======================================================§
                            |                \033[1;34;95mVending at The Corner.\033[0m                 |
                            |                                                       |
                            |           Select a \033[1;34;31msubcategory\033[0m of \033[4;34;92mSpecialties\033[0m:        |
                            |                                                       |
                            |                \033[1;34;92m1.\033[0m \033[7;34;33mHealthy Options\033[0m                     |
                            |                                                       |
                            |                \033[1;34;92m2.\033[0m \033[7;34;33mInstant Noodles\033[0m                     |
                            |                                                       |
                            |                \033[1;34;92m3.\033[0m \033[7;34;33mSandwiches and Wraps\033[0m                |
                            |                                                       |
                            |                \033[1;34;92m4.\033[0m \033[7;34;33mFruit Cups\033[0m                          |
                            |                                                       |
                            |                \033[1;34;92m5.\033[0m \033[7;34;33mDried Fruit Packets\033[0m                 |
                            |                                                       |
                            §=======================================================§
""")



def chocolatebar_snacks_1():
                
        print (("""\033[1;34;31m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |               Select a \033[1;34;31mtype\033[0m of \033[4;34;92mChocolate Bar\033[0m:                 |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m SC1 \033[0m        \033[1;7;36;96m Snickers \033[0m       \033[1;7;32;92m 3.50 \033[0m           \033[1;7;31;91m 7 \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SC2 \033[0m        \033[1;7;36;96m KitKat \033[0m         \033[1;7;32;92m 2.50 \033[0m           \033[1;7;31;91m 4 \033[0m        |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SC3 \033[0m        \033[1;7;36;96m Hershey's \033[0m      \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 10 \033[0m       |                                                                                       
                        |                                                               |
                        |     \033[1;7;31;91m SC4 \033[0m        \033[1;7;36;96m Milky Way \033[0m      \033[1;7;32;92m 1.99 \033[0m           \033[1;7;31;91m 9 \033[0m        |                                                                                                                                                      
                        |                                                               |
                        §===============================================================§
""")


def chips_snacks_2():
                        
        print (("""\n\n\033[1;34;31m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("\n\n" """\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |                   Select a \033[1;34;31mtype\033[0m of \033[4;34;92mChip\033[0m:                      |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m C1 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m 1.00 \033[0m           \033[1;7;31;91m 5 \033[0m         |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m C2 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m 1.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                 \033[1;7;36;96m (BBQ) \033[0m                                       |                                                                                                                              
                        |                                                               |
                        |     \033[1;7;31;91m C3 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 3 \033[0m         |
                        |                 \033[1;7;36;96m (Sour Cream) \033[0m                                |                                                                                                                                                      
                        |                                                               |
                        |     \033[1;7;31;91m C4 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 7 \033[0m         |
                        |                 \033[1;7;36;96m (Salt & \033[0m                                     |  
                        |                 \033[1;7;36;96m Vinegar) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m C5 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 5 \033[0m         |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C6 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 4 \033[0m         |
                        |                 \033[1;7;36;96m (Hot & BBQ) \033[0m                                 |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C7 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m 3.00 \033[0m           \033[1;7;31;91m 10 \033[0m        |
                        |                 \033[1;7;36;96m (Cheddar \033[0m                                    |  
                        |                 \033[1;7;36;96mJalepeno) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m C8 \033[0m        \033[1;7;36;96m Cheetos \033[0m        \033[1;7;32;92m 1.00 \033[0m           \033[1;7;31;91m 15 \033[0m        |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C9 \033[0m        \033[1;7;36;96m Cheetos \033[0m        \033[1;7;32;92m 1.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                 \033[1;7;36;96m (Flamin' Hot) \033[0m                               |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C10 \033[0m       \033[1;7;36;96m Ruffles \033[0m        \033[1;7;32;92m 3.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                 \033[1;7;36;96m (Originals) \033[0m                                 |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C10 \033[0m       \033[1;7;36;96m Chips \033[0m          \033[1;7;32;92m 5.00 \033[0m           \033[1;7;31;91m 13 \033[0m        |
                        |                 \033[1;7;36;96m Omani \033[0m                                       |                                                              
                        |                                                               |                                      
                        §===============================================================§
""")
        

def crackerscookies_snacks_3():
                        
        print (("""\033[1;34;31m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |               Select a \033[1;34;31mtype\033[0m of \033[4;34;92mCracker or Cookie\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m CC1 \033[0m        \033[1;7;36;96m Ritz \033[0m           \033[1;7;32;92m 1.50 \033[0m           \033[1;7;31;91m 3 \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m CC2 \033[0m        \033[1;7;36;96m Oreos \033[0m          \033[1;7;32;92m 2.50 \033[0m           \033[1;7;31;91m 5 \033[0m        |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m CC3 \033[0m        \033[1;7;36;96m Cheez-Its \033[0m      \033[1;7;32;92m 1.00 \033[0m           \033[1;7;31;91m 1 \033[0m        |                                                                                       
                        |                                                               |
                        |     \033[1;7;31;91m CC4 \033[0m        \033[1;7;36;96m Nutter \033[0m         \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 5 \033[0m        |
                        |                  \033[1;7;36;96m Butterz \033[0m                                    |
                        |                                                               |
                        |                                                               |               
                        §===============================================================§
""")
        

def candy_snacks_4():
                        
        print (("""\033[1;34;31m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |                   Select a \033[1;34;31mtype\033[0m of \033[4;34;92mCandy\033[0m:                     |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m CA1 \033[0m          \033[1;7;36;96m M&Ms \033[0m         \033[1;7;32;92m 4.50 \033[0m          \033[1;7;31;91m 15 \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m CA2 \033[0m          \033[1;7;36;96m M&Ms \033[0m         \033[1;7;32;92m 5.00 \033[0m          \033[1;7;31;91m 1 \033[0m         |
                        |                    \033[1;7;36;96m (Peanuts) \033[0m                                |
                        |                                                               |               
                        |     \033[1;7;31;91m CA3 \033[0m          \033[1;7;36;96m Skittles \033[0m     \033[1;7;32;92m 4.50 \033[0m          \033[1;7;31;91m 0 \033[0m         |                                                                                       
                        |                                                               |                                                                                    
                        |     \033[1;7;31;91m CA4 \033[0m          \033[1;7;36;96m Skittles \033[0m     \033[1;7;32;92m 5.00 \033[0m          \033[1;7;31;91m 1 \033[0m         |
                        |                    \033[1;7;36;96m (Sour) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m CA5 \033[0m          \033[1;7;36;96m Juicy \033[0m        \033[1;7;32;92m 0.50 \033[0m          \033[1;7;31;91m 2 \033[0m         |
                        |                    \033[1;7;36;96m Fruitz \033[0m                                   |                                                               
                        |                                                               |
                        §===============================================================§
""")
        


def water_drinks_1():
                                
        print (("""\033[1;34;34m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |                   Select a \033[1;34;31mtype\033[0m of \033[4;34;92mWater\033[0m:                     |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m W1 \033[0m           \033[1;7;36;96m Water \033[0m         \033[1;7;32;92m 0.99 \033[0m          \033[1;7;31;91m 0 \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m W2 \033[0m           \033[1;7;36;96m Vitamin \033[0m       \033[1;7;32;92m 4.25 \033[0m          \033[1;7;31;91m 1 \033[0m        |
                        |                    \033[1;7;36;96m Water \033[0m                                    |
                        |                                                               |               
                        |     \033[1;7;31;91m W3 \033[0m           \033[1;7;36;96m Water \033[0m         \033[1;7;32;92m 3.99 \033[0m          \033[1;7;31;91m 5 \033[0m        |
                        |                    \033[1;7;36;96m (Sparkling) \033[0m                              |                                                               
                        |                                                               |
                        §===============================================================§
""")


def sodasoftdrinks_drinks_2():
                                
        print (("""\n\n\033[1;34;34m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("\n\n" """\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |             Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSoda or Soft Drink\033[0m:              |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m SS1 \033[0m         \033[1;7;36;96m Coke \033[0m         \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                                                               |
                        |     \033[1;7;31;91m SS2 \033[0m         \033[1;7;36;96m Pepsi \033[0m        \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                                                               |
                        |     \033[1;7;31;91m SS3 \033[0m         \033[1;7;36;96m Spite \033[0m        \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 3 \033[0m         |
                        |                                                               |
                        |     \033[1;7;31;91m SS4 \033[0m         \033[1;7;36;96m Dr. \033[0m          \033[1;7;32;92m 4.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Pepper \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m SS5 \033[0m         \033[1;7;36;96m Mountain \033[0m     \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 6 \033[0m         |
                        |                   \033[1;7;36;96m Dew \033[0m                                       |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SS6 \033[0m         \033[1;7;36;96m Fanta \033[0m        \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 4 \033[0m         |
                        |                                                               |
                        |     \033[1;7;31;91m SS7 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m 3.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Coke \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m SS8 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m 3.00 \033[0m           \033[1;7;31;91m 5 \033[0m         |
                        |                   \033[1;7;36;96m Pepsi \033[0m                                     |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SS9 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m 3.00 \033[0m           \033[1;7;31;91m 3 \033[0m         |
                        |                   \033[1;7;36;96m Dew \033[0m                                       |                                                                                                                            
                        |                                                               |                                      
                        §===============================================================§
""")
        

def sportshyd_drinks_3():
                                        
        print (("""\033[1;34;34m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |                   Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSports Drink\033[0m:              |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m H1 \033[0m           \033[1;7;36;96m Gatorade \033[0m     \033[1;7;32;92m 5.05 \033[0m          \033[1;7;31;91m 5 \033[0m         |
                        |                                                               |                                                              
                        §===============================================================§
""")
        

def icetea_drinks_4():
                                        
        print (("""\n\n\033[1;34;34m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("\n\n" """\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |                  Select a \033[1;34;31mtype\033[0m of \033[4;34;92mIce Tea\033[0m:                    |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m T1 \033[0m          \033[1;7;36;96m Gold \033[0m         \033[1;7;32;92m 3.45 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                   \033[1;7;36;96m Peak \033[0m                                      |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T2 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m 3.75 \033[0m           \033[1;7;31;91m 5 \033[0m         |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m (Peach) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T3 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m 3.75 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m (Lemon) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T4 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m 2.75 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m (Strawberry \033[0m                               |
                        |                   \033[1;7;36;96m Blast) \033[0m                                    |                                                                         
                        |                                                               |                                      
                        §===============================================================§
""")


def fruitjuice_drinks_5():
                                        
        print (("""\033[1;34;34m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |                Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Juice\033[0m:                  |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m F1 \033[0m           \033[1;7;36;96m Tropicana \033[0m    \033[1;7;32;92m 2.00 \033[0m          \033[1;7;31;91m 10 \033[0m        |
                        |                    \033[1;7;36;96m Mango \033[0m                                    |
                        |                    \033[1;7;36;96m Juice \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m F2 \033[0m           \033[1;7;36;96m Newman's \033[0m     \033[1;7;32;92m 2.00 \033[0m          \033[1;7;31;91m 1 \033[0m         |
                        |                    \033[1;7;36;96m Orange \033[0m                                   |
                        |                    \033[1;7;36;96m Juice \033[0m                                    |                        
                        |                                                               |
                        |     \033[1;7;31;91m F3 \033[0m           \033[1;7;36;96m Minute \033[0m       \033[1;7;32;92m 4.00 \033[0m          \033[1;7;31;91m 0 \033[0m         |
                        |                    \033[1;7;36;96m Made \033[0m                                     |
                        |                    \033[1;7;36;96m Peach \033[0m                                    |                        
                        |                                                               |               
                        |     \033[1;7;31;91m F4 \033[0m           \033[1;7;36;96m Simply \033[0m       \033[1;7;32;92m 6.00 \033[0m          \033[1;7;31;91m 1 \033[0m         |
                        |                    \033[1;7;36;96m Lemonade \033[0m                                 |                                                               
                        |                                                               |
                        §===============================================================§
""")


def coffee_drinks_6():
                                                
        print (("""\033[1;34;34m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\n\n\
                        §===============================================================§
                        |                   \033[1;34;95mVending at The Corner.\033[0m                      |
                        |                                                               |
                        |                  Select a \033[1;34;31mtype\033[0m of \033[4;34;92mCoffee\033[0m:                     |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m CO1 \033[0m          \033[1;7;36;96m Coffee \033[0m       \033[1;7;32;92m 4.00 \033[0m          \033[1;7;31;91m 0 \033[0m         |
                        |                    \033[1;7;36;96m (Hot) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m CO2 \033[0m          \033[1;7;36;96m Coffee \033[0m       \033[1;7;32;92m 6.00 \033[0m          \033[1;7;31;91m 1 \033[0m         |
                        |                    \033[1;7;36;96m (Iced) \033[0m                                   |
                        |                                                               |
                        §===============================================================§
""")
        

coffee_drinks_6()







def display():
        
        print (("""\033[1;34;30m
         _____                                                                                     _____
        ( ___ )-----------------------------------------------------------------------------------( ___ )
         |   |                                                                                     |   |
         |   | _________          _______    _______  _______  _______  _        _______  _______  |   |
         |   | \__   __/|\     /|(  ____ \  (  ____ \(  ___  )(  ____ )( (    /|(  ____ \(  ____ ) |   |
         |   |    ) (   | )   ( || (    \/  | (    \/| (   ) || (    )||  \  ( || (    \/| (    )| |   |
         |   |    | |   | (___) || (__      | |      | |   | || (____)||   \ | || (__    | (____)| |   |
         |   |    | |   |  ___  ||  __)     | |      | |   | ||     __)| (\ \) ||  __)   |     __) |   |
         |   |    | |   | (   ) || (        | |      | |   | || (\ (   | | \   || (      | (\ (    |   |
         |   |    | |   | )   ( || (____/\  | (____/\| (___) || ) \ \__| )  \  || (____/\| ) \ \__ |   |
         |   |    )_(   |/     \|(_______/  (_______/(_______)|/   \__/|/    )_)(_______/|/   \__/ |   |
         |___|                                                                                     |___|
        (_____)-----------------------------------------------------------------------------------(_____)
\033[0m"""))
        print ("""\
                            §=======================================================§
                            |         \033[1;34;95mWelcome to Vending at 'The Corner'\033[0m            |
                            |                                                       |
                            |         Please select \033[1;34;31m1\033[0m of the \033[1;34;92m3\033[0m categories:          |
                            |                                                       |
                            |                    \033[1;34;92m1.\033[0m \033[7;34;94mSnacks\033[0m                          |
                            |                                                       |
                            |                    \033[1;34;92m2.\033[0m \033[7;34;94mDrinks\033[0m                          |
                            |                                                       |
                            |                    \033[1;34;92m3.\033[0m \033[7;34;94mSpecialties\033[0m                     |
                            |                                                       |
                            §=======================================================§
""")

        selection_no1  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selection_no1}")
        if selection_no1 == "1" or selection_no1.lower() == "snacks":
                snacks_display()
        elif selection_no1 == "2" or selection_no1.lower() == "drinks":
                drinks_display()
        elif selection_no1 == "3" or selection_no1.lower() == "specialties":
                spec_display()
        else: 
                print ("Please ensure to select an option to continue")
                display()


