
# Vending Machine - Aneeka Memon


# The title for the vending machine 

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
            7: {"code" : "C3" , "name" : "Lay's (Sour Cream & Onion)", "price": 2.00, "stock" : 3  },
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
            26: {"code" : "W1" , "name" : "Water", "price": 0.99, "stock" : 8, "tags": ["Gluten Free, Sugar Free"]},
            27: {"code" : "W2" , "name" : "Water (Sparkling)", "price": 3.99, "stock" : 5, "tags": ["Gluten Free"] },
            28: {"code" : "W3" , "name" : "Vitamin Water", "price": 4.25, "stock" : 1, "tags": ["Gluten Free, Sugar Free"] },
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
    
