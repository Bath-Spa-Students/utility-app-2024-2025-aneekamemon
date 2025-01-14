
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








def chocolateBar_snacks_1demo():

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

codes = {
        "USD",
        "AED",
        "GBP"
}

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

CurrenciesSnacks = {
       
       "USD" : { "code" : "USD" , "symbol" : "$", "rate" : 1 },
       "GBP" : { "code" : "GBP" , "symbol" : "£", "rate" : 0.8 },
       "AED" : { "code" : "AED" , "symbol" : "د.إ", "rate" : 3.67}
}




ChocolateBars = {
        "SC1": {"name" : "Snickers","price": 2.30, "stock" : 7 },
        "SC2": {"name" : "KitKat","price": 2.50, "stock" : 4 },
        "SC3": {"name" : "Hershey's", "price": 2.00, "stock" : 1 },
        "SC4": {"name" : "Milky Way","price": 1.99, "stock" : 9 },
}

Chips = {
            "C1": { "name" : "Lay's (Classic)", "price": 1.00, "stock" : 5, "tags": ["Gluten Free"] },
            "C2": { "name" : "Lay's (BBQ)", "price": 1.00, "stock" : 1  },
            "C3": { "name" : "Lay's (Sour Cream)", "price": 2.00, "stock" : 3  },
            "C4": { "name" : "Lay's (Salt & Vinegar)", "price": 2.00, "stock" : 7, "tags": ["Gluten Free"] },
            "C5": { "name" : "Pringles (Classic)", "price": 2.00, "stock" : 5  },
            "C6": { "name" : "Pringles (Hot & BBQ)", "price": 2.00, "stock" : 4 },
            "C7": { "name" : "Pringles (Cheddar Jalepeno)", "price": 1.50, "stock" : 1  },
            "C8": { "name" : "Cheetos (Classic)", "price": 1.00, "stock" : 5 },
            "C9": { "name" : "Cheetos (Flamin' Hot)", "price": 1.00, "stock" : 1 },
            "C10": { "name" : "Ruffles (Originals)", "price": 1.25, "stock" : 1, "tags": ["Vegan"]},
            "C11": { "name" : "Chips Omani", "price": 0.50, "stock" : 3, "tags": ["Gluten Free, Diabetes Friendly"] },
}

CrackersandCookies = {
        "CC1": { "name" : "Ritz", "price": 1.50, "stock" : 3 },
        "CC2": { "name" : "Oreos", "price": 2.50, "stock" : 5 },
        "CC3": { "name" : "Cheez-Its", "price": 1.00, "stock" : 1 },
        "CC4": { "name" : "Nutter Butterz", "price": 2.45, "stock" : 9 },
}

Candy = {
        "CA1": {"name" : "M&Ms","price": 4.50, "stock" : 5 },
        "CA2": {"name" : "M&Ms (Peanuts)", "price": 5.00, "stock" : 1 },
        "CA3": {"name" : "Skittles", "price": 4.50, "stock" : 0 },
        "CA4": {"name" : "Skittles (Sour)", "price": 5.50, "stock" : 2 },
        "CA5": {"name" : "Juicy Fruitz", "price": 4.66, "stock" : 3 },
}

water = {
        "W1": { "name" : "Water", "price": 0.99, "stock" : 0, "tags": ["Gluten Free, Sugar Free"]},
        "W3": { "name" : "Water (Sparkling)", "price": 2.99, "stock" : 5, "tags": ["Gluten Free"] },
        "W2": { "name" : "Vitamin Water", "price": 4.25, "stock" : 1, "tags": ["Gluten Free, Sugar Free"] },
}

EnergyDrinks = {
        "EE1": { "name" : "Red bull", "price": 7.25, "stock" : 0, "tags": ["Gluten Free"] },
        "EE2": { "name" : "Red bull (Cherry)", "price": 7.99, "stock" : 1, "tags": ["Gluten Free"] },
        "EE3": { "name" : "MONSTER ENERGY", "price": 9.65, "stock" : 1 },
}

SodaSoftDrinks = {
        "SS1": { "name" : "Coke", "price": 2.00, "stock" : 0 },
        "SS2": { "name" : "Pepsi", "price": 2.00, "stock" : 2 },
        "SS3": { "name" : "Spite", "price": 2.00, "stock" : 3, "tags": ["Gluten Free"] },
        "SS4": { "name" : "Dr. Pepper", "price": 2.25, "stock" : 1, "tags": ["Gluten Free"] },
        "SS5": { "name" : "Mountain Dew", "price": 2.00, "stock" : 6 },
        "SS6": { "name" : "Fanta", "price": 2.00, "stock" : 4 },
        "SS7": { "name" : "Diet Coke", "price": 2.70, "stock" : 1, "tags": ["Sugar Free"] },
        "SS8": { "name" : "Diet Pepsi", "price": 2.70, "stock" : 5, "tags": ["Sugar Free"]  },
        "SS9": { "name" : "Diet Dew", "price": 2.70, "stock" : 3, "tags": ["Sugar Free"]  },
}

sportsdrinks = {
        "H1" : { "name" : "Gatorade", "price": 5.05, "stock" : 5 },
}

icetea = {
        "T1": { "name" : "Gold Peak Tea", "price": 3.45, "stock" : 2, "tags": ["Sugar Free"]  },
        "T2": { "name" : "Lipton Ice Tea (Peach)", "price": 3.75, "stock" : 5 },
        "T3": { "name" : "Lipton Ice Tea (Lemon)", "price": 3.75, "stock" : 0 },
        "T4": { "name" : "Lipton Ice Tea (Strawberry)", "price": 2.75, "stock" : 0 },
}

fruitjuice = {
        "F1": { "name" : "Tropicana Mango Juice", "price": 3.90, "stock" : 3 },
        "F2": { "name" : "Newman's Orange Juice", "price": 3.35, "stock" : 1 },
        "F3": { "name" : "Minute Made Peach", "price": 4.00, "stock" : 0 },
        "F4": { "name" : "Simply Lemonade", "price": 6.00, "stock" : 1, "tags": ["Sugar Free"]  },
}   

coffee = {
        "CO1": { "name" : "Coffee (Hot)", "price": 4.00, "stock" : 0, "tags": ["Sugar Free"]  },
        "CO2": { "name" : "Coffee (Iced)", "price": 6.00, "stock" : 1, "tags": ["Sugar Free"]  },
}

healthyoptions = {
        "EG1": { "name" : "Clif Bar", "price": 4.00, "stock" : 4 },
        "EG2": { "name" : "Nature Valley", "price": 2.99, "stock" : 2, "tags": ["Vegan"] },
        "EG3": { "name" : "Granola Bar", "price": 4.00, "stock" : 0 },
        "EG4": { "name" : "Lara Bar", "price": 5.65, "stock" : 1, "tags": ["Gluten Free"] },
        "JM1": { "name" : "Slim Jim", "price": 6.00, "stock" : 7, "tags": ["Gluten Free"] },
        "JM2": { "name" : "Jack Link's", "price": 6.59, "stock" : 0, "tags": ["Gluten Free"] },
        "JM3": { "name" : "Perky Jerky", "price": 7.99, "stock" : 2, "tags": ["Gluten Free"] },
        "JM4": { "name" : "Oberto", "price": 11.75, "stock" : 1, "tags": ["Vegan, Gluten Free"] },
}

instantnoodles = {
        "IN1": { "name" : "Chicken Cup Noodles", "price": 4.00, "stock" : 4, "tags": ["Gluten Free"] },
        "IN2": { "name" : "Beef Cup Noodles", "price": 4.00, "stock" : 2, "tags": ["Gluten Free"] },
        "IN3": { "name" : "Curry Cup Noodles", "price": 4.75, "stock" : 2 },
        "IN4": { "name" : "Chili Cup Noodles", "price": 4.00, "stock" : 0 },
        "IN5": { "name" : "Mushroom Cup Noodles", "price": 5.29, "stock" : 6, "tags": ["Vegan"] },
        "IN6": { "name" : "Shrimp Cup Noodles", "price": 4.00, "stock" : 1, "tags": ["Gluten Free"] },
}

sandwichswraps = {
        "SW1": { "name" : "Chicken Sandwich", "price": 3.75, "stock" : 0, "tags": ["Gluten Free"] },
        "SW2": { "name" : "Seafood Sandwich", "price": 2.75, "stock" : 4, "tags": ["Gluten Free"] },
        "SW3": { "name" : "Beef Sandwich", "price": 4.99, "stock" : 2, "tags": ["Gluten Free"] },
        "SW4": { "name" : "Cheese Sandwich", "price": 6.99, "stock" : 4 },
        "SW5": { "name" : "Salmon Sandwich", "price": 6.75, "stock" : 1, "tags": ["Gluten Free"] },
        "WP1": { "name" : "Grilled Wrap", "price": 3.00, "stock" : 1, "tags": ["Vegan"] },
        "WP2": { "name" : "Tuna Wrap", "price": 9.00, "stock" : 8, "tags": ["Gluten Free"] },
        "WP3": { "name" : "Chicken Wrap", "price": 5.00, "stock" : 3, "tags": ["Gluten Free"] },
        "WP4": { "name" : "Spud Wrap", "price": 12.30, "stock" : 2 },
}

fruitcups = {
        "FC1": { "name" : "Watermelon Cup", "price": 7.00, "stock" : 3, "tags": ["Vegan"] },
        "FC2": { "name" : "Pineapple Cup", "price": 8.00, "stock" : 1, "tags": ["Vegan"] },
        "FC3": { "name" : "Orange Cup", "price": 5.00, "stock" : 8, "tags": ["Vegan"] },
        "FC4": { "name" : "Kiwi Cup", "price": 8.00, "stock" : 2, "tags": ["Vegan"] },
        "FC5": { "name" : "Mango Cup", "price": 9.99, "stock" : 4, "tags": ["Vegan"] },
        "FC6": { "name" : "Pomogranate Cup", "price": 9.99, "stock" : 1, "tags": ["Vegan"] },
}

driedfruitpackets = {
        "DF1": { "name" : "Walnut Packet", "price": 5.25, "stock" : 5, "tags": ["Vegan, Sugar Free"] },
        "DF2": { "name" : "Pistachios Packet", "price": 6.25, "stock" : 2, "tags": ["Vegan, Sugar Free"] },
        "DF3": { "name" : "Almond Packet", "price": 5.25, "stock" : 0, "tags": ["Vegan, Sugar Free"] },
        "DF4": { "name" : "Cashews Packet", "price": 6.25, "stock" : 1, "tags": ["Vegan, Sugar Free"] },
        "DF5": { "name" : "Dried Apricots Packet", "price": 8.99, "stock" : 5 },
        "DF6": { "name" : "Dried Figs Packet", "price": 8.99, "stock" : 9 },
}




cart = {}

codewidth = 3
namewidth = 27
pricew = 4
stockw = 3
borderwidth = 15


Selected_Currency_Snacks = None


def chocolateBar_snacks_1(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoRed()
        DesignTOP()
                         
        print("""                                         Select a \033[1;34;31mtype\033[0m of \033[4;34;92mChocolate Bar\033[0m:
                                
                                   \033[1;34;97mCode:           Name:         Price:          Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in ChocolateBars.items()}
        Nstock = {code: details["stock"] for code, details in ChocolateBars.items()}

        for code in ChocolateBars.keys():
             print (f"""                                   \033[1;7;31;91m {code:>3} \033[0m        \033[1;7;36;96m {ChocolateBars[code]['name']:>9} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>4} \033[0m        \033[1;7;31;91m {Nstock [code]:>2}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in ChocolateBars:
                item = ChocolateBars[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def chips_snacks_2(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoRed()
        DesignTOP()
        print("""                                              Select a \033[1;34;31mtype\033[0m of \033[4;34;92mChip\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in Chips.items()}
        Nstock = {code: details["stock"] for code, details in Chips.items()}

        for code in Chips.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {Chips[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m            \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in Chips:
                item = Chips[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def crackersCookies_snacks_3(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoRed()
        DesignTOP()
                         
        print("""                                         Select a \033[1;34;31mtype\033[0m of \033[4;34;92mCracker or cookie\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in CrackersandCookies.items()}
        Nstock = {code: details["stock"] for code, details in CrackersandCookies.items()}

        for code in CrackersandCookies.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {CrackersandCookies[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m            \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in CrackersandCookies:
                item = CrackersandCookies[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def candy_snacks_4(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoRed()
        DesignTOP()                         
        print("""                                              Select a \033[1;34;31mtype\033[0m of \033[4;34;92mCandy\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in Candy.items()}
        Nstock = {code: details["stock"] for code, details in Candy.items()}

        for code in Candy.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {Candy[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m            \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in Candy:
                item = Candy[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")
 

def water_drinks_1(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoBlue()
        DesignTOP()            
        print("""                                              Select a \033[1;34;31mtype\033[0m of \033[4;34;92mWater\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in water.items()}
        Nstock = {code: details["stock"] for code, details in water.items()}

        for code in water.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {water[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m            \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in water:
                item = water[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def EnergyDrink_drinks_2(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoBlue()
        DesignTOP()                
        print("""                                             Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy Drink\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in EnergyDrinks.items()}
        Nstock = {code: details["stock"] for code, details in EnergyDrinks.items()}

        for code in EnergyDrinks.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {EnergyDrinks[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in EnergyDrinks:
                item = EnergyDrinks[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def SodaSoftDrinks_drinks_3(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoBlue()
        DesignTOP()                         
        print("""                                         Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSoda or Soft Drink\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in SodaSoftDrinks.items()}
        Nstock = {code: details["stock"] for code, details in SodaSoftDrinks.items()}

        for code in SodaSoftDrinks.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {SodaSoftDrinks[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m            \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in SodaSoftDrinks:
                item = SodaSoftDrinks[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def SportsHyd_drinks_4(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoBlue()
        DesignTOP()                         
        print("""                                           Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSports Drink\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in sportsdrinks.items()}
        Nstock = {code: details["stock"] for code, details in sportsdrinks.items()}

        for code in sportsdrinks.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {sportsdrinks[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in sportsdrinks:
                item = sportsdrinks[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def IceTea_drinks_5(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoBlue()
        DesignTOP()                
        print("""                                            Select a \033[1;34;31mtype\033[0m of \033[4;34;92mIce Tea\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in icetea.items()}
        Nstock = {code: details["stock"] for code, details in icetea.items()}

        for code in icetea.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {icetea[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in icetea:
                item = icetea[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def FruitJuice_drinks_6(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoBlue()
        DesignTOP()
        print("""                                           Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Juice\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in fruitjuice.items()}
        Nstock = {code: details["stock"] for code, details in fruitjuice.items()}

        for code in fruitjuice.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {fruitjuice[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in fruitjuice:
                item = fruitjuice[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def Coffee_drinks_7(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoBlue()
        DesignTOP()             
        print("""                                            Select a \033[1;34;31mtype\033[0m of \033[4;34;92mCoffee\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in coffee.items()}
        Nstock = {code: details["stock"] for code, details in coffee.items()}

        for code in coffee.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {coffee[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()
        
        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in coffee:
                item = coffee[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def HealthyOptions_spec_1(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoGreen()
        DesignTOP()                   
        print("""                                    Select a \033[1;34;31mtype\033[0m of \033[4;34;92mEnergy and/or Granola Bar\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in healthyoptions.items()}
        Nstock = {code: details["stock"] for code, details in healthyoptions.items()}

        for code in healthyoptions.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {healthyoptions[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m            \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in healthyoptions:
                item = healthyoptions[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def InstantNoodles_spec_2(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoGreen()
        DesignTOP()                 
        print("""                                         Select a \033[1;34;31mtype\033[0m of \033[4;34;92mInstant Noodle\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in instantnoodles.items()}
        Nstock = {code: details["stock"] for code, details in instantnoodles.items()}

        for code in instantnoodles.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {instantnoodles[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in instantnoodles:
                item = instantnoodles[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def SandWraps_spec_3(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoGreen()
        DesignTOP()
        print("""                                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSandwich and/or Wrap\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in sandwichswraps.items()}
        Nstock = {code: details["stock"] for code, details in sandwichswraps.items()}

        for code in sandwichswraps.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {sandwichswraps[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in sandwichswraps:
                item = sandwichswraps[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def FruitCups_spec_4(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoGreen()
        DesignTOP()
        print("""                                                Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in fruitcups.items()}
        Nstock = {code: details["stock"] for code, details in fruitcups.items()}

        for code in fruitcups.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {fruitcups[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in fruitcups:
                item = fruitcups[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def DriedFruitPackets_spec_5(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoGreen()
        DesignTOP()
        print("""                                 Select a \033[1;34;31mtype\033[0m of \033[4;34;92mDried Fruit Packet\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in driedfruitpackets.items()}
        Nstock = {code: details["stock"] for code, details in driedfruitpackets.items()}

        for code in driedfruitpackets.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {driedfruitpackets[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD()
                elif CurrencyCode == "GBP":
                        displayGBP()
                elif CurrencyCode == "AED":
                        displayAED()
                break
        elif userchoice == "CART":
                viewcart()
                break
        elif userchoice in driedfruitpackets:
                item = driedfruitpackets[userchoice]
                amount = int(input(f"\n\n\033[1;7;36;96mHow many {item['name']} would you like to add?\033[0m "))
                if amount <= item["stock"]:
                        if userchoice in cart:
                                cart[userchoice]["amount"] += amount
                        else: 
                                cart[userchoice] = {
                                        "name": item["name"],
                                        "price": item["price"],
                                        "amount": amount,
                                }
                        item["stock"] -= amount
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} has been added to the cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")






# The logo design in different colors for different front variations

def TheCornerLogoGreen():
               print (("""\033[1;32;32m
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

def TheCornerLogoRed():
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

def TheCornerLogoBlue():
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

def TheCornerLogoGrey():
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


# The front page design for the Subcategories (Snacks, Drinks, and Specialities)

def Subcategory_Snacks():
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

def Subcategory_Drinks():
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

def Subcategory_Spec():
        print ("\n" * 5)
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
       

# The front page for the 3 different categories

def CategorySelection():
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
                            |                    \033[1;34;92m4.\033[0m \033[7;34;94mView Cart\033[0m                       |
                            |                                                       |
                            |                    \033[1;34;92m5.\033[0m \033[7;34;94mCheckout\033[0m                        |
                            |                                                       |
                            |                    \033[1;34;92m0.\033[0m \033[7;34;94mReset Currency\033[0m                  |
                            |                                                       |
                            §=======================================================§
""")
       

# Design partition TOP

def DesignTOP():
        print("""
                §=====================================================================================§
                |+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+|
                §=====================================================================================§
              
                                              \033[1;34;95mVending at The Corner.\033[0m
              
              """)

# Design partition BOTTOM

def DesignBOTTOM():
        print("""                §=====================================================================================§
                |+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+|
                §=====================================================================================§""")



def viewcart():
        if not cart:
                print("Your cart is empty.")
                return
       

        print("\nYour cart:")
        print(f" {'name':<20}{'price':<10}{'amount':<10}{'total':<10} ")
        totalprice = 0
        for item in cart.values():
                total = item["price"] * item["amount"]
                print(f" {item['name']}    {item['price']}    {item['amount']}    {total:<10} ")
                totalprice += total
        print(f"\n\nTotal Price: ${totalprice:.2f}")

def checkout():
        if not cart:
                print ("your cart is empty. please add items to checkout!")
                return
        viewcart()
        totalprice = sum( item ["price"] * item ["amount"] for item in cart.values())
        while totalprice> 0:
                payment =float(input(f"your total is ${totalprice:.2f}. Enter payment amount: "))
                if payment >=totalprice:
                        change = payment - totalprice
                        print (f"PAYMENT SUCCESSFULLLL!!!! your change is ${change:.2f}.")
                        cart.clear()
                else:
                        totalprice -= payment
                        print(f"remaining balance: ${totalprice:.2f}")
        print("thanaks for the purchase!")





def MainCurrencyDisplay():
        TheCornerLogoGrey()
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
        print ("Please ensure to select an option to continue")
        MainCurrencyDisplay()



def displayUSD():
        TheCornerLogoGrey()
        CategorySelection()

        selectUSD  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectUSD}")

        if selectUSD == "1" or selectUSD.lower() in "snacks":
                snacks_displayUSD()
        elif selectUSD == "2" or selectUSD.lower() in "drinks":
                drinks_displayUSD()
        elif selectUSD == "3" or selectUSD.lower() in "specialties":
                spec_displayUSD()
        elif selectUSD == "4" or selectUSD.lower() in "view cart":
                viewcart()
        elif selectUSD == "5" or selectUSD.lower() in "checkout":
                checkout()
        elif selectUSD == "0" or selectUSD.lower() in "reset currency":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                displayUSD()


def displayGBP():
        TheCornerLogoGrey()
        CategorySelection()

        selectGBP  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectGBP}")
        if selectGBP == "1" or selectGBP.lower() in "snacks":
                snacks_displayGBP()
        elif selectGBP == "2" or selectGBP.lower() in "drinks":
                drinks_displayGBP()
        elif selectGBP == "3" or selectGBP.lower() in "specialties":
                spec_displayGBP()
        elif selectGBP == "4" or selectGBP.lower() in "view cart":
                viewcart()
        elif selectGBP == "5" or selectGBP.lower() in "checkout":
                checkout()
        elif selectGBP == "0" or selectGBP.lower() in "reset currency":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                displayGBP()

def displayAED():
        TheCornerLogoGrey()
        CategorySelection()

        selectAED  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectAED}")
        if selectAED == "1" or selectAED.lower() in "snacks":
                snacks_displayAED()
        elif selectAED == "2" or selectAED.lower() in "drinks":
                drinks_displayAED()
        elif selectAED == "3" or selectAED.lower() in "specialties":
                spec_displayAED()
        elif selectAED == "4" or selectAED.lower() in "view cart":
                viewcart()
        elif selectAED == "5" or selectAED.lower() in "checkout":
                checkout()
        elif selectAED == "0" or selectAED.lower() in "reset currency":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                displayAED()



def snacks_displayUSD():
        TheCornerLogoGrey()
        Subcategory_Snacks()
        
        selectUSD = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectUSD}")

        if selectUSD == "1" or selectUSD.lower() in "chocolate bars":
                chocolateBar_snacks_1("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "2" or selectUSD.lower() in "chips":
                chips_snacks_2("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "3" or selectUSD.lower() in "crackers & cookies" "crackers and cookies":
                crackersCookies_snacks_3("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "4" or selectUSD.lower() in "candy":
                candy_snacks_4("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "0" or selectUSD.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                snacks_displayUSD()

def snacks_displayGBP():
        TheCornerLogoGrey()
        Subcategory_Snacks()
        
        selectGBP = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectGBP}")

        if selectGBP == "1" or selectGBP.lower() in "chocolate bars":
                chocolateBar_snacks_1("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "2" or selectGBP.lower() in "chips":
                chips_snacks_2("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "3" or selectGBP.lower() in "crackers & cookies" "crackers and cookies":
                crackersCookies_snacks_3("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "4" or selectGBP.lower() in "candy":
                candy_snacks_4("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "0" or selectGBP.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                snacks_displayGBP()

def snacks_displayAED():
        TheCornerLogoGrey()
        Subcategory_Snacks()
        
        selectAED = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectAED}")

        if selectAED == "1" or selectAED.lower() in "chocolate bars":
                chocolateBar_snacks_1("AED", symbols["AED"], rates["AED"])
        elif selectAED == "2" or selectAED.lower() in "chips":
                chips_snacks_2("AED", symbols["AED"], rates["AED"])
        elif selectAED == "3" or selectAED.lower() in "crackers & cookies" "crackers and cookies":
                crackersCookies_snacks_3("AED", symbols["AED"], rates["AED"])
        elif selectAED == "4" or selectAED.lower() in "candy":
                candy_snacks_4("AED", symbols["AED"], rates["AED"])
        elif selectAED == "0" or selectAED.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                snacks_displayAED()



def drinks_displayUSD():
        TheCornerLogoGrey()
        Subcategory_Drinks()
        
        selectUSD = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectUSD}")

        if selectUSD == "1" or selectUSD.lower() in "water":
                water_drinks_1("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "2" or selectUSD.lower() in "energy drinks":
                EnergyDrink_drinks_2("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "3" or selectUSD.lower() in "soda & soft drinks" "soda and soft drinks":
                SodaSoftDrinks_drinks_3("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "4" or selectUSD.lower() in "sports hydration":
                SportsHyd_drinks_4("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "5" or selectUSD.lower() in "ice tea":
                IceTea_drinks_5("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "6" or selectUSD.lower() in "fruit juice":
                FruitJuice_drinks_6("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "7" or selectUSD.lower() in "coffee":
                Coffee_drinks_7("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "0" or selectUSD.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                drinks_displayUSD()

def drinks_displayGBP():
        TheCornerLogoGrey()
        Subcategory_Drinks()
        
        selectGBP = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectGBP}")

        if selectGBP == "1" or selectGBP.lower() in "water":
                water_drinks_1("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "2" or selectGBP.lower() in "energy drinks":
                EnergyDrink_drinks_2("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "3" or selectGBP.lower() in "soda & soft drinks" "soda and soft drinks":
                SodaSoftDrinks_drinks_3("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "4" or selectGBP.lower() in "sports hydration":
                SportsHyd_drinks_4("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "5" or selectGBP.lower() in "ice tea":
                IceTea_drinks_5("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "6" or selectGBP.lower() in "fruit juice":
                FruitJuice_drinks_6("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "7" or selectGBP.lower() in "coffee":
                Coffee_drinks_7("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "0" or selectGBP.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                drinks_displayGBP()

def drinks_displayAED():
        TheCornerLogoGrey()
        Subcategory_Drinks()
        
        selectAED = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectAED}")

        if selectAED == "1" or selectAED.lower() in "water":
                water_drinks_1("AED", symbols["AED"], rates["AED"])
        elif selectAED == "2" or selectAED.lower() in "energy drinks":
                EnergyDrink_drinks_2("AED", symbols["AED"], rates["AED"])
        elif selectAED == "3" or selectAED.lower() in "soda & soft drinks" "soda and soft drinks":
                SodaSoftDrinks_drinks_3("AED", symbols["AED"], rates["AED"])
        elif selectAED == "4" or selectAED.lower() in "sports hydration":
                SportsHyd_drinks_4("AED", symbols["AED"], rates["AED"])
        elif selectAED == "5" or selectAED.lower() in "ice tea":
                IceTea_drinks_5("AED", symbols["AED"], rates["AED"])
        elif selectAED == "6" or selectAED.lower() in "fruit juice":
                FruitJuice_drinks_6("AED", symbols["AED"], rates["AED"])
        elif selectAED == "7" or selectAED.lower() in "coffee":
                Coffee_drinks_7("AED", symbols["AED"], rates["AED"])
        elif selectAED == "0" or selectAED.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                drinks_displayAED()



def spec_displayUSD():
        TheCornerLogoGrey()
        Subcategory_Spec()

        selectUSD = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectUSD}")

        if selectUSD == "1" or selectUSD.lower() in "healthy options":
                HealthyOptions_spec_1("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "2" or selectUSD.lower() in "instant noodles":
                InstantNoodles_spec_2("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "3" or selectUSD.lower() in "sandwiches and wraps":
                SandWraps_spec_3("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "4" or selectUSD.lower() in "fruit cups":
                FruitCups_spec_4("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "5" or selectUSD.lower() in "dried fruit packets":
                DriedFruitPackets_spec_5("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "0" or selectUSD.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                spec_displayUSD()


def spec_displayGBP():
        TheCornerLogoGrey()
        Subcategory_Spec()
        
        selectGBP = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectGBP}")

        if selectGBP == "1" or selectGBP.lower() in "healthy options":
                HealthyOptions_spec_1("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "2" or selectGBP.lower() in "instant noodles":
                InstantNoodles_spec_2("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "3" or selectGBP.lower() in "sandwiches and wraps":
                SandWraps_spec_3("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "4" or selectGBP.lower() in "fruit cups":
                FruitCups_spec_4("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "5" or selectGBP.lower() in "dried fruit packets":
                DriedFruitPackets_spec_5("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "0" or selectGBP.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                spec_displayGBP()


def spec_displayAED():
        TheCornerLogoGrey()
        Subcategory_Spec()
        
        selectAED = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectAED}")

        if selectAED == "1" or selectAED.lower() in "healthy options":
                HealthyOptions_spec_1("AED", symbols["AED"], rates["AED"])
        elif selectAED == "2" or selectAED.lower() in "instant noodles":
                InstantNoodles_spec_2("AED", symbols["AED"], rates["AED"])
        elif selectAED == "3" or selectAED.lower() in "sandwiches and wraps":
                SandWraps_spec_3("AED", symbols["AED"], rates["AED"])
        elif selectAED == "4" or selectAED.lower() in "fruit cups":
                FruitCups_spec_4("AED", symbols["AED"], rates["AED"])
        elif selectAED == "5" or selectAED.lower() in "dried fruit packets":
                DriedFruitPackets_spec_5("AED", symbols["AED"], rates["AED"])
        elif selectAED == "0" or selectAED.lower() in "exit":
                MainCurrencyDisplay()
        else: 
                print ("Please ensure to select an option to continue")
                spec_displayAED()













MainCurrencyDisplay()









