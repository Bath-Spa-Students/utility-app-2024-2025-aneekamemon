
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


# For every one currency unit to the exchange currency unit. with the dollar being the standard





#   The main tags allocated to the items are: Gluten Free, Sugar Free, Diabetes Friendly, and Vegan.       <--


items = {

    "Snacks": {             # Start of the Snacks category 

        "Chocolate Bars": {
            "SC1": {"name" : "Snickers", "price": 3.50, "stock" : 7  },
            "SC2": {"name" : "KitKat", "price": 2.50, "stock" : 4 },
            "SC3": {"name" : "Hershey's", "price": 2.00, "stock" : 10 },
            "SC4": {"name" : "Milky Way", "price": 1.99, "stock" : 9 },
            },

        "Chips": {
            "C1": {"code" : "C1" , "name" : "Lay's (Classic)", "price": 1.00, "stock" : 5, "tags": ["Gluten Free"] },
            "C2": {"code" : "C2" , "name" : "Lay's (BBQ)", "price": 1.00, "stock" : 1  },
            "C3": {"code" : "C3" , "name" : "Lay's (Sour Cream)", "price": 2.00, "stock" : 3  },
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
            "CA1": {"code" : "CA1" , "name" : "M&Ms", "price": 4.50, "stock" : 15 },
            "CA2": {"code" : "CA2" , "name" : "M&Ms (Peanuts)", "price": 5.00, "stock" : 1 },
            "CA3": {"code" : "CA3" , "name" : "Skittles", "price": 4.50, "stock" : 0 },
            "CA4": {"code" : "CA4" , "name" : "Skittles (Sour)", "price": 5.50, "stock" : 2 },
            "CA5": {"code" : "CA5" , "name" : "Juicy Fruitz", "price": 0.50, "stock" : 30 },
            "CA6": {"code" : "CA6" , "name" : "Starbursts", "price": 2.75, "stock" : 8 },
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
                54: {"code" : "EG3" , "name" : "Granola Bar", "price": 3.00, "stock" : 0 },
                55: {"code" : "EG4" , "name" : "Lara Bar", "price": 2.00, "stock" : 1, "tags": ["Gluten Free"] },
            },

            "Jerky & Meat Snacks": {
                56: {"code" : "JM1" , "name" : "Slim Jim", "price": 6.00, "stock" : 7, "tags": ["Gluten Free"] },
                57: {"code" : "JM2" , "name" : "Jack Link's", "price": 6.59, "stock" : 0, "tags": ["Gluten Free"] },
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


#       ANSI escape codes :
# '\033' Starts the escape sequence.
# '[0;34;40m' specifies the formatting.
#   
#  The 0 accounts for different text styles   --> Text styles : 0 = no effect, 1 = bold, 3 = negative, 4 = underlined, 7 = highlighted BG. 
#  ;34; is the text color 
#  ;40m is the background color (40 is black)

#       Here are the different ANSI escape text color codes:    (NORMAL COLOR) [BRIGHT VARIANTS] {BRIGHT BACKGROUND VARIANTS}
#       
#       BLACK (30) [90] {100}             #       MAGENTA (35) [95] {105}  
#       RED (31) [91] {101}               #       CYAN (36) [96] {106}
#       GREEN (32) [92] {102}             #       WHITE (37) [97] {107}
#       YELLOW (33) [93] {103}
#       BLUE (34) [94] {104}



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
        print ("\n" * 5)
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
        print ("\n" * 4)
        
        selectTWO = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTWO}")

        if selectTWO == "1" or selectTWO.lower() in "chocolate bars":
                CurrencyDisplay_ChocolateBar()
        elif selectTWO == "2" or selectTWO.lower() in "chips":
                CurrencyDisplay_Chips()
        elif selectTWO == "3" or selectTWO.lower() in "crackers & cookies" "crackers and cookies":
                CurrencyDisplay_CrackersCookies()
        elif selectTWO == "4" or selectTWO.lower() in "candy":
                CurrencyDisplay_Candy()
        elif selectTWO == "0" or selectTWO.lower() in "exit":
                display()
        else: 
                print ("Please ensure to select an option to continue")
                snacks_display()

        
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
        print ("\n" * 5)
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
        print ("\n" * 4)
        
        selectTHREE = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTHREE}")

        if selectTHREE == "1" or selectTHREE.lower() in "water":
                CurrencyDisplay_Water()
        elif selectTHREE == "2" or selectTHREE.lower() in "energy drinks":
                CurrencyDisplay_EnergyDrinks()
        elif selectTHREE == "3" or selectTHREE.lower() in "soda & soft drinks" "soda and soft drinks":
                CurrencyDisplay_SodaSoftDrinks()
        elif selectTHREE == "4" or selectTHREE.lower() in "sports hydration":
                sportsHyd_drinks_4()
        elif selectTHREE == "5" or selectTHREE.lower() in "ice tea":
                iceTea_drinks_5()
        elif selectTHREE == "6" or selectTHREE.lower() in "fruit juice":
                fruitJuice_drinks_6()
        elif selectTHREE == "7" or selectTHREE.lower() in "coffee":
                coffee_drinks_7()
        elif selectTHREE == "0" or selectTHREE.lower() in "exit":
                display()
        else: 
                print ("Please ensure to select an option to continue")
                drinks_display()


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
        print ("\n" * 4)
        
        selectTHREE = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTHREE}")

        if selectTHREE == "1" or selectTHREE.lower() in "healthy options":
                healthyOptions_spec_1()
        elif selectTHREE == "2" or selectTHREE.lower() in "instant noodles":
                instantNoodles_spec_2()
        elif selectTHREE == "3" or selectTHREE.lower() in "sandwiches and wraps":
                sandWraps_spec_3()
        elif selectTHREE == "4" or selectTHREE.lower() in "fruit cups":
                fruitCups_spec_4()
        elif selectTHREE == "5" or selectTHREE.lower() in "dried fruit packets":
                driedFruitPackets_spec_5()
        elif selectTHREE == "0" or selectTHREE.lower() in "exit":
                display()
        else: 
                print ("Please ensure to select an option to continue")
                spec_display()



def chocolateBar_snacks_1():

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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

ChocolateBars =  {
        "SC1": {"price": 3.50, "stock" : 7 },
        "SC2": {"price": 2.50, "stock" : 4 },
        "SC3": {"price": 2.00, "stock" : 10 },
        "SC4": {"price": 1.99, "stock" : 9 },
}

def chocolateBar_snacks_1USD():

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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in ChocolateBars.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in ChocolateBars.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SC1 \033[0m        \033[1;7;36;96m Snickers \033[0m       \033[1;7;32;92m {convertedcurrency['SC1']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['SC1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SC2 \033[0m        \033[1;7;36;96m KitKat \033[0m         \033[1;7;32;92m {convertedcurrency['SC2']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['SC2']} \033[0m        |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SC3 \033[0m        \033[1;7;36;96m Hershey's \033[0m      \033[1;7;32;92m {convertedcurrency['SC3']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['SC3']} \033[0m       |                                                                                       
                        |                                                               |
                        |     \033[1;7;31;91m SC4 \033[0m        \033[1;7;36;96m Milky Way \033[0m      \033[1;7;32;92m {convertedcurrency['SC4']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['SC4']} \033[0m        |
                        |                                                               |
                        §===============================================================§
""")

def chocolateBar_snacks_1AED():


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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in ChocolateBars.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in ChocolateBars.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SC1 \033[0m        \033[1;7;36;96m Snickers \033[0m       \033[1;7;32;92m {convertedcurrency['SC1']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['SC1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SC2 \033[0m        \033[1;7;36;96m KitKat \033[0m         \033[1;7;32;92m {convertedcurrency['SC2']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SC2']} \033[0m        |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SC3 \033[0m        \033[1;7;36;96m Hershey's \033[0m      \033[1;7;32;92m {convertedcurrency['SC3']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SC3']} \033[0m       |                                                                                       
                        |                                                               |
                        |     \033[1;7;31;91m SC4 \033[0m        \033[1;7;36;96m Milky Way \033[0m      \033[1;7;32;92m {convertedcurrency['SC4']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SC4']} \033[0m        |
                        |                                                               |
                        §===============================================================§
""")

def chocolateBar_snacks_1GBP():


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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in ChocolateBars.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in ChocolateBars.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SC1 \033[0m        \033[1;7;36;96m Snickers \033[0m       \033[1;7;32;92m {convertedcurrency['SC1']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['SC1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SC2 \033[0m        \033[1;7;36;96m KitKat \033[0m         \033[1;7;32;92m {convertedcurrency['SC2']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['SC2']} \033[0m        |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SC3 \033[0m        \033[1;7;36;96m Hershey's \033[0m      \033[1;7;32;92m {convertedcurrency['SC3']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['SC3']} \033[0m       |                                                                                       
                        |                                                               |
                        |     \033[1;7;31;91m SC4 \033[0m        \033[1;7;36;96m Milky Way \033[0m      \033[1;7;32;92m {convertedcurrency['SC4']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['SC4']} \033[0m        |
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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

Chips = {
            "C1": {"price": 1.00, "stock" : 5, "tags": ["Gluten Free"] },
            "C2": {"price": 1.00, "stock" : 1  },
            "C3": {"price": 2.00, "stock" : 3  },
            "C4": {"price": 2.00, "stock" : 7, "tags": ["Gluten Free"] },
            "C5": {"price": 2.00, "stock" : 5  },
            "C6": {"price": 2.00, "stock" : 4 },
            "C7": {"price": 3.00, "stock" : 10  },
            "C8": {"price": 1.00, "stock" : 15 },
            "C9": {"price": 1.00, "stock" : 1 },
            "C10": {"price": 3.00, "stock" : 1, "tags": ["Vegan"]},
            "C11": {"price": 5.00, "stock" : 13, "tags": ["Gluten Free, Diabetes Friendly"] },
}

def chips_snacks_2USD():
                        
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
                        |     \033[1;34;97mCode:        Name:           Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in Chips.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in Chips.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m C1 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C1']} \033[0m        |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m C2 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C2']} \033[0m        |
                        |                 \033[1;7;36;96m (BBQ) \033[0m                                       |                                                                                                                              
                        |                                                               |
                        |     \033[1;7;31;91m C3 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C3']} \033[0m        |
                        |                 \033[1;7;36;96m (Sour Cream) \033[0m                                |                                                                                                                                                      
                        |                                                               |
                        |     \033[1;7;31;91m C4 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C4']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C4']} \033[0m        |
                        |                 \033[1;7;36;96m (Salt & \033[0m                                     |  
                        |                 \033[1;7;36;96m Vinegar) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m C5 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C5']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C5']} \033[0m        |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C6 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C6']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C6']} \033[0m        |
                        |                 \033[1;7;36;96m (Hot & BBQ) \033[0m                                 |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C7 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C7']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C7']} \033[0m       |
                        |                 \033[1;7;36;96m (Cheddar \033[0m                                    |  
                        |                 \033[1;7;36;96mJalepeno) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m C8 \033[0m        \033[1;7;36;96m Cheetos \033[0m        \033[1;7;32;92m {convertedcurrency['C8']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C8']} \033[0m       |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C9 \033[0m        \033[1;7;36;96m Cheetos \033[0m        \033[1;7;32;92m {convertedcurrency['C9']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C9']} \033[0m        |
                        |                 \033[1;7;36;96m (Flamin' Hot) \033[0m                               |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C10 \033[0m       \033[1;7;36;96m Ruffles \033[0m        \033[1;7;32;92m {convertedcurrency['C10']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C10']} \033[0m        |
                        |                 \033[1;7;36;96m (Originals) \033[0m                                 |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C11 \033[0m       \033[1;7;36;96m Chips \033[0m          \033[1;7;32;92m {convertedcurrency['C11']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['C11']} \033[0m       |
                        |                 \033[1;7;36;96m Omani \033[0m                                       |                                                              
                        |                                                               |                                      
                        §===============================================================§
""")
        
def chips_snacks_2AED():
                        
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
                        |     \033[1;34;97mCode:        Name:            Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in Chips.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in Chips.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m C1 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C1']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['C1']} \033[0m        |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m C2 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C2']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['C2']} \033[0m        |
                        |                 \033[1;7;36;96m (BBQ) \033[0m                                       |                                                                                                                              
                        |                                                               |
                        |     \033[1;7;31;91m C3 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C3']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['C3']} \033[0m        |
                        |                 \033[1;7;36;96m (Sour Cream) \033[0m                                |                                                                                                                                                      
                        |                                                               |
                        |     \033[1;7;31;91m C4 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C4']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['C4']} \033[0m        |
                        |                 \033[1;7;36;96m (Salt & \033[0m                                     |  
                        |                 \033[1;7;36;96m Vinegar) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m C5 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C5']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['C5']} \033[0m        |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C6 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C6']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['C6']} \033[0m        |
                        |                 \033[1;7;36;96m (Hot & BBQ) \033[0m                                 |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C7 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C7']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['C7']} \033[0m       |
                        |                 \033[1;7;36;96m (Cheddar \033[0m                                    |  
                        |                 \033[1;7;36;96mJalepeno) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m C8 \033[0m        \033[1;7;36;96m Cheetos \033[0m        \033[1;7;32;92m {convertedcurrency['C8']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['C8']} \033[0m       |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C9 \033[0m        \033[1;7;36;96m Cheetos \033[0m        \033[1;7;32;92m {convertedcurrency['C9']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['C9']} \033[0m        |
                        |                 \033[1;7;36;96m (Flamin' Hot) \033[0m                               |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C10 \033[0m       \033[1;7;36;96m Ruffles \033[0m        \033[1;7;32;92m {convertedcurrency['C10']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['C10']} \033[0m        |
                        |                 \033[1;7;36;96m (Originals) \033[0m                                 |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C11 \033[0m       \033[1;7;36;96m Chips \033[0m          \033[1;7;32;92m {convertedcurrency['C11']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['C11']} \033[0m       |
                        |                 \033[1;7;36;96m Omani \033[0m                                       |                                                              
                        |                                                               |                                      
                        §===============================================================§
""")

def chips_snacks_2GBP():
                        
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
                        |     \033[1;34;97mCode:        Name:           Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in Chips.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in Chips.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m C1 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C1']} \033[0m        |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m C2 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C2']} \033[0m        |
                        |                 \033[1;7;36;96m (BBQ) \033[0m                                       |                                                                                                                              
                        |                                                               |
                        |     \033[1;7;31;91m C3 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C3']} \033[0m        |
                        |                 \033[1;7;36;96m (Sour Cream) \033[0m                                |                                                                                                                                                      
                        |                                                               |
                        |     \033[1;7;31;91m C4 \033[0m        \033[1;7;36;96m Lay's \033[0m          \033[1;7;32;92m {convertedcurrency['C4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C4']} \033[0m        |
                        |                 \033[1;7;36;96m (Salt & \033[0m                                     |  
                        |                 \033[1;7;36;96m Vinegar) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m C5 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C5']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C5']} \033[0m        |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C6 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C6']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C6']} \033[0m        |
                        |                 \033[1;7;36;96m (Hot & BBQ) \033[0m                                 |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C7 \033[0m        \033[1;7;36;96m Pringles \033[0m       \033[1;7;32;92m {convertedcurrency['C7']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C7']} \033[0m       |
                        |                 \033[1;7;36;96m (Cheddar \033[0m                                    |  
                        |                 \033[1;7;36;96mJalepeno) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m C8 \033[0m        \033[1;7;36;96m Cheetos \033[0m        \033[1;7;32;92m {convertedcurrency['C8']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C8']} \033[0m       |
                        |                 \033[1;7;36;96m (Classic) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C9 \033[0m        \033[1;7;36;96m Cheetos \033[0m        \033[1;7;32;92m {convertedcurrency['C9']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C9']} \033[0m        |
                        |                 \033[1;7;36;96m (Flamin' Hot) \033[0m                               |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C10 \033[0m       \033[1;7;36;96m Ruffles \033[0m        \033[1;7;32;92m {convertedcurrency['C10']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C10']} \033[0m        |
                        |                 \033[1;7;36;96m (Originals) \033[0m                                 |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m C11 \033[0m       \033[1;7;36;96m Chips \033[0m          \033[1;7;32;92m {convertedcurrency['C11']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['C11']} \033[0m       |
                        |                 \033[1;7;36;96m Omani \033[0m                                       |                                                              
                        |                                                               |                                      
                        §===============================================================§
""")









def crackersCookies_snacks_3():
                        
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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

CrackersandCookies = {
            "CC1": {"price": 1.50, "stock" : 3 },
            "CC2": {"price": 2.50, "stock" : 5 },
            "CC3": {"price": 1.00, "stock" : 1 },
            "CC4": {"price": 3.50, "stock" : 9 },
}

def crackersCookies_snacks_3USD():
                        
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
                        |     \033[1;34;97mCode:         Name:           Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in CrackersandCookies.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in CrackersandCookies.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m CC1 \033[0m        \033[1;7;36;96m Ritz \033[0m           \033[1;7;32;92m {convertedcurrency['CC1']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CC1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m CC2 \033[0m        \033[1;7;36;96m Oreos \033[0m          \033[1;7;32;92m {convertedcurrency['CC2']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CC2']} \033[0m        |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m CC3 \033[0m        \033[1;7;36;96m Cheez-Its \033[0m      \033[1;7;32;92m {convertedcurrency['CC3']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CC3']} \033[0m        |                                                                                       
                        |                                                               |
                        |     \033[1;7;31;91m CC4 \033[0m        \033[1;7;36;96m Nutter \033[0m         \033[1;7;32;92m {convertedcurrency['CC4']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CC4']} \033[0m        |
                        |                  \033[1;7;36;96m Butterz \033[0m                                    |
                        |                                                               |
                        |                                                               |               
                        §===============================================================§
""")

def crackersCookies_snacks_3GBP():
                        
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
                        |     \033[1;34;97mCode:         Name:           Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in CrackersandCookies.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in CrackersandCookies.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m CC1 \033[0m        \033[1;7;36;96m Ritz \033[0m           \033[1;7;32;92m {convertedcurrency['CC1']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CC1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m CC2 \033[0m        \033[1;7;36;96m Oreos \033[0m          \033[1;7;32;92m {convertedcurrency['CC2']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CC2']} \033[0m        |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m CC3 \033[0m        \033[1;7;36;96m Cheez-Its \033[0m      \033[1;7;32;92m {convertedcurrency['CC3']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CC3']} \033[0m        |                                                                                       
                        |                                                               |
                        |     \033[1;7;31;91m CC4 \033[0m        \033[1;7;36;96m Nutter \033[0m         \033[1;7;32;92m {convertedcurrency['CC4']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CC4']} \033[0m        |
                        |                  \033[1;7;36;96m Butterz \033[0m                                    |
                        |                                                               |
                        |                                                               |               
                        §===============================================================§
""")

def crackersCookies_snacks_3AED():
                        
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
                        |     \033[1;34;97mCode:         Name:            Price:         Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in CrackersandCookies.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in CrackersandCookies.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m CC1 \033[0m        \033[1;7;36;96m Ritz \033[0m           \033[1;7;32;92m {convertedcurrency['CC1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['CC1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m CC2 \033[0m        \033[1;7;36;96m Oreos \033[0m          \033[1;7;32;92m {convertedcurrency['CC2']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['CC2']} \033[0m        |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m CC3 \033[0m        \033[1;7;36;96m Cheez-Its \033[0m      \033[1;7;32;92m {convertedcurrency['CC3']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['CC3']} \033[0m        |                                                                                       
                        |                                                               |
                        |     \033[1;7;31;91m CC4 \033[0m        \033[1;7;36;96m Nutter \033[0m         \033[1;7;32;92m {convertedcurrency['CC4']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['CC4']} \033[0m        |
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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

Candy = {
        "CA1": {"price": 4.50, "stock" : 15 },
        "CA2": {"price": 5.00, "stock" : 1 },
        "CA3": {"price": 4.50, "stock" : 0 },
        "CA4": {"price": 5.50, "stock" : 2 },
        "CA5": {"price": 0.50, "stock" : 30 },
        "CA6": {"price": 2.75, "stock" : 8 },
}

def candy_snacks_4USD():
                        
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in Candy.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in Candy.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m CA1 \033[0m          \033[1;7;36;96m M&Ms \033[0m         \033[1;7;32;92m {convertedcurrency['CA1']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CA1']} \033[0m       |
                        |                                                               |
                        |     \033[1;7;31;91m CA2 \033[0m          \033[1;7;36;96m M&Ms \033[0m         \033[1;7;32;92m {convertedcurrency['CA2']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CA2']} \033[0m        |
                        |                    \033[1;7;36;96m (Peanuts) \033[0m                                |
                        |                                                               |               
                        |     \033[1;7;31;91m CA3 \033[0m          \033[1;7;36;96m Skittles \033[0m     \033[1;7;32;92m {convertedcurrency['CA3']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CA3']} \033[0m        |                                                                                       
                        |                                                               |                                                                                    
                        |     \033[1;7;31;91m CA4 \033[0m          \033[1;7;36;96m Skittles \033[0m     \033[1;7;32;92m {convertedcurrency['CA4']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CA4']} \033[0m        |
                        |                    \033[1;7;36;96m (Sour) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m CA5 \033[0m          \033[1;7;36;96m Juicy \033[0m        \033[1;7;32;92m {convertedcurrency['CA5']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CA5']} \033[0m       |
                        |                    \033[1;7;36;96m Fruitz \033[0m                                   |                                                               
                        |                                                               |
                        §===============================================================§
""")

def candy_snacks_4GBP():
                        
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in Candy.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in Candy.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m CA1 \033[0m          \033[1;7;36;96m M&Ms \033[0m         \033[1;7;32;92m {convertedcurrency['CA1']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CA1']} \033[0m       |
                        |                                                               |
                        |     \033[1;7;31;91m CA2 \033[0m          \033[1;7;36;96m M&Ms \033[0m         \033[1;7;32;92m {convertedcurrency['CA2']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CA2']} \033[0m        |
                        |                    \033[1;7;36;96m (Peanuts) \033[0m                                |
                        |                                                               |               
                        |     \033[1;7;31;91m CA3 \033[0m          \033[1;7;36;96m Skittles \033[0m     \033[1;7;32;92m {convertedcurrency['CA3']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CA3']} \033[0m        |                                                                                       
                        |                                                               |                                                                                    
                        |     \033[1;7;31;91m CA4 \033[0m          \033[1;7;36;96m Skittles \033[0m     \033[1;7;32;92m {convertedcurrency['CA4']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CA4']} \033[0m        |
                        |                    \033[1;7;36;96m (Sour) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m CA5 \033[0m          \033[1;7;36;96m Juicy \033[0m        \033[1;7;32;92m {convertedcurrency['CA5']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CA5']} \033[0m       |
                        |                    \033[1;7;36;96m Fruitz \033[0m                                   |                                                               
                        |                                                               |
                        §===============================================================§
""")

def candy_snacks_4AED():
                        
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in Candy.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in Candy.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m CA1 \033[0m          \033[1;7;36;96m M&Ms \033[0m         \033[1;7;32;92m {convertedcurrency['CA1']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['CA1']} \033[0m       |
                        |                                                               |
                        |     \033[1;7;31;91m CA2 \033[0m          \033[1;7;36;96m M&Ms \033[0m         \033[1;7;32;92m {convertedcurrency['CA2']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['CA2']} \033[0m        |
                        |                    \033[1;7;36;96m (Peanuts) \033[0m                                |
                        |                                                               |               
                        |     \033[1;7;31;91m CA3 \033[0m          \033[1;7;36;96m Skittles \033[0m     \033[1;7;32;92m {convertedcurrency['CA3']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['CA3']} \033[0m        |                                                                                       
                        |                                                               |                                                                                    
                        |     \033[1;7;31;91m CA4 \033[0m          \033[1;7;36;96m Skittles \033[0m     \033[1;7;32;92m {convertedcurrency['CA4']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['CA4']} \033[0m        |
                        |                    \033[1;7;36;96m (Sour) \033[0m                                   |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m CA5 \033[0m          \033[1;7;36;96m Juicy \033[0m        \033[1;7;32;92m {convertedcurrency['CA5']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['CA5']} \033[0m       |
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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

water = {
            "W1": {"price": 0.99, "stock" : 0, "tags": ["Gluten Free, Sugar Free"]},
            "W3": {"price": 3.99, "stock" : 5, "tags": ["Gluten Free"] },
            "W2": {"price": 4.25, "stock" : 1, "tags": ["Gluten Free, Sugar Free"]},
}

def water_drinks_1USD():
                                
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
                        |     \033[1;34;97mCode:           Name:          Price:         Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in water.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in water.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m W1 \033[0m           \033[1;7;36;96m Water \033[0m         \033[1;7;32;92m {convertedcurrency['W1']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['W1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m W2 \033[0m           \033[1;7;36;96m Vitamin \033[0m       \033[1;7;32;92m {convertedcurrency['W2']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['W2']} \033[0m        |
                        |                    \033[1;7;36;96m Water \033[0m                                    |
                        |                                                               |               
                        |     \033[1;7;31;91m W3 \033[0m           \033[1;7;36;96m Water \033[0m         \033[1;7;32;92m {convertedcurrency['W3']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['W3']} \033[0m        |
                        |                    \033[1;7;36;96m (Sparkling) \033[0m                              |                                                               
                        |                                                               |
                        §===============================================================§
""")

def water_drinks_1GBP():
                                
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in water.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in water.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m W1 \033[0m           \033[1;7;36;96m Water \033[0m        \033[1;7;32;92m {convertedcurrency['W1']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['W1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m W2 \033[0m           \033[1;7;36;96m Vitamin \033[0m      \033[1;7;32;92m {convertedcurrency['W2']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['W2']} \033[0m        |
                        |                    \033[1;7;36;96m Water \033[0m                                    |
                        |                                                               |               
                        |     \033[1;7;31;91m W3 \033[0m           \033[1;7;36;96m Water \033[0m        \033[1;7;32;92m {convertedcurrency['W3']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['W3']} \033[0m        |
                        |                    \033[1;7;36;96m (Sparkling) \033[0m                              |                                                               
                        |                                                               |
                        §===============================================================§
""")

def water_drinks_1AED():
                                
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
                        |     \033[1;34;97mCode:           Name:          Price:         Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in water.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in water.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m W1 \033[0m           \033[1;7;36;96m Water \033[0m        \033[1;7;32;92m {convertedcurrency['W1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['W1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m W2 \033[0m           \033[1;7;36;96m Vitamin \033[0m      \033[1;7;32;92m {convertedcurrency['W2']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['W2']} \033[0m        |
                        |                    \033[1;7;36;96m Water \033[0m                                    |
                        |                                                               |               
                        |     \033[1;7;31;91m W3 \033[0m           \033[1;7;36;96m Water \033[0m        \033[1;7;32;92m {convertedcurrency['W3']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['W3']} \033[0m        |
                        |                    \033[1;7;36;96m (Sparkling) \033[0m                              |                                                               
                        |                                                               |
                        §===============================================================§
""")









def energyDrink_drinks_2():
                                        
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
                        |                Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy Drink\033[0m:                 |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m EE1 \033[0m          \033[1;7;36;96m Red \033[0m          \033[1;7;32;92m 7.25 \033[0m          \033[1;7;31;91m 0 \033[0m         |
                        |                    \033[1;7;36;96m Bull \033[0m                                     |               
                        |                                                               |
                        |     \033[1;7;31;91m EE2 \033[0m          \033[1;7;36;96m Red \033[0m          \033[1;7;32;92m 7.99 \033[0m          \033[1;7;31;91m 1 \033[0m         |
                        |                    \033[1;7;36;96m Bull \033[0m                                     |
                        |                    \033[1;7;36;96m (Cherry) \033[0m                                 |               
                        |                                                               |               
                        |     \033[1;7;31;91m EE3 \033[0m          \033[1;7;36;96m MONSTER \033[0m      \033[1;7;32;92m 9.65 \033[0m          \033[1;7;31;91m 1 \033[0m         |
                        |                    \033[1;7;36;96m ENERGY \033[0m                                   |                                                               
                        |                                                               |
                        §===============================================================§
""")

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

EnergyDrinks = {
        "EE1": {"price": 7.25, "stock" : 0, "tags": ["Gluten Free"] },
        "EE2": {"price": 7.99, "stock" : 1, "tags": ["Gluten Free"] },
        "EE3": {"price": 9.65, "stock" : 1 },
}

def energyDrink_drinks_2USD():
                                        
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
                        |                Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy Drink\033[0m:                 |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in EnergyDrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in EnergyDrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m EE1 \033[0m          \033[1;7;36;96m Red \033[0m          \033[1;7;32;92m {convertedcurrency['EE1']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['EE1']} \033[0m        |
                        |                    \033[1;7;36;96m Bull \033[0m                                     |               
                        |                                                               |
                        |     \033[1;7;31;91m EE2 \033[0m          \033[1;7;36;96m Red \033[0m          \033[1;7;32;92m {convertedcurrency['EE2']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['EE2']} \033[0m        |
                        |                    \033[1;7;36;96m Bull \033[0m                                     |
                        |                    \033[1;7;36;96m (Cherry) \033[0m                                 |               
                        |                                                               |               
                        |     \033[1;7;31;91m EE3 \033[0m          \033[1;7;36;96m MONSTER \033[0m      \033[1;7;32;92m {convertedcurrency['EE3']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['EE3']} \033[0m        |
                        |                    \033[1;7;36;96m ENERGY \033[0m                                   |                                                               
                        |                                                               |
                        §===============================================================§
""")

def energyDrink_drinks_2GBP():
                                        
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
                        |                Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy Drink\033[0m:                 |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in EnergyDrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in EnergyDrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m EE1 \033[0m          \033[1;7;36;96m Red \033[0m          \033[1;7;32;92m {convertedcurrency['EE1']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['EE1']} \033[0m        |
                        |                    \033[1;7;36;96m Bull \033[0m                                     |               
                        |                                                               |
                        |     \033[1;7;31;91m EE2 \033[0m          \033[1;7;36;96m Red \033[0m          \033[1;7;32;92m {convertedcurrency['EE2']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['EE2']} \033[0m        |
                        |                    \033[1;7;36;96m Bull \033[0m                                     |
                        |                    \033[1;7;36;96m (Cherry) \033[0m                                 |               
                        |                                                               |               
                        |     \033[1;7;31;91m EE3 \033[0m          \033[1;7;36;96m MONSTER \033[0m      \033[1;7;32;92m {convertedcurrency['EE3']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['EE3']} \033[0m        |
                        |                    \033[1;7;36;96m ENERGY \033[0m                                   |                                                               
                        |                                                               |
                        §===============================================================§
""")

def energyDrink_drinks_2AED():
                                        
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
                        |                Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy Drink\033[0m:                 |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in EnergyDrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in EnergyDrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m EE1 \033[0m          \033[1;7;36;96m Red \033[0m         \033[1;7;32;92m {convertedcurrency['EE1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['EE1']} \033[0m        |
                        |                    \033[1;7;36;96m Bull \033[0m                                     |               
                        |                                                               |
                        |     \033[1;7;31;91m EE2 \033[0m          \033[1;7;36;96m Red \033[0m         \033[1;7;32;92m {convertedcurrency['EE2']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['EE2']} \033[0m        |
                        |                    \033[1;7;36;96m Bull \033[0m                                     |
                        |                    \033[1;7;36;96m (Cherry) \033[0m                                 |               
                        |                                                               |               
                        |     \033[1;7;31;91m EE3 \033[0m          \033[1;7;36;96m MONSTER \033[0m     \033[1;7;32;92m {convertedcurrency['EE3']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['EE3']} \033[0m        |
                        |                    \033[1;7;36;96m ENERGY \033[0m                                   |                                                               
                        |                                                               |
                        §===============================================================§
""")








def sodaSoftDrinks_drinks_3():
                                
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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

SodaSoftDrinks = {
            "SS1": {"price": 2.00, "stock" : 0 },
            "SS2": {"price": 2.00, "stock" : 2 },
            "SS3": {"price": 2.00, "stock" : 3, "tags": ["Gluten Free"] },
            "SS4": {"price": 4.00, "stock" : 1, "tags": ["Gluten Free"]},
            "SS5": {"price": 2.00, "stock" : 6 },
            "SS6": {"price": 2.00, "stock" : 4 },
            "SS7": {"price": 3.00, "stock" : 1, "tags": ["Sugar Free"] },
            "SS8": {"price": 3.00, "stock" : 5, "tags": ["Sugar Free"] },
            "SS9": {"price": 3.00, "stock" : 3, "tags": ["Sugar Free"] },
}

def sodaSoftDrinks_drinks_3USD():
                                
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in SodaSoftDrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in SodaSoftDrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SS1 \033[0m         \033[1;7;36;96m Coke \033[0m         \033[1;7;32;92m {convertedcurrency['SS1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS2 \033[0m         \033[1;7;36;96m Pepsi \033[0m        \033[1;7;32;92m {convertedcurrency['SS2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS2']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS3 \033[0m         \033[1;7;36;96m Spite \033[0m        \033[1;7;32;92m {convertedcurrency['SS3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS3']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS4 \033[0m         \033[1;7;36;96m Dr. \033[0m          \033[1;7;32;92m {convertedcurrency['SS4']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS4']} \033[0m        |
                        |                   \033[1;7;36;96m Pepper \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m SS5 \033[0m         \033[1;7;36;96m Mountain \033[0m     \033[1;7;32;92m {convertedcurrency['SS5']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS5']} \033[0m        |
                        |                   \033[1;7;36;96m Dew \033[0m                                       |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SS6 \033[0m         \033[1;7;36;96m Fanta \033[0m        \033[1;7;32;92m {convertedcurrency['SS6']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS6']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS7 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS7']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS7']} \033[0m        |
                        |                   \033[1;7;36;96m Coke \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m SS8 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS8']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS8']} \033[0m        |
                        |                   \033[1;7;36;96m Pepsi \033[0m                                     |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SS9 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS9']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SS9']} \033[0m        |
                        |                   \033[1;7;36;96m Dew \033[0m                                       |                                                                                                                            
                        |                                                               |                                      
                        §===============================================================§
""")

def sodaSoftDrinks_drinks_3GBP():
                                
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in SodaSoftDrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in SodaSoftDrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SS1 \033[0m         \033[1;7;36;96m Coke \033[0m         \033[1;7;32;92m {convertedcurrency['SS1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS2 \033[0m         \033[1;7;36;96m Pepsi \033[0m        \033[1;7;32;92m {convertedcurrency['SS2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS2']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS3 \033[0m         \033[1;7;36;96m Spite \033[0m        \033[1;7;32;92m {convertedcurrency['SS3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS3']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS4 \033[0m         \033[1;7;36;96m Dr. \033[0m          \033[1;7;32;92m {convertedcurrency['SS4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS4']} \033[0m        |
                        |                   \033[1;7;36;96m Pepper \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m SS5 \033[0m         \033[1;7;36;96m Mountain \033[0m     \033[1;7;32;92m {convertedcurrency['SS5']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS5']} \033[0m        |
                        |                   \033[1;7;36;96m Dew \033[0m                                       |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SS6 \033[0m         \033[1;7;36;96m Fanta \033[0m        \033[1;7;32;92m {convertedcurrency['SS6']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS6']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS7 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS7']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS7']} \033[0m        |
                        |                   \033[1;7;36;96m Coke \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m SS8 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS8']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS8']} \033[0m        |
                        |                   \033[1;7;36;96m Pepsi \033[0m                                     |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SS9 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS9']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SS9']} \033[0m        |
                        |                   \033[1;7;36;96m Dew \033[0m                                       |                                                                                                                            
                        |                                                               |                                      
                        §===============================================================§
""")

def sodaSoftDrinks_drinks_3AED():
                                
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
                        |     \033[1;34;97mCode:         Name:           Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in SodaSoftDrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in SodaSoftDrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SS1 \033[0m         \033[1;7;36;96m Coke \033[0m         \033[1;7;32;92m {convertedcurrency['SS1']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['SS1']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS2 \033[0m         \033[1;7;36;96m Pepsi \033[0m        \033[1;7;32;92m {convertedcurrency['SS2']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['SS2']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS3 \033[0m         \033[1;7;36;96m Spite \033[0m        \033[1;7;32;92m {convertedcurrency['SS3']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['SS3']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS4 \033[0m         \033[1;7;36;96m Dr. \033[0m          \033[1;7;32;92m {convertedcurrency['SS4']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SS4']} \033[0m        |
                        |                   \033[1;7;36;96m Pepper \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m SS5 \033[0m         \033[1;7;36;96m Mountain \033[0m     \033[1;7;32;92m {convertedcurrency['SS5']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['SS5']} \033[0m        |
                        |                   \033[1;7;36;96m Dew \033[0m                                       |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SS6 \033[0m         \033[1;7;36;96m Fanta \033[0m        \033[1;7;32;92m {convertedcurrency['SS6']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['SS6']} \033[0m        |
                        |                                                               |
                        |     \033[1;7;31;91m SS7 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS7']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SS7']} \033[0m        |
                        |                   \033[1;7;36;96m Coke \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m SS8 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS8']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SS8']} \033[0m        |
                        |                   \033[1;7;36;96m Pepsi \033[0m                                     |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m SS9 \033[0m         \033[1;7;36;96m Diet \033[0m         \033[1;7;32;92m {convertedcurrency['SS9']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SS9']} \033[0m        |
                        |                   \033[1;7;36;96m Dew \033[0m                                       |                                                                                                                            
                        |                                                               |                                      
                        §===============================================================§
""")






def sportsHyd_drinks_4():
                                        
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
        
symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

sportsdrinks = {
        "H1" : {"price": 5.05, "stock" : 5 },
}

def sportsHyd_drinks_4USD():
                                        
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
                        |                Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSports Drink\033[0m:                 |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in sportsdrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in sportsdrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m H1 \033[0m          \033[1;7;36;96m Gatorade \033[0m      \033[1;7;32;92m {convertedcurrency['H1']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['H1']} \033[0m        |
                        |                                                               |                                                              
                        §===============================================================§
""")

def sportsHyd_drinks_4GBP():
                                        
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
                        |                Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSports Drink\033[0m:                 |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in sportsdrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in sportsdrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m H1 \033[0m          \033[1;7;36;96m Gatorade \033[0m      \033[1;7;32;92m {convertedcurrency['H1']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['H1']} \033[0m        |
                        |                                                               |                                                              
                        §===============================================================§
""")

def sportsHyd_drinks_4AED():
                                        
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in sportsdrinks.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in sportsdrinks.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m H1 \033[0m          \033[1;7;36;96m Gatorade \033[0m     \033[1;7;32;92m {convertedcurrency['H1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['H1']} \033[0m        |
                        |                                                               |                                                              
                        §===============================================================§
""")







def iceTea_drinks_5():
                                        
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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

icetea = {
        "T1": {"price": 3.45, "stock" : 2, "tags": ["Sugar Free"]  },
        "T2": {"price": 3.75, "stock" : 5 },
        "T3": {"price": 3.75, "stock" : 0 },
        "T4": {"price": 2.75, "stock" : 0 },
}

def iceTea_drinks_5USD():
                                        
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in icetea.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in icetea.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m T1 \033[0m          \033[1;7;36;96m Gold \033[0m         \033[1;7;32;92m {convertedcurrency['T1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['T1']} \033[0m        |
                        |                   \033[1;7;36;96m Peak \033[0m                                      |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T2 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['T2']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Peach) \033[0m                                    |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T3 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['T3']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Lemon) \033[0m                                    |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T4 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T4']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['T4']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Strawberry \033[0m                                |
                        |                   \033[1;7;36;96m Blast) \033[0m                                    |                                                                         
                        |                                                               |                                      
                        §===============================================================§
""")

def iceTea_drinks_5GBP():
                                        
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
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in icetea.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in icetea.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m T1 \033[0m          \033[1;7;36;96m Gold \033[0m         \033[1;7;32;92m {convertedcurrency['T1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['T1']} \033[0m        |
                        |                   \033[1;7;36;96m Peak \033[0m                                      |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T2 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['T2']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Peach) \033[0m                                    |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T3 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['T3']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Lemon) \033[0m                                    |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T4 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['T4']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Strawberry \033[0m                                |
                        |                   \033[1;7;36;96m Blast) \033[0m                                    |                                                                         
                        |                                                               |                                      
                        §===============================================================§
""")

def iceTea_drinks_5AED():
                                        
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
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in icetea.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in icetea.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m T1 \033[0m          \033[1;7;36;96m Gold \033[0m         \033[1;7;32;92m {convertedcurrency['T1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['T1']} \033[0m        |
                        |                   \033[1;7;36;96m Peak \033[0m                                      |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T2 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T2']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['T2']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Peach) \033[0m                                    |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T3 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T3']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['T3']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Lemon) \033[0m                                    |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m T4 \033[0m          \033[1;7;36;96m Lipton \033[0m       \033[1;7;32;92m {convertedcurrency['T4']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['T4']} \033[0m        |
                        |                   \033[1;7;36;96m Ice \033[0m                                       |  
                        |                   \033[1;7;36;96m Tea  \033[0m                                      |                                                               
                        |                   \033[1;7;36;96m(Strawberry \033[0m                                |
                        |                   \033[1;7;36;96m Blast) \033[0m                                    |                                                                         
                        |                                                               |                                      
                        §===============================================================§
""")





def fruitJuice_drinks_6():
                                        
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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

fruitjuice = {
        "F1": {"price": 2.00, "stock" : 10 },
        "F2": {"price": 2.00, "stock" : 1 },
        "F3": {"price": 4.00, "stock" : 0 },
        "F4": {"price": 6.00, "stock" : 1, "tags": ["Sugar Free"]  },
}       

def fruitJuice_drinks_6USD():
                                        
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
                        |     \033[1;34;97mCode:           Name:         Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in fruitjuice.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in fruitjuice.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m F1 \033[0m           \033[1;7;36;96m Tropicana \033[0m    \033[1;7;32;92m {convertedcurrency['F1']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['F1']} \033[0m       |
                        |                    \033[1;7;36;96m Mango \033[0m                                    |
                        |                    \033[1;7;36;96m Juice \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m F2 \033[0m           \033[1;7;36;96m Newman's \033[0m     \033[1;7;32;92m {convertedcurrency['F2']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['F2']} \033[0m        |
                        |                    \033[1;7;36;96m Orange \033[0m                                   |
                        |                    \033[1;7;36;96m Juice \033[0m                                    |                        
                        |                                                               |
                        |     \033[1;7;31;91m F3 \033[0m           \033[1;7;36;96m Minute \033[0m       \033[1;7;32;92m {convertedcurrency['F3']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['F3']} \033[0m        |
                        |                    \033[1;7;36;96m Made \033[0m                                     |
                        |                    \033[1;7;36;96m Peach \033[0m                                    |                        
                        |                                                               |               
                        |     \033[1;7;31;91m F4 \033[0m           \033[1;7;36;96m Simply \033[0m       \033[1;7;32;92m {convertedcurrency['F4']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['F4']} \033[0m        |
                        |                    \033[1;7;36;96m Lemonade \033[0m                                 |                                                               
                        |                                                               |
                        §===============================================================§
""")

def fruitJuice_drinks_6GBP():
                                        
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
                        |     \033[1;34;97mCode:           Name:         Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in fruitjuice.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in fruitjuice.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m F1 \033[0m           \033[1;7;36;96m Tropicana \033[0m    \033[1;7;32;92m {convertedcurrency['F1']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['F1']} \033[0m       |
                        |                    \033[1;7;36;96m Mango \033[0m                                    |
                        |                    \033[1;7;36;96m Juice \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m F2 \033[0m           \033[1;7;36;96m Newman's \033[0m     \033[1;7;32;92m {convertedcurrency['F2']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['F2']} \033[0m        |
                        |                    \033[1;7;36;96m Orange \033[0m                                   |
                        |                    \033[1;7;36;96m Juice \033[0m                                    |                        
                        |                                                               |
                        |     \033[1;7;31;91m F3 \033[0m           \033[1;7;36;96m Minute \033[0m       \033[1;7;32;92m {convertedcurrency['F3']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['F3']} \033[0m        |
                        |                    \033[1;7;36;96m Made \033[0m                                     |
                        |                    \033[1;7;36;96m Peach \033[0m                                    |                        
                        |                                                               |               
                        |     \033[1;7;31;91m F4 \033[0m           \033[1;7;36;96m Simply \033[0m       \033[1;7;32;92m {convertedcurrency['F4']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['F4']} \033[0m        |
                        |                    \033[1;7;36;96m Lemonade \033[0m                                 |                                                               
                        |                                                               |
                        §===============================================================§
""")

def fruitJuice_drinks_6AED():
                                        
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
                        |     \033[1;34;97mCode:           Name:          Price:         Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in fruitjuice.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in fruitjuice.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m F1 \033[0m           \033[1;7;36;96m Tropicana \033[0m    \033[1;7;32;92m {convertedcurrency['F1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['F1']} \033[0m       |
                        |                    \033[1;7;36;96m Mango \033[0m                                    |
                        |                    \033[1;7;36;96m Juice \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m F2 \033[0m           \033[1;7;36;96m Newman's \033[0m     \033[1;7;32;92m {convertedcurrency['F2']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['F2']} \033[0m        |
                        |                    \033[1;7;36;96m Orange \033[0m                                   |
                        |                    \033[1;7;36;96m Juice \033[0m                                    |                        
                        |                                                               |
                        |     \033[1;7;31;91m F3 \033[0m           \033[1;7;36;96m Minute \033[0m       \033[1;7;32;92m {convertedcurrency['F3']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['F3']} \033[0m        |
                        |                    \033[1;7;36;96m Made \033[0m                                     |
                        |                    \033[1;7;36;96m Peach \033[0m                                    |                        
                        |                                                               |               
                        |     \033[1;7;31;91m F4 \033[0m           \033[1;7;36;96m Simply \033[0m       \033[1;7;32;92m {convertedcurrency['F4']:.2f}{symbols['AED']} \033[0m       \033[1;7;31;91m {newstock['F4']} \033[0m        |
                        |                    \033[1;7;36;96m Lemonade \033[0m                                 |                                                               
                        |                                                               |
                        §===============================================================§
""")






def coffee_drinks_7():
                                                
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

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}       

coffee = {
        "CO1": {"price": 4.00, "stock" : 0, "tags": ["Sugar Free"]  },
        "CO2": {"price": 6.00, "stock" : 1, "tags": ["Sugar Free"]  },
}

def coffee_drinks_7USD():
                                                
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
                        |     \033[1;34;97mCode:           Name:         Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in coffee.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in coffee.items():
                newstock[code] = (details["stock"])       
        print(f"""                        |     \033[1;7;31;91m CO1 \033[0m          \033[1;7;36;96m Coffee \033[0m       \033[1;7;32;92m {convertedcurrency['CO1']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CO1']} \033[0m        |
                        |                    \033[1;7;36;96m (Hot) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m CO2 \033[0m          \033[1;7;36;96m Coffee \033[0m       \033[1;7;32;92m {convertedcurrency['CO2']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['CO2']} \033[0m        |
                        |                    \033[1;7;36;96m (Iced) \033[0m                                   |
                        |                                                               |
                        §===============================================================§
""")

def coffee_drinks_7GBP():
                                                
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
                        |     \033[1;34;97mCode:           Name:         Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in coffee.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)   
        newstock = {}
        for code, details in coffee.items():
                newstock[code] = (details["stock"])           
        print(f"""                        |     \033[1;7;31;91m CO1 \033[0m          \033[1;7;36;96m Coffee \033[0m       \033[1;7;32;92m {convertedcurrency['CO1']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CO1']} \033[0m        |
                        |                    \033[1;7;36;96m (Hot) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m CO2 \033[0m          \033[1;7;36;96m Coffee \033[0m       \033[1;7;32;92m {convertedcurrency['CO2']:.2f}{symbols['GBP']} \033[0m          \033[1;7;31;91m {newstock['CO2']} \033[0m        |
                        |                    \033[1;7;36;96m (Iced) \033[0m                                   |
                        |                                                               |
                        §===============================================================§
""")

def coffee_drinks_7AED():
                                                
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
                        |     \033[1;34;97mCode:           Name:         Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in coffee.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in coffee.items():
                newstock[code] = (details["stock"])             
        print(f"""                        |     \033[1;7;31;91m CO1 \033[0m          \033[1;7;36;96m Coffee \033[0m      \033[1;7;32;92m {convertedcurrency['CO1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['CO1']} \033[0m        |
                        |                    \033[1;7;36;96m (Hot) \033[0m                                    |
                        |                                                               |
                        |     \033[1;7;31;91m CO2 \033[0m          \033[1;7;36;96m Coffee \033[0m      \033[1;7;32;92m {convertedcurrency['CO2']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['CO2']} \033[0m        |
                        |                    \033[1;7;36;96m (Iced) \033[0m                                   |
                        |                                                               |
                        §===============================================================§
""")






def healthyOptions_spec_1():
                                        
        print (("""\n\n\033[1;32;32m
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
                        |           Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy or Granola Bar\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m EG1 \033[0m         \033[1;7;36;96m Clif \033[0m         \033[1;7;32;92m 1.00 \033[0m           \033[1;7;31;91m 4 \033[0m         |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m EG2 \033[0m         \033[1;7;36;96m Nature \033[0m       \033[1;7;32;92m 3.99 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                   \033[1;7;36;96m Valley \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m EG3 \033[0m         \033[1;7;36;96m Granola \033[0m      \033[1;7;32;92m 3.00 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m EG4 \033[0m         \033[1;7;36;96m Lara \033[0m         \033[1;7;32;92m 2.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |             Select a \033[1;34;31mtype\033[0m of \033[4;34;92mJerky or Meat Snack\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m JM1 \033[0m         \033[1;7;36;96m Slim \033[0m         \033[1;7;32;92m 6.00 \033[0m           \033[1;7;31;91m 7 \033[0m         |
                        |                   \033[1;7;36;96m Jim \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m JM2 \033[0m         \033[1;7;36;96m Jack \033[0m         \033[1;7;32;92m 6.59 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                   \033[1;7;36;96m Link's \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m JM3 \033[0m         \033[1;7;36;96m Perky \033[0m        \033[1;7;32;92m 7.99 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                   \033[1;7;36;96m Jerky \033[0m                                     |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m JM4 \033[0m         \033[1;7;36;96m Oberto \033[0m       \033[1;7;32;92m 11.75 \033[0m          \033[1;7;31;91m 1 \033[0m         |
                        |                                                               |
                        §===============================================================§
""")

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

healthyoptions = {
        "EG1": {"price": 1.00, "stock" : 4 },
        "EG2": {"price": 3.99, "stock" : 2, "tags": ["Vegan"] },
        "EG3": {"price": 3.00, "stock" : 0 },
        "EG4": {"price": 2.00, "stock" : 1, "tags": ["Gluten Free"] },
        "JM1": {"price": 6.00, "stock" : 7, "tags": ["Gluten Free"] },
        "JM2": {"price": 6.59, "stock" : 0, "tags": ["Gluten Free"] },
        "JM3": {"price": 7.99, "stock" : 2, "tags": ["Gluten Free"] },
        "JM4": {"price": 11.75, "stock" : 1, "tags": ["Vegan, Gluten Free"] },
}

def healthyOptions_spec_1USD():
                                        
        print (("""\n\n\033[1;32;32m
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
                        |           Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy or Granola Bar\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in healthyoptions.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in healthyoptions.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m EG1 \033[0m         \033[1;7;36;96m Clif \033[0m         \033[1;7;32;92m {convertedcurrency['EG1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['EG1']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m EG2 \033[0m         \033[1;7;36;96m Nature \033[0m       \033[1;7;32;92m {convertedcurrency['EG2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['EG2']} \033[0m        |
                        |                   \033[1;7;36;96m Valley \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m EG3 \033[0m         \033[1;7;36;96m Granola \033[0m      \033[1;7;32;92m {convertedcurrency['EG3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['EG3']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m EG4 \033[0m         \033[1;7;36;96m Lara \033[0m         \033[1;7;32;92m {convertedcurrency['EG4']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['EG4']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |             Select a \033[1;34;31mtype\033[0m of \033[4;34;92mJerky or Meat Snack\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m JM1 \033[0m         \033[1;7;36;96m Slim \033[0m         \033[1;7;32;92m {convertedcurrency['JM1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['JM1']} \033[0m        |
                        |                   \033[1;7;36;96m Jim \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m JM2 \033[0m         \033[1;7;36;96m Jack \033[0m         \033[1;7;32;92m {convertedcurrency['JM2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['JM2']} \033[0m        |
                        |                   \033[1;7;36;96m Link's \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m JM3 \033[0m         \033[1;7;36;96m Perky \033[0m        \033[1;7;32;92m {convertedcurrency['JM3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['JM3']} \033[0m        |
                        |                   \033[1;7;36;96m Jerky \033[0m                                     |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m JM4 \033[0m         \033[1;7;36;96m Oberto \033[0m       \033[1;7;32;92m {convertedcurrency['JM4']:.2f}{symbols['USD']} \033[0m          \033[1;7;31;91m {newstock['JM4']} \033[0m        |
                        |                                                               |
                        §===============================================================§
""")

def healthyOptions_spec_1GBP():
                                        
        print (("""\n\n\033[1;32;32m
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
                        |           Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy or Granola Bar\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in healthyoptions.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in healthyoptions.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m EG1 \033[0m         \033[1;7;36;96m Clif \033[0m         \033[1;7;32;92m {convertedcurrency['EG1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['EG1']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m EG2 \033[0m         \033[1;7;36;96m Nature \033[0m       \033[1;7;32;92m {convertedcurrency['EG2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['EG2']} \033[0m        |
                        |                   \033[1;7;36;96m Valley \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m EG3 \033[0m         \033[1;7;36;96m Granola \033[0m      \033[1;7;32;92m {convertedcurrency['EG3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['EG3']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m EG4 \033[0m         \033[1;7;36;96m Lara \033[0m         \033[1;7;32;92m {convertedcurrency['EG4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['EG4']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |             Select a \033[1;34;31mtype\033[0m of \033[4;34;92mJerky or Meat Snack\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m JM1 \033[0m         \033[1;7;36;96m Slim \033[0m         \033[1;7;32;92m {convertedcurrency['JM1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['JM1']} \033[0m        |
                        |                   \033[1;7;36;96m Jim \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m JM2 \033[0m         \033[1;7;36;96m Jack \033[0m         \033[1;7;32;92m {convertedcurrency['JM2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['JM2']} \033[0m        |
                        |                   \033[1;7;36;96m Link's \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m JM3 \033[0m         \033[1;7;36;96m Perky \033[0m        \033[1;7;32;92m {convertedcurrency['JM3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['JM3']} \033[0m        |
                        |                   \033[1;7;36;96m Jerky \033[0m                                     |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m JM4 \033[0m         \033[1;7;36;96m Oberto \033[0m       \033[1;7;32;92m {convertedcurrency['JM4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['JM4']} \033[0m        |
                        |                                                               |
                        §===============================================================§
""")

def healthyOptions_spec_1AED():
                                        
        print (("""\n\n\033[1;32;32m
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
                        |           Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy or Granola Bar\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in healthyoptions.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in healthyoptions.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m EG1 \033[0m         \033[1;7;36;96m Clif \033[0m        \033[1;7;32;92m {convertedcurrency['EG1']:.2f}{symbols['AED']} \033[0m          \033[1;7;31;91m {newstock['EG1']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m EG2 \033[0m         \033[1;7;36;96m Nature \033[0m      \033[1;7;32;92m {convertedcurrency['EG2']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['EG2']} \033[0m        |
                        |                   \033[1;7;36;96m Valley \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m EG3 \033[0m         \033[1;7;36;96m Granola \033[0m     \033[1;7;32;92m {convertedcurrency['EG3']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['EG3']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m EG4 \033[0m         \033[1;7;36;96m Lara \033[0m        \033[1;7;32;92m {convertedcurrency['EG4']:.2f}{symbols['AED']} \033[0m          \033[1;7;31;91m {newstock['EG4']} \033[0m        |
                        |                   \033[1;7;36;96m Bar \033[0m                                       |  
                        |                                                               |
                        |             Select a \033[1;34;31mtype\033[0m of \033[4;34;92mJerky or Meat Snack\033[0m:             |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m JM1 \033[0m         \033[1;7;36;96m Slim \033[0m        \033[1;7;32;92m {convertedcurrency['JM1']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['JM1']} \033[0m        |
                        |                   \033[1;7;36;96m Jim \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m JM2 \033[0m         \033[1;7;36;96m Jack \033[0m        \033[1;7;32;92m {convertedcurrency['JM2']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['JM2']} \033[0m        |
                        |                   \033[1;7;36;96m Link's \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m JM3 \033[0m         \033[1;7;36;96m Perky \033[0m       \033[1;7;32;92m {convertedcurrency['JM3']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['JM3']} \033[0m        |
                        |                   \033[1;7;36;96m Jerky \033[0m                                     |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m JM4 \033[0m         \033[1;7;36;96m Oberto \033[0m      \033[1;7;32;92m {convertedcurrency['JM4']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['JM4']} \033[0m        |
                        |                                                               |
                        §===============================================================§
""")







def instantNoodles_spec_2():
                                                
        print (("""\n\n\033[1;32;32m
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
                        |               Select a \033[1;34;31mtype\033[0m of \033[4;34;92mInstant Noodle\033[0m:                |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m IN1 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m 4.00 \033[0m           \033[1;7;31;91m 4 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |  
                        |                                                               |
                        |     \033[1;7;31;91m IN2 \033[0m         \033[1;7;36;96m Beef \033[0m         \033[1;7;32;92m 4.00 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |                                                               |
                        |     \033[1;7;31;91m IN3 \033[0m         \033[1;7;36;96m Curry \033[0m        \033[1;7;32;92m 4.75 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN4 \033[0m         \033[1;7;36;96m Chili \033[0m        \033[1;7;32;92m 4.00 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |  
                        |                                                               |
                        |     \033[1;7;31;91m IN5 \033[0m         \033[1;7;36;96m Mushroom \033[0m     \033[1;7;32;92m 5.29 \033[0m           \033[1;7;31;91m 6 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |                                                               |
                        |     \033[1;7;31;91m IN6 \033[0m         \033[1;7;36;96m Shrimp \033[0m       \033[1;7;32;92m 4.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |                        
                        §===============================================================§
""")

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

instantnoodles = {
        "IN1": {"price": 4.00, "stock" : 4, "tags": ["Gluten Free"] },
        "IN2": {"price": 4.00, "stock" : 2, "tags": ["Gluten Free"] },
        "IN3": {"price": 4.75, "stock" : 2 },
        "IN4": {"price": 4.00, "stock" : 0 },
        "IN5": {"price": 5.29, "stock" : 6, "tags": ["Vegan"] },
        "IN6": {"price": 4.00, "stock" : 1, "tags": ["Gluten Free"] },
}
      
def instantNoodles_spec_2USD():
                                                
        print (("""\n\n\033[1;32;32m
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
                        |               Select a \033[1;34;31mtype\033[0m of \033[4;34;92mInstant Noodle\033[0m:                |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in instantnoodles.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in instantnoodles.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m IN1 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m {convertedcurrency['IN1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['IN1']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |  
                        |                                                               |
                        |     \033[1;7;31;91m IN2 \033[0m         \033[1;7;36;96m Beef \033[0m         \033[1;7;32;92m {convertedcurrency['IN2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['IN2']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN3 \033[0m         \033[1;7;36;96m Curry \033[0m        \033[1;7;32;92m {convertedcurrency['IN3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['IN3']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN4 \033[0m         \033[1;7;36;96m Chili \033[0m        \033[1;7;32;92m {convertedcurrency['IN4']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['IN4']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |  
                        |                                                               |
                        |     \033[1;7;31;91m IN5 \033[0m         \033[1;7;36;96m Mushroom \033[0m     \033[1;7;32;92m {convertedcurrency['IN5']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['IN5']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN6 \033[0m         \033[1;7;36;96m Shrimp \033[0m       \033[1;7;32;92m {convertedcurrency['IN6']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['IN6']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |                        
                        §===============================================================§
""")

def instantNoodles_spec_2GBP():
                                                
        print (("""\n\n\033[1;32;32m
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
                        |               Select a \033[1;34;31mtype\033[0m of \033[4;34;92mInstant Noodle\033[0m:                |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in instantnoodles.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in instantnoodles.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m IN1 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m {convertedcurrency['IN1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['IN1']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |  
                        |                                                               |
                        |     \033[1;7;31;91m IN2 \033[0m         \033[1;7;36;96m Beef \033[0m         \033[1;7;32;92m {convertedcurrency['IN2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['IN2']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN3 \033[0m         \033[1;7;36;96m Curry \033[0m        \033[1;7;32;92m {convertedcurrency['IN3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['IN3']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN4 \033[0m         \033[1;7;36;96m Chili \033[0m        \033[1;7;32;92m {convertedcurrency['IN4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['IN4']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |  
                        |                                                               |
                        |     \033[1;7;31;91m IN5 \033[0m         \033[1;7;36;96m Mushroom \033[0m     \033[1;7;32;92m {convertedcurrency['IN5']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['IN5']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN6 \033[0m         \033[1;7;36;96m Shrimp \033[0m       \033[1;7;32;92m {convertedcurrency['IN6']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['IN6']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |                        
                        §===============================================================§
""")

def instantNoodles_spec_2AED():
                                                
        print (("""\n\n\033[1;32;32m
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
                        |               Select a \033[1;34;31mtype\033[0m of \033[4;34;92mInstant Noodle\033[0m:                |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in instantnoodles.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in instantnoodles.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m IN1 \033[0m         \033[1;7;36;96m Chicken \033[0m     \033[1;7;32;92m {convertedcurrency['IN1']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['IN1']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |  
                        |                                                               |
                        |     \033[1;7;31;91m IN2 \033[0m         \033[1;7;36;96m Beef \033[0m        \033[1;7;32;92m {convertedcurrency['IN2']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['IN2']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN3 \033[0m         \033[1;7;36;96m Curry \033[0m       \033[1;7;32;92m {convertedcurrency['IN3']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['IN3']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN4 \033[0m         \033[1;7;36;96m Chili \033[0m       \033[1;7;32;92m {convertedcurrency['IN4']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['IN4']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |  
                        |                                                               |
                        |     \033[1;7;31;91m IN5 \033[0m         \033[1;7;36;96m Mushroom \033[0m    \033[1;7;32;92m {convertedcurrency['IN5']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['IN5']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |
                        |     \033[1;7;31;91m IN6 \033[0m         \033[1;7;36;96m Shrimp \033[0m      \033[1;7;32;92m {convertedcurrency['IN6']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['IN6']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                   \033[1;7;36;96m Noodles \033[0m                                   |
                        |                                                               |                        
                        §===============================================================§
""")







def sandWraps_spec_3():
                                                
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSandwich\033[0m:                    |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m SW1 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m 3.75 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW2 \033[0m         \033[1;7;36;96m Seafood \033[0m      \033[1;7;32;92m 2.75 \033[0m           \033[1;7;31;91m 4 \033[0m         |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW3 \033[0m         \033[1;7;36;96m Beef \033[0m         \033[1;7;32;92m 4.99 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW4 \033[0m         \033[1;7;36;96m Cheese \033[0m       \033[1;7;32;92m 1.99 \033[0m           \033[1;7;31;91m 4 \033[0m         |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW5 \033[0m         \033[1;7;36;96m Salmon \033[0m       \033[1;7;32;92m 6.75 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |                   Select a \033[1;34;31mtype\033[0m of \033[4;34;92mWrap\033[0m:                      |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m WP1 \033[0m         \033[1;7;36;96m Grilled \033[0m      \033[1;7;32;92m 3.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m WP2 \033[0m         \033[1;7;36;96m Tuna \033[0m         \033[1;7;32;92m 1.00 \033[0m           \033[1;7;31;91m 8 \033[0m         |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m WP3 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m 5.00 \033[0m           \033[1;7;31;91m 3 \033[0m         |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m WP4 \033[0m         \033[1;7;36;96m Spud \033[0m         \033[1;7;32;92m 2.30 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |                                                               
                        |                                                               |
                        §===============================================================§
""")
                
symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

sandwichswraps = {
        "SW1": {"price": 3.75, "stock" : 0, "tags": ["Gluten Free"] },
        "SW2": {"price": 2.75, "stock" : 4, "tags": ["Gluten Free"] },
        "SW3": {"price": 4.99, "stock" : 2, "tags": ["Gluten Free"] },
        "SW4": {"price": 1.99, "stock" : 4 },
        "SW5": {"price": 6.75, "stock" : 1, "tags": ["Gluten Free"] },
        "WP1": {"price": 3.00, "stock" : 1, "tags": ["Vegan"] },
        "WP2": {"price": 1.00, "stock" : 8, "tags": ["Gluten Free"] },
        "WP3": {"price": 5.00, "stock" : 3, "tags": ["Gluten Free"] },
        "WP4": {"price": 2.30, "stock" : 2 },
}

def sandWraps_spec_3USD():
                                                
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSandwich\033[0m:                    |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in sandwichswraps.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in sandwichswraps.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SW1 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m {convertedcurrency['SW1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SW1']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW2 \033[0m         \033[1;7;36;96m Seafood \033[0m      \033[1;7;32;92m {convertedcurrency['SW2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SW2']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW3 \033[0m         \033[1;7;36;96m Beef \033[0m         \033[1;7;32;92m {convertedcurrency['SW3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SW3']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW4 \033[0m         \033[1;7;36;96m Cheese \033[0m       \033[1;7;32;92m {convertedcurrency['SW4']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SW4']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW5 \033[0m         \033[1;7;36;96m Salmon \033[0m       \033[1;7;32;92m {convertedcurrency['SW5']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['SW5']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |                   Select a \033[1;34;31mtype\033[0m of \033[4;34;92mWrap\033[0m:                      |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m WP1 \033[0m         \033[1;7;36;96m Grilled \033[0m      \033[1;7;32;92m {convertedcurrency['WP1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['WP1']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m WP2 \033[0m         \033[1;7;36;96m Tuna \033[0m         \033[1;7;32;92m {convertedcurrency['WP2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['WP2']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m WP3 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m {convertedcurrency['WP3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['WP3']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m WP4 \033[0m         \033[1;7;36;96m Spud \033[0m         \033[1;7;32;92m {convertedcurrency['WP4']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['WP4']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |                                                               
                        |                                                               |
                        §===============================================================§
""")

def sandWraps_spec_3GBP():
                                                
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSandwich\033[0m:                    |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in sandwichswraps.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in sandwichswraps.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SW1 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m {convertedcurrency['SW1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SW1']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW2 \033[0m         \033[1;7;36;96m Seafood \033[0m      \033[1;7;32;92m {convertedcurrency['SW2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SW2']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW3 \033[0m         \033[1;7;36;96m Beef \033[0m         \033[1;7;32;92m {convertedcurrency['SW3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SW3']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW4 \033[0m         \033[1;7;36;96m Cheese \033[0m       \033[1;7;32;92m {convertedcurrency['SW4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SW4']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW5 \033[0m         \033[1;7;36;96m Salmon \033[0m       \033[1;7;32;92m {convertedcurrency['SW5']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['SW5']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |                   Select a \033[1;34;31mtype\033[0m of \033[4;34;92mWrap\033[0m:                      |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:         Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m WP1 \033[0m         \033[1;7;36;96m Grilled \033[0m      \033[1;7;32;92m {convertedcurrency['WP1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['WP1']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m WP2 \033[0m         \033[1;7;36;96m Tuna \033[0m         \033[1;7;32;92m {convertedcurrency['WP2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['WP2']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m WP3 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m {convertedcurrency['WP3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['WP3']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m WP4 \033[0m         \033[1;7;36;96m Spud \033[0m         \033[1;7;32;92m {convertedcurrency['WP4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['WP4']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |                                                               
                        |                                                               |
                        §===============================================================§
""")
   
def sandWraps_spec_3AED():
                                                
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSandwich\033[0m:                    |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in sandwichswraps.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in sandwichswraps.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m SW1 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m {convertedcurrency['SW1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SW1']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW2 \033[0m         \033[1;7;36;96m Seafood \033[0m      \033[1;7;32;92m {convertedcurrency['SW2']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SW2']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW3 \033[0m         \033[1;7;36;96m Beef \033[0m         \033[1;7;32;92m {convertedcurrency['SW3']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SW3']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW4 \033[0m         \033[1;7;36;96m Cheese \033[0m       \033[1;7;32;92m {convertedcurrency['SW4']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['SW4']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |     \033[1;7;31;91m SW5 \033[0m         \033[1;7;36;96m Salmon \033[0m       \033[1;7;32;92m {convertedcurrency['SW5']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['SW5']} \033[0m        |
                        |                   \033[1;7;36;96m Sandwich \033[0m                                  |  
                        |                                                               |
                        |                   Select a \033[1;34;31mtype\033[0m of \033[4;34;92mWrap\033[0m:                      |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m WP1 \033[0m         \033[1;7;36;96m Grilled \033[0m      \033[1;7;32;92m {convertedcurrency['WP1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['WP1']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m WP2 \033[0m         \033[1;7;36;96m Tuna \033[0m         \033[1;7;32;92m {convertedcurrency['WP2']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['WP2']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |  
                        |                                                               |
                        |     \033[1;7;31;91m WP3 \033[0m         \033[1;7;36;96m Chicken \033[0m      \033[1;7;32;92m {convertedcurrency['WP3']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['WP3']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |                                                               
                        |                                                               |
                        |     \033[1;7;31;91m WP4 \033[0m         \033[1;7;36;96m Spud \033[0m         \033[1;7;32;92m {convertedcurrency['WP4']:.2f}{symbols['AED']} \033[0m         \033[1;7;31;91m {newstock['WP4']} \033[0m        |
                        |                   \033[1;7;36;96m Wrap \033[0m                                      |                                                               
                        |                                                               |
                        §===============================================================§
""")
 








def fruitCups_spec_4():
                                                        
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:                   |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m FC1 \033[0m         \033[1;7;36;96m Watermelon \033[0m   \033[1;7;32;92m 7.00 \033[0m           \033[1;7;31;91m 3 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC2 \033[0m         \033[1;7;36;96m Pineapple \033[0m    \033[1;7;32;92m 8.00 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC3 \033[0m         \033[1;7;36;96m Orange \033[0m       \033[1;7;32;92m 5.00 \033[0m           \033[1;7;31;91m 8 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC4 \033[0m         \033[1;7;36;96m Kiwi \033[0m         \033[1;7;32;92m 8.00 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC5 \033[0m         \033[1;7;36;96m Mango \033[0m        \033[1;7;32;92m 9.99 \033[0m           \033[1;7;31;91m 4 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC6 \033[0m         \033[1;7;36;96m Pomogranate \033[0m  \033[1;7;32;92m 9.99 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |                                
                        §===============================================================§
""")

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

fruitcups = {
        "FC1": {"price": 7.00, "stock" : 3, "tags": ["Vegan"] },
        "FC2": {"price": 8.00, "stock" : 1, "tags": ["Vegan"] },
        "FC3": {"price": 5.00, "stock" : 8, "tags": ["Vegan"] },
        "FC4": {"price": 8.00, "stock" : 2, "tags": ["Vegan"] },
        "FC5": {"price": 9.99, "stock" : 4, "tags": ["Vegan"] },
        "FC6": {"price": 9.99, "stock" : 1, "tags": ["Vegan"] },
}

def fruitCups_spec_4USD():
                                                        
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:                   |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:            Price:         Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in fruitcups.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in fruitcups.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m FC1 \033[0m         \033[1;7;36;96m Watermelon \033[0m     \033[1;7;32;92m {convertedcurrency['FC1']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['FC1']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC2 \033[0m         \033[1;7;36;96m Pineapple \033[0m      \033[1;7;32;92m {convertedcurrency['FC2']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['FC2']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC3 \033[0m         \033[1;7;36;96m Orange \033[0m         \033[1;7;32;92m {convertedcurrency['FC3']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['FC3']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC4 \033[0m         \033[1;7;36;96m Kiwi \033[0m           \033[1;7;32;92m {convertedcurrency['FC4']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['FC4']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC5 \033[0m         \033[1;7;36;96m Mango \033[0m          \033[1;7;32;92m {convertedcurrency['FC5']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['FC5']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC6 \033[0m         \033[1;7;36;96m Pomogranate \033[0m    \033[1;7;32;92m {convertedcurrency['FC6']:.2f}{symbols['USD']} \033[0m         \033[1;7;31;91m {newstock['FC6']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       | 
                        |                                                               |                                
                        §===============================================================§
""")

def fruitCups_spec_4GBP():
                                                        
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:                   |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:            Price:         Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in fruitcups.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in fruitcups.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m FC1 \033[0m         \033[1;7;36;96m Watermelon \033[0m     \033[1;7;32;92m {convertedcurrency['FC1']:.2f}{symbols['GBP']} \033[0m         \033[1;7;31;91m {newstock['FC1']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC2 \033[0m         \033[1;7;36;96m Pineapple \033[0m      \033[1;7;32;92m {convertedcurrency['FC2']:.2f}{symbols['GBP']} \033[0m         \033[1;7;31;91m {newstock['FC2']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC3 \033[0m         \033[1;7;36;96m Orange \033[0m         \033[1;7;32;92m {convertedcurrency['FC3']:.2f}{symbols['GBP']} \033[0m         \033[1;7;31;91m {newstock['FC3']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC4 \033[0m         \033[1;7;36;96m Kiwi \033[0m           \033[1;7;32;92m {convertedcurrency['FC4']:.2f}{symbols['GBP']} \033[0m         \033[1;7;31;91m {newstock['FC4']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC5 \033[0m         \033[1;7;36;96m Mango \033[0m          \033[1;7;32;92m {convertedcurrency['FC5']:.2f}{symbols['GBP']} \033[0m         \033[1;7;31;91m {newstock['FC5']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC6 \033[0m         \033[1;7;36;96m Pomogranate \033[0m    \033[1;7;32;92m {convertedcurrency['FC6']:.2f}{symbols['GBP']} \033[0m         \033[1;7;31;91m {newstock['FC6']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       | 
                        |                                                               |                                
                        §===============================================================§
""")

def fruitCups_spec_4AED():
                                                        
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:                   |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:            Price:        Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in fruitcups.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in fruitcups.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m FC1 \033[0m         \033[1;7;36;96m Watermelon \033[0m     \033[1;7;32;92m {convertedcurrency['FC1']:.2f}{symbols['AED']} \033[0m      \033[1;7;31;91m {newstock['FC1']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC2 \033[0m         \033[1;7;36;96m Pineapple \033[0m      \033[1;7;32;92m {convertedcurrency['FC2']:.2f}{symbols['AED']} \033[0m      \033[1;7;31;91m {newstock['FC2']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC3 \033[0m         \033[1;7;36;96m Orange \033[0m         \033[1;7;32;92m {convertedcurrency['FC3']:.2f}{symbols['AED']} \033[0m      \033[1;7;31;91m {newstock['FC3']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC4 \033[0m         \033[1;7;36;96m Kiwi \033[0m           \033[1;7;32;92m {convertedcurrency['FC4']:.2f}{symbols['AED']} \033[0m      \033[1;7;31;91m {newstock['FC4']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC5 \033[0m         \033[1;7;36;96m Mango \033[0m          \033[1;7;32;92m {convertedcurrency['FC5']:.2f}{symbols['AED']} \033[0m      \033[1;7;31;91m {newstock['FC5']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       |  
                        |                                                               |
                        |     \033[1;7;31;91m FC6 \033[0m         \033[1;7;36;96m Pomogranate \033[0m    \033[1;7;32;92m {convertedcurrency['FC6']:.2f}{symbols['AED']} \033[0m      \033[1;7;31;91m {newstock['FC6']} \033[0m        |
                        |                   \033[1;7;36;96m Cup \033[0m                                       | 
                        |                                                               |                                
                        §===============================================================§
""")




def driedFruitPackets_spec_5():
                                                                
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:                   |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |
                        |     \033[1;7;31;91m DF1 \033[0m         \033[1;7;36;96m Walnut \033[0m       \033[1;7;32;92m 5.25 \033[0m           \033[1;7;31;91m 5 \033[0m         |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF2 \033[0m         \033[1;7;36;96m Pistachios \033[0m   \033[1;7;32;92m 6.25 \033[0m           \033[1;7;31;91m 2 \033[0m         |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF3 \033[0m         \033[1;7;36;96m Almond \033[0m       \033[1;7;32;92m 5.25 \033[0m           \033[1;7;31;91m 0 \033[0m         |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF4 \033[0m         \033[1;7;36;96m Cashews \033[0m      \033[1;7;32;92m 6.25 \033[0m           \033[1;7;31;91m 1 \033[0m         |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF5 \033[0m         \033[1;7;36;96m Dried \033[0m        \033[1;7;32;92m 8.99 \033[0m           \033[1;7;31;91m 5 \033[0m         |
                        |                   \033[1;7;36;96m Apricots \033[0m                                  |  
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF6 \033[0m         \033[1;7;36;96m Dried \033[0m        \033[1;7;32;92m 8.99 \033[0m           \033[1;7;31;91m 9 \033[0m         |
                        |                   \033[1;7;36;96m Figs \033[0m                                      |  
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |                                
                        §===============================================================§
""")

symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

driedfruitpackets = {
        "DF1": {"price": 5.25, "stock" : 5, "tags": ["Vegan, Sugar Free"] },
        "DF2": {"price": 6.25, "stock" : 2, "tags": ["Vegan, Sugar Free"] },
        "DF3": {"price": 5.25, "stock" : 0, "tags": ["Vegan, Sugar Free"] },
        "DF4": {"price": 6.25, "stock" : 1, "tags": ["Vegan, Sugar Free"] },
        "DF5": {"price": 8.99, "stock" : 5 },
        "DF6": {"price": 8.99, "stock" : 9 },
}

def driedFruitPackets_spec_5USD():
                                                                
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:                   |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in driedfruitpackets.items():
                        convertedcurrency[code] = round(details["price"] * rates["USD"], 2)
        newstock = {}
        for code, details in driedfruitpackets.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m DF1 \033[0m         \033[1;7;36;96m Walnut \033[0m       \033[1;7;32;92m {convertedcurrency['DF1']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['DF1']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF2 \033[0m         \033[1;7;36;96m Pistachios \033[0m   \033[1;7;32;92m {convertedcurrency['DF2']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['DF2']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF3 \033[0m         \033[1;7;36;96m Almond \033[0m       \033[1;7;32;92m {convertedcurrency['DF3']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['DF3']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF4 \033[0m         \033[1;7;36;96m Cashews \033[0m      \033[1;7;32;92m {convertedcurrency['DF4']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['DF4']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF5 \033[0m         \033[1;7;36;96m Dried \033[0m        \033[1;7;32;92m {convertedcurrency['DF5']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['DF5']} \033[0m        |
                        |                   \033[1;7;36;96m Apricots \033[0m                                  |  
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF6 \033[0m         \033[1;7;36;96m Dried \033[0m        \033[1;7;32;92m {convertedcurrency['DF6']:.2f}{symbols['USD']} \033[0m           \033[1;7;31;91m {newstock['DF6']} \033[0m        |
                        |                   \033[1;7;36;96m Figs \033[0m                                      |  
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |                                
                        §===============================================================§
""")

def driedFruitPackets_spec_5GBP():
                                                                
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:                   |
                        |                                                               |
                        |     \033[1;34;97mCode:         Name:          Price:           Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in driedfruitpackets.items():
                        convertedcurrency[code] = round(details["price"] * rates["GBP"], 2)
        newstock = {}
        for code, details in driedfruitpackets.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m DF1 \033[0m         \033[1;7;36;96m Walnut \033[0m       \033[1;7;32;92m {convertedcurrency['DF1']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['DF1']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF2 \033[0m         \033[1;7;36;96m Pistachios \033[0m   \033[1;7;32;92m {convertedcurrency['DF2']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['DF2']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF3 \033[0m         \033[1;7;36;96m Almond \033[0m       \033[1;7;32;92m {convertedcurrency['DF3']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['DF3']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF4 \033[0m         \033[1;7;36;96m Cashews \033[0m      \033[1;7;32;92m {convertedcurrency['DF4']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['DF4']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF5 \033[0m         \033[1;7;36;96m Dried \033[0m        \033[1;7;32;92m {convertedcurrency['DF5']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['DF5']} \033[0m        |
                        |                   \033[1;7;36;96m Apricots \033[0m                                  |  
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF6 \033[0m         \033[1;7;36;96m Dried \033[0m        \033[1;7;32;92m {convertedcurrency['DF6']:.2f}{symbols['GBP']} \033[0m           \033[1;7;31;91m {newstock['DF6']} \033[0m        |
                        |                   \033[1;7;36;96m Figs \033[0m                                      |  
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |                                
                        §===============================================================§
""")

def driedFruitPackets_spec_5AED():
                                                                
        print (("""\n\n\033[1;32;32m
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
                        |                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:                   |
                        |                                                               |
                        |     \033[1;34;97mCode:          Name:          Price:          Stock:\033[0m      |
                        |                                                               |""")
        convertedcurrency = {}
        for code, details in driedfruitpackets.items():
                        convertedcurrency[code] = round(details["price"] * rates["AED"], 2)
        newstock = {}
        for code, details in driedfruitpackets.items():
                newstock[code] = (details["stock"])
        print(f"""                        |     \033[1;7;31;91m DF1 \033[0m         \033[1;7;36;96m Walnut \033[0m       \033[1;7;32;92m {convertedcurrency['DF1']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['DF1']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF2 \033[0m         \033[1;7;36;96m Pistachios \033[0m   \033[1;7;32;92m {convertedcurrency['DF2']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['DF2']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF3 \033[0m         \033[1;7;36;96m Almond \033[0m       \033[1;7;32;92m {convertedcurrency['DF3']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['DF3']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF4 \033[0m         \033[1;7;36;96m Cashews \033[0m      \033[1;7;32;92m {convertedcurrency['DF4']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['DF4']} \033[0m        |
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF5 \033[0m         \033[1;7;36;96m Dried \033[0m        \033[1;7;32;92m {convertedcurrency['DF5']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['DF5']} \033[0m        |
                        |                   \033[1;7;36;96m Apricots \033[0m                                  |  
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |
                        |     \033[1;7;31;91m DF6 \033[0m         \033[1;7;36;96m Dried \033[0m        \033[1;7;32;92m {convertedcurrency['DF6']:.2f}{symbols['AED']} \033[0m        \033[1;7;31;91m {newstock['DF6']} \033[0m        |
                        |                   \033[1;7;36;96m Figs \033[0m                                      |  
                        |                   \033[1;7;36;96m Packet \033[0m                                    |  
                        |                                                               |                                
                        §===============================================================§
""")









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

        selectONE  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectONE}")
        if selectONE == "1" or selectONE.lower() == "snacks":
                snacks_display()
        elif selectONE == "2" or selectONE.lower() == "drinks":
                drinks_display()
        elif selectONE == "3" or selectONE.lower() == "specialties":
                spec_display()
        else: 
                print ("Please ensure to select an option to continue")
                display()



def MainCurrencyDisplay():
        
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
                            |         Please select \033[1;34;31m1\033[0m of the \033[1;34;92m3\033[0m Currencies:          |
                            |                                                       |
                            |                    \033[1;34;92m1.\033[0m \033[7;34;94m Dollars (USD) \033[0m                 |
                            |                                                       |
                            |                    \033[1;34;92m2.\033[0m \033[7;34;94m Pounds (GBP) \033[0m                  |
                            |                                                       |
                            |                    \033[1;34;92m3.\033[0m \033[7;34;94m Dirhams (AED) \033[0m                 |
                            |                                                       |
                            §=======================================================§
""")
        selectcurrency  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectcurrency}")
        if selectcurrency == "1" or selectcurrency.lower() in "dollars (usd)":
                displayUSD()
        elif selectcurrency == "2" or selectcurrency.lower() in "pounds (gbp)":
                displayGBP()
        elif selectcurrency == "3" or selectcurrency.lower() in "dirhams (aed)":
                displayAED()
        else: 
                print ("Please ensure to select an option to continue")
                MainCurrencyDisplay()



def displayUSD():
        
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

        selectONE  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectONE}")
        if selectONE == "1" or selectONE.lower() in "snacks":
                snacks_displayUSD()
        elif selectONE == "2" or selectONE.lower() in "drinks":
                drinks_displayUSD()
        elif selectONE == "3" or selectONE.lower() in "specialties":
                spec_displayUSD()
        else: 
                print ("Please ensure to select an option to continue")
                displayUSD()

def displayGBP():
        
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

        selectONE  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectONE}")
        if selectONE == "1" or selectONE.lower() in "snacks":
                snacks_displayGBP()
        elif selectONE == "2" or selectONE.lower() in "drinks":
                drinks_displayGBP()
        elif selectONE == "3" or selectONE.lower() in "specialties":
                spec_displayGBP()
        else: 
                print ("Please ensure to select an option to continue")
                displayGBP()

def displayAED():
        
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

        selectONE  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectONE}")
        if selectONE == "1" or selectONE.lower() in "snacks":
                snacks_displayAED()
        elif selectONE == "2" or selectONE.lower() in "drinks":
                drinks_displayAED()
        elif selectONE == "3" or selectONE.lower() in "specialties":
                spec_displayAED()
        else: 
                print ("Please ensure to select an option to continue")
                displayAED()



def snacks_displayUSD():

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
        print ("\n" * 5)
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
        print ("\n" * 4)
        
        selectTWO = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTWO}")

        if selectTWO == "1" or selectTWO.lower() in "chocolate bars":
                chocolateBar_snacks_1USD()
        elif selectTWO == "2" or selectTWO.lower() in "chips":
                chips_snacks_2USD()
        elif selectTWO == "3" or selectTWO.lower() in "crackers & cookies" "crackers and cookies":
                crackersCookies_snacks_3USD()
        elif selectTWO == "4" or selectTWO.lower() in "candy":
                candy_snacks_4USD()
        elif selectTWO == "0" or selectTWO.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                snacks_displayUSD()

def snacks_displayGBP():

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
        print ("\n" * 5)
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
        print ("\n" * 4)
        
        selectTWO = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTWO}")

        if selectTWO == "1" or selectTWO.lower() in "chocolate bars":
                chocolateBar_snacks_1GBP()
        elif selectTWO == "2" or selectTWO.lower() in "chips":
                chips_snacks_2GBP()
        elif selectTWO == "3" or selectTWO.lower() in "crackers & cookies" "crackers and cookies":
                crackersCookies_snacks_3GBP()
        elif selectTWO == "4" or selectTWO.lower() in "candy":
                candy_snacks_4GBP()
        elif selectTWO == "0" or selectTWO.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                snacks_displayGBP()

def snacks_displayAED():

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
        print ("\n" * 5)
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
        print ("\n" * 4)
        
        selectTWO = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTWO}")

        if selectTWO == "1" or selectTWO.lower() in "chocolate bars":
                chocolateBar_snacks_1AED()
        elif selectTWO == "2" or selectTWO.lower() in "chips":
                chips_snacks_2AED()
        elif selectTWO == "3" or selectTWO.lower() in "crackers & cookies" "crackers and cookies":
                crackersCookies_snacks_3AED()
        elif selectTWO == "4" or selectTWO.lower() in "candy":
                candy_snacks_4AED()
        elif selectTWO == "0" or selectTWO.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                snacks_displayAED()



def drinks_displayUSD():
        
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
        print ("\n" * 5)
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
        print ("\n" * 4)
        
        selectTHREE = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTHREE}")

        if selectTHREE == "1" or selectTHREE.lower() in "water":
                water_drinks_1USD()
        elif selectTHREE == "2" or selectTHREE.lower() in "energy drinks":
                energyDrink_drinks_2USD()
        elif selectTHREE == "3" or selectTHREE.lower() in "soda & soft drinks" "soda and soft drinks":
                sodaSoftDrinks_drinks_3USD()
        elif selectTHREE == "4" or selectTHREE.lower() in "sports hydration":
                sportsHyd_drinks_4USD()
        elif selectTHREE == "5" or selectTHREE.lower() in "ice tea":
                iceTea_drinks_5USD()
        elif selectTHREE == "6" or selectTHREE.lower() in "fruit juice":
                fruitJuice_drinks_6USD()
        elif selectTHREE == "7" or selectTHREE.lower() in "coffee":
                coffee_drinks_7USD()
        elif selectTHREE == "0" or selectTHREE.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                drinks_display()

def drinks_displayGBP():
        
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
        print ("\n" * 5)
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
        print ("\n" * 4)
        
        selectTHREE = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTHREE}")

        if selectTHREE == "1" or selectTHREE.lower() in "water":
                water_drinks_1GBP()
        elif selectTHREE == "2" or selectTHREE.lower() in "energy drinks":
                energyDrink_drinks_2GBP()
        elif selectTHREE == "3" or selectTHREE.lower() in "soda & soft drinks" "soda and soft drinks":
                sodaSoftDrinks_drinks_3GBP()
        elif selectTHREE == "4" or selectTHREE.lower() in "sports hydration":
                sportsHyd_drinks_4GBP()
        elif selectTHREE == "5" or selectTHREE.lower() in "ice tea":
                iceTea_drinks_5GBP()
        elif selectTHREE == "6" or selectTHREE.lower() in "fruit juice":
                fruitJuice_drinks_6GBP()
        elif selectTHREE == "7" or selectTHREE.lower() in "coffee":
                coffee_drinks_7GBP()
        elif selectTHREE == "0" or selectTHREE.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                drinks_displayGBP()

def drinks_displayAED():
        
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
        print ("\n" * 5)
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
        print ("\n" * 4)
        
        selectTHREE = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTHREE}")

        if selectTHREE == "1" or selectTHREE.lower() in "water":
                water_drinks_1AED()
        elif selectTHREE == "2" or selectTHREE.lower() in "energy drinks":
                energyDrink_drinks_2AED()
        elif selectTHREE == "3" or selectTHREE.lower() in "soda & soft drinks" "soda and soft drinks":
                sodaSoftDrinks_drinks_3AED()
        elif selectTHREE == "4" or selectTHREE.lower() in "sports hydration":
                sportsHyd_drinks_4AED()
        elif selectTHREE == "5" or selectTHREE.lower() in "ice tea":
                iceTea_drinks_5AED()
        elif selectTHREE == "6" or selectTHREE.lower() in "fruit juice":
                fruitJuice_drinks_6AED()
        elif selectTHREE == "7" or selectTHREE.lower() in "coffee":
                coffee_drinks_7AED()
        elif selectTHREE == "0" or selectTHREE.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                drinks_displayAED()



def spec_displayUSD():
        
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
        print ("\n" * 4)
        
        selectTHREE = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTHREE}")

        if selectTHREE == "1" or selectTHREE.lower() in "healthy options":
                healthyOptions_spec_1USD()
        elif selectTHREE == "2" or selectTHREE.lower() in "instant noodles":
                instantNoodles_spec_2USD()
        elif selectTHREE == "3" or selectTHREE.lower() in "sandwiches and wraps":
                sandWraps_spec_3USD()
        elif selectTHREE == "4" or selectTHREE.lower() in "fruit cups":
                fruitCups_spec_4USD()
        elif selectTHREE == "5" or selectTHREE.lower() in "dried fruit packets":
                driedFruitPackets_spec_5USD()
        elif selectTHREE == "0" or selectTHREE.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                spec_displayUSD()

def spec_displayGBP():
        
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
        print ("\n" * 4)
        
        selectTHREE = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTHREE}")

        if selectTHREE == "1" or selectTHREE.lower() in "healthy options":
                healthyOptions_spec_1GBP()
        elif selectTHREE == "2" or selectTHREE.lower() in "instant noodles":
                instantNoodles_spec_2GBP()
        elif selectTHREE == "3" or selectTHREE.lower() in "sandwiches and wraps":
                sandWraps_spec_3GBP()
        elif selectTHREE == "4" or selectTHREE.lower() in "fruit cups":
                fruitCups_spec_4GBP()
        elif selectTHREE == "5" or selectTHREE.lower() in "dried fruit packets":
                driedFruitPackets_spec_5GBP()
        elif selectTHREE == "0" or selectTHREE.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                spec_displayGBP()

def spec_displayAED():
        
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
        print ("\n" * 4)
        
        selectTHREE = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectTHREE}")

        if selectTHREE == "1" or selectTHREE.lower() in "healthy options":
                healthyOptions_spec_1AED()
        elif selectTHREE == "2" or selectTHREE.lower() in "instant noodles":
                instantNoodles_spec_2AED()
        elif selectTHREE == "3" or selectTHREE.lower() in "sandwiches and wraps":
                sandWraps_spec_3AED()
        elif selectTHREE == "4" or selectTHREE.lower() in "fruit cups":
                fruitCups_spec_4AED()
        elif selectTHREE == "5" or selectTHREE.lower() in "dried fruit packets":
                driedFruitPackets_spec_5AED()
        elif selectTHREE == "0" or selectTHREE.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                spec_displayAED()















MainCurrencyDisplay()














