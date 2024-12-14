
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

items = {

    "Snacks": {             # Start of the Snacks category 

        "Chocolate Bars": {
            1: {"name" : "Snickers", "price": 3.50, "stock" : 7  },
            2: {"name" : "KitKat", "price": 2.50, "stock" : 4 },
            3: {"name" : "Hershey's", "price": 2.00, "stock" : 10 },
            4: {"name" : "Milky Way", "price": 1.99, "stock" : 9 },
            },

        "Chips": {
            5: {"name" : "Lay's (Classic)", "price": 1.00, "stock" : 5  },
            6: {"name" : "Lay's (BBQ)", "price": 1.00, "stock" : 1  },
            7: {"name" : "Lay's (Sour Cream & Onion)", "price": 2.00, "stock" : 3  },
            8: {"name" : "Lay's (Salt & Vinegar)", "price": 2.00, "stock" : 7  },
            9: {"name" : "Pringles (Classic)", "price": 2.00, "stock" : 5  },
            10: {"name" : "Pringles (Hot & BBQ)", "price": 2.00, "stock" : 4  },
            11: {"name" : "Pringles (Cheddar Jalepeno)", "price": 3.00, "stock" : 10  },
            12: {"name" : "Cheetos (Classic)", "price": 1.00, "stock" : 15 },
            13: {"name" : "Cheetos (Flamin' Hot)", "price": 1.00, "stock" : 1 },
            14: {"name" : "Ruffles (Originals)", "price": 3.00, "stock" : 1 },
            15: {"name" : "Chips Omani", "price": 5.00, "stock" : 13 },
        },

        "Crackers & Cookies": {
            16: {"name" : "Ritz", "price": 1.50, "stock" : 3 },
            17: {"name" : "Oreos", "price": 2.50, "stock" : 5 },
            18: {"name" : "Cheez-Its", "price": 1.00, "stock" : 1 },
            19: {"name" : "Nutter Butterz", "price": 3.50, "stock" : 9 },
        },

        "Candy": {
            20: {"name" : "M&Ms", "price": 4.50, "stock" : 15 },
            21: {"name" : "M&Ms (Peanuts)", "price": 5.00, "stock" : 1 },
            22: {"name" : "Skittles", "price": 4.50, "stock" : 0 },
            23: {"name" : "Skittles (Sour)", "price": 5.50, "stock" : 2 },
            24: {"name" : "Juicy Fruitz", "price": 0.50, "stock" : 30 },
            25: {"name" : "Starbursts", "price": 2.75, "stock" : 8 },
        },
    },      # End of the Snacks category 




    "Drinks": {     # Start of the Drinks category 

        "water": {
            26: {"name" : "Water", "price": 0.99, "stock" : 8 },
            27: {"name" : "Water (Sparkling)", "price": 3.99, "stock" : 5 },
            28: {"name" : "Vitamin Water", "price": 4.25, "stock" : 1 },
        },

        "Energy Drinks": {
            29: {"name" : "Red bull", "price": 7.25, "stock" : 0 },
            30: {"name" : "Red bull (Cherry)", "price": 7.99, "stock" : 1 },
            31: {"name" : "MONSTER ENERGY", "price": 9.65, "stock" : 1 },
        },

        "Soda & Soft Drinks": {
            32: {"name" : "Coke", "price": 2.00, "stock" : 0 },
            33: {"name" : "Pepsi", "price": 2.00, "stock" : 2 },
            34: {"name" : "Spite", "price": 2.00, "stock" : 3 },
            35: {"name" : "Dr. Pepper", "price": 4.00, "stock" : 1 },
            36: {"name" : "Mountain Dew", "price": 2.00, "stock" : 6 },
            37: {"name" : "Fanta", "price": 2.00, "stock" : 4 },
            38: {"name" : "Diet Coke", "price": 3.00, "stock" : 1 },
            39: {"name" : "Diet Pepsi", "price": 3.00, "stock" : 5 },
            40: {"name" : "Diet Dew", "price": 3.00, "stock" : 3 },
        },

        "Sports Hydration": {
            41: {"name" : "Gatorade", "price": 5.05, "stock" : 5 },
        },

        "Ice Tea": {
            42: {"name" : "Gold Peak Tea", "price": 3.45, "stock" : 2 },
            43: {"name" : "Lipton Ice Tea (Peach)", "price": 3.75, "stock" : 5 },
            44: {"name" : "Lipton Ice Tea (Lemon)", "price": 3.75, "stock" : 0 },
            45: {"name" : "Lipton Ice Tea (Strawberry Blast)", "price": 2.75, "stock" : 0 },
        },

        "Fruit Juice": {
            46: {"name" : "Tropicana Mango Juice", "price": 2.00, "stock" : 10 },
            47: {"name" : "Newman's Orange Juice", "price": 2.00, "stock" : 1 },
            48: {"name" : "Minute Made Peach", "price": 4.00, "stock" : 0 },
            49: {"name" : "Simply Lemonade", "price": 6.00, "stock" : 1 },
        },

        "coffee": {
            50: {"name" : "Coffee (Hot)", "price": 4.00, "stock" : 0 },
            51: {"name" : "Coffee (Iced)", "price": 6.00, "stock" : 1 },
        },
    },          # End of the Drinks category 




    "Specialties": {   # Start of the Specialties category 

        "Healthy Options": {

            "Energy & Granola Bars": {
                52: {"name" : "Clif Bar", "price": 1.00, "stock" : 4 },
                53: {"name" : "Nature Valley", "price": 3.99, "stock" : 2 },
                54: {"name" : "Kind Granola Bar", "price": 3.00, "stock" : 0 },
                55: {"name" : "Lara Bar", "price": 2.00, "stock" : 1 },
            },

            "Jerky & Meat Snacks": {
                56: {"name" : "Slim Jim", "price": 6.00, "stock" : 7 },
                57: {"name" : "Jack Link's", "price": 6.59, "stock" : 3 },
                58: {"name" : "Perky Jerky", "price": 7.99, "stock" : 2 },
                59: {"name" : "Oberto", "price": 11.75, "stock" : 1 },
            },
        },

        "Instant Noodles": {
            60: {"name" : "Chicken Cup Noodles", "price": 4.00, "stock" : 4 },
            61: {"name" : "Beef Cup Noodles", "price": 4.00, "stock" : 2 },
            62: {"name" : "Curry Cup Noodles", "price": 4.75, "stock" : 2 },
            63: {"name" : "Chili Cup Noodles", "price": 4.00, "stock" : 0 },
            64: {"name" : "Mushroom Cup Noodles", "price": 5.29, "stock" : 6 },
            65: {"name" : "Shrimp Cup Noodles", "price": 4.00, "stock" : 1 },
        },

        "Sandwiches and Wraps": {

            "Sandwiches": {
                66: {"name" : "Chicken Sandwich", "price": 3.75, "stock" : 0 },
                67: {"name" : "Seafood Sandwich", "price": 2.75, "stock" : 4 },
                68: {"name" : "Beef Sandwich", "price": 4.99, "stock" : 2 },
                69: {"name" : "Cheese Sandwich", "price": 1.99, "stock" : 4 },
                70: {"name" : "Salmon Sandwich", "price": 6.75, "stock" : 1 },
            },

            "Wraps": {
                71: {"name" : "Grilled Wrap", "price": 3.00, "stock" : 1 },
                72: {"name" : "Tuna Wrap", "price": 1.00, "stock" : 8 },
                73: {"name" : "Chicken Wrap", "price": 5.00, "stock" : 3 },
                74: {"name" : "Spud Wrap", "price": 2.30, "stock" : 2 },
            },
        },

        "Fruit Cups": {
            74: {"name" : "Watermelon Cup", "price": 7.00, "stock" : 3 },
            75: {"name" : "Pineapple Cup", "price": 8.00, "stock" : 1 },
            76: {"name" : "Orange Cup", "price": 5.00, "stock" : 8 },
            77: {"name" : "Kiwi Cup", "price": 8.00, "stock" : 2 },
            78: {"name" : "Mango Cup", "price": 9.99, "stock" : 4 },
            79: {"name" : "Pomogranate Cup", "price": 9.99, "stock" : 1 },
            },

        "Dried Fruit Packets": {
            80: {"name" : "Walnut Packet", "price": 5.25, "stock" : 5 },
            81: {"name" : "Pistachios Packet", "price": 6.25, "stock" : 2 },
            82: {"name" : "Almond Packet", "price": 5.25, "stock" : 0 },
            83: {"name" : "Cashews Packet", "price": 6.25, "stock" : 1 },
            84: {"name" : "Dried Apricots Packet", "price": 8.99, "stock" : 5 },
            85: {"name" : "Dried Figs Packet", "price": 8.99, "stock" : 9 },
            },
    },          # End of the Specialties category 

    }       # End of the Specialties category 
    
