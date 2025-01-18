
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

# The 3 different Currency options the user gets to choose from
codes = {
        "USD",
        "AED",
        "GBP"
}

# The symbols that accompany the 3 different currencies
symbols = {
        "AED" : "د.إ",
        "USD" : "$",
        "GBP" : "£"
}

# The rates used for conversion (USD is the standard)
rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

        # Start of the Snacks category 

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
            "C11": { "name" : "Chips Omani", "price": 0.50, "stock" : 3, "tags": ["Gluten Free"] },
}


Candy = {
        "CA1": {"name" : "M&Ms","price": 4.50, "stock" : 5 },
        "CA2": {"name" : "M&Ms (Peanuts)", "price": 5.00, "stock" : 1 },
        "CA3": {"name" : "Skittles", "price": 4.50, "stock" : 0 },
        "CA4": {"name" : "Skittles (Sour)", "price": 5.50, "stock" : 2 },
        "CA5": {"name" : "Juicy Fruitz", "price": 4.66, "stock" : 3 },
}

        # End of the Snacks category 


        # Start of the Drinks category 

water = {
        "W1": { "name" : "Water", "price": 0.99, "stock" : 0, "tags": ["Gluten Free, Sugar Free"]},
        "W2": { "name" : "Vitamin Water", "price": 4.25, "stock" : 1, "tags": ["Gluten Free, Sugar Free"] },
        "W3": { "name" : "Water (Sparkling)", "price": 2.99, "stock" : 5, "tags": ["Gluten Free"] },

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


icetea = {
        "T1": { "name" : "Gold Peak Tea", "price": 3.45, "stock" : 2, "tags": ["Sugar Free"]  },
        "T2": { "name" : "Lipton Ice Tea (Peach)", "price": 3.75, "stock" : 5 },
        "T3": { "name" : "Lipton Ice Tea (Lemon)", "price": 3.75, "stock" : 0 },
        "T4": { "name" : "Lipton Ice Tea (Strawberry)", "price": 2.75, "stock" : 0 },
}

        # End of the Drinks category  



        # Start of the Specialties category
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

        # End of the Specialties category



cart = {}               # The empty dictionary in-which the user will add all items they like to purchase 


# Different border-dividers
codewidth = 3
namewidth = 27
pricew = 4
stockw = 3
borderwidth = 15


Selected_Currency_Snacks = None



import random   # Used to import the random module which will generate randomized related functions. 

def chocolateBar_snacks_1(CurrencyCode, SymbolOfCurrency, ConRate):     # Define Function for -> Chocolate Bars that contains arguments, parameters, or input variables.
 while True:    # A while true loop has been implemented to create a infinite loop, so that stock does not reset after the user exits out of the function. Which closely resembles the actual mannerisms of a vending machine.  
        # The Corner Logo added on top for aesthetics
        TheCornerLogoRed()
        # The top design function
        DesignTOP()
        # This formatted string code structure prints out the items, their names, codes, price and stock.
        # It contains f-strings  -> {} <- which will insert the expressions of designated values.          
        print(f"""                                         Select a \033[1;34;31mtype\033[0m of \033[4;34;92mChocolate Bar\033[0m:
                                
                                   \033[1;34;97mCode:           Name:         Price:          Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in ChocolateBars.items()}   # A new dictionary is created from ChocolateBars.items() where the value is the price of each item. The value is being multiplied by a conversion rate (ConRate, rounded to 2 decimal places).
        Nstock = {code: details["stock"] for code, details in ChocolateBars.items()}    # A new dictionary is created from ChocolateBars.items() where the stock information is extracted.

        for code in ChocolateBars.keys():       # This will print the keys in ChocolateBars.items() individually 
             print (f"""                                   \033[1;7;31;91m {code:>3} \033[0m        \033[1;7;36;96m {ChocolateBars[code]['name']:>9} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>4} \033[0m        \033[1;7;31;91m {Nstock [code]:>2}  \033[0m
                                                                                                    """)    
        # The bottom design function
        DesignBOTTOM()
                # This is the user input where the user is asked to enter the code of the product they're picking.
        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").upper()
        if userchoice == "EXIT":        # If they pick exit they before selecting any items they're brought to the maincurrencypage.
                if CurrencyCode == "USD":
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)
                
        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                
                        AdditionalOrder = input("\n\n\033[1;7;36;96mEnergy Drinks are popular add-ons with Chocolate Bars! Would you like to add a random Energy Drink?: \033[0m").strip().lower()
                        if AdditionalOrder == "yes":
                                DrinksAvailable = [code for code, details in EnergyDrinks.items() if details["stock"] > 0]
                                if DrinksAvailable:
                                        AdditionalOrderCODE = random.choice(DrinksAvailable)
                                        SelectedDrinkCB = EnergyDrinks[AdditionalOrderCODE]
                                        ConvertedAddItem = round(SelectedDrinkCB["price"] * ConRate, 2)
                                        print(f"\n\n\033[1;7;34;94mYour Drink is: {SelectedDrinkCB['name']} which costs {ConvertedAddItem:.2f} {SymbolOfCurrency} \033[0m")
                                        DrinkAMOUNT = int(input(f"\n\n\033[1;7;34;94m Keeping in mind that the available stock is {SelectedDrinkCB['stock']}. Please enter the amount of {SelectedDrinkCB['name']} you would like to purchase: \033[0m"))
                                        print(f"\n\n\033[1;7;34;94mYour Drink is: {SelectedDrinkCB['name']} which costs {ConvertedAddItem:.2f} {SymbolOfCurrency} \n\n\033[0m")
                                        if DrinkAMOUNT <= SelectedDrinkCB["stock"]:
                                                if AdditionalOrderCODE in cart:
                                                        cart[AdditionalOrderCODE]["amount"]     += DrinkAMOUNT
                                                else:
                                                        cart[AdditionalOrderCODE] = {
                                                        "name": SelectedDrinkCB["name"],
                                                        "price": SelectedDrinkCB["price"],
                                                        "amount": DrinkAMOUNT,
                                                        }
                                                SelectedDrinkCB["stock"] -= DrinkAMOUNT
                                                print(f"\033[1;7;36;96m Your Selection of {DrinkAMOUNT} {SelectedDrinkCB['name']} has been added to your cart!\033[0m ")               
                                        else:
                                                print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {SelectedDrinkCB['name']}! Only {SelectedDrinkCB['stock']} is available.\033[0m")
                                else:
                                        print(f"\n\n\033[1;7;31;91m Energy Drinks are currently out of stock...\033[0m")
                        else:
                                print(f"\n\n\033[1;7;31;91m No add-ons selected. \033[0m")
                        continue
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")                
                
                
                

def chips_snacks_2(CurrencyCode, SymbolOfCurrency, ConRate):    # Define Function for -> Chips that contains arguments, parameters, or input variables.
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")

import random



def candy_snacks_4(CurrencyCode, SymbolOfCurrency, ConRate):    # Define Function for -> candy that contains arguments, parameters, or input variables.
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")
 

def water_drinks_1(CurrencyCode, SymbolOfCurrency, ConRate):    # Define Function for -> water that contains arguments, parameters, or input variables.
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def EnergyDrink_drinks_2(CurrencyCode, SymbolOfCurrency, ConRate):      # Define Function for -> energy drinks that contains arguments, parameters, or input variables.
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        AdditionalOrder = input("\n\n\033[1;7;36;96mCandy is a popular add-on with Energy Drinks! Would you like to add candy to your cart: \033[0m").strip().lower()
                        if AdditionalOrder == "yes":
                                CandyAvailable = [code for code, details in Candy.items() if details["stock"] > 0]
                                if CandyAvailable:
                                        AdditionalOrderCODE = random.choice(CandyAvailable)
                                        SelectedDrinkCB = Candy[AdditionalOrderCODE]
                                        ConvertedAddItem = round(SelectedDrinkCB["price"] * ConRate, 2)                                        
                                        print(f"\n\n\033[1;7;34;94mYour Drink is: {SelectedDrinkCB['name']} which costs {ConvertedAddItem:.2f} {SymbolOfCurrency} \033[0m")
                                        DrinkAMOUNT = int(input(f"\n\n\033[1;7;34;94m Keeping in mind that the available stock is {SelectedDrinkCB['stock']}. Please enter the amount of {SelectedDrinkCB['name']} you would like to purchase: \033[0m"))
                                        print(f"\n\n\033[1;7;34;94mYour Item is: {SelectedDrinkCB['name']} which costs {ConvertedAddItem:.2f} {SymbolOfCurrency} \n\n\033[0m")
                                        if DrinkAMOUNT <= SelectedDrinkCB["stock"]:
                                                if AdditionalOrderCODE in cart:
                                                        cart[AdditionalOrderCODE]["amount"]     += DrinkAMOUNT
                                                else:
                                                        cart[AdditionalOrderCODE] = {
                                                        "name": SelectedDrinkCB["name"],
                                                        "price": SelectedDrinkCB["price"],
                                                        "amount": DrinkAMOUNT,
                                                        }
                                                SelectedDrinkCB["stock"] -= DrinkAMOUNT
                                                print(f"\033[1;7;36;96m Your Selection of {DrinkAMOUNT} {SelectedDrinkCB['name']} has been added to your cart!\033[0m ")               
                                        else:
                                                print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {SelectedDrinkCB['name']}! Only {SelectedDrinkCB['stock']} is available.\033[0m")
                                else:
                                        print(f"\n\n\033[1;7;31;91m There aren't any Candy items available...\033[0m")
                        else:
                                print(f"\n\n\033[1;7;31;91m No add-ons selected. \033[0m")
                        continue
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def SodaSoftDrinks_drinks_3(CurrencyCode, SymbolOfCurrency, ConRate):   # Define Function for -> Soda & Soft Drinks that contains arguments, parameters, or input variables.
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")




def IceTea_drinks_5(CurrencyCode, SymbolOfCurrency, ConRate):   # Define Function for -> ice tea drinks that contains arguments, parameters, or input variables.
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")






def HealthyOptions_spec_1(CurrencyCode, SymbolOfCurrency, ConRate):     # Define Function for -> healthy options that contains arguments, parameters, or input variables.
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        AdditionalOrder = input("\n\n\033[1;7;36;96mDried Fruit Packets are popular add-ons with Energy and Granola Bars! Would you like to add a random Dried Fruit Packet?: \033[0m").strip().lower()
                        if AdditionalOrder == "yes":
                                DrinksAvailable = [code for code, details in driedfruitpackets.items() if details["stock"] > 0]
                                if DrinksAvailable:
                                        AdditionalOrderCODE = random.choice(DrinksAvailable)
                                        SelectedDrinkCB = driedfruitpackets[AdditionalOrderCODE]
                                        ConvertedAddItem = round(SelectedDrinkCB["price"] * ConRate, 2)
                                        print(f"\n\n\033[1;7;34;94mYour Item is: {SelectedDrinkCB['name']} which costs {ConvertedAddItem:.2f} {SymbolOfCurrency} \033[0m")
                                        DrinkAMOUNT = int(input(f"\n\n\033[1;7;34;94m Keeping in mind that the available stock is {SelectedDrinkCB['stock']}. Please enter the amount of {SelectedDrinkCB['name']} you would like to purchase: \033[0m"))
                                        print(f"\n\n\033[1;7;34;94mYour Item is: {SelectedDrinkCB['name']} which costs {ConvertedAddItem:.2f} {SymbolOfCurrency} \n\n\033[0m")
                                        if DrinkAMOUNT <= SelectedDrinkCB["stock"]:
                                                if AdditionalOrderCODE in cart:
                                                        cart[AdditionalOrderCODE]["amount"]     += DrinkAMOUNT
                                                else:
                                                        cart[AdditionalOrderCODE] = {
                                                        "name": SelectedDrinkCB["name"],
                                                        "price": SelectedDrinkCB["price"],
                                                        "amount": DrinkAMOUNT,
                                                        }
                                                SelectedDrinkCB["stock"] -= DrinkAMOUNT
                                                print(f"\033[1;7;36;96m Your Selection of {DrinkAMOUNT} {SelectedDrinkCB['name']} has been added to your cart!\033[0m ")               
                                        else:
                                                print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {SelectedDrinkCB['name']}! Only {SelectedDrinkCB['stock']} is available.\033[0m")
                                else:
                                        print(f"\n\n\033[1;7;31;91m Dried Fruit Packets are currently out of stock...\033[0m")
                        else:
                                print(f"\n\n\033[1;7;31;91m No add-ons selected. \033[0m")
                        continue
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")




def SandWraps_spec_3(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoGreen()
        DesignTOP()
        print("""                                         Select a \033[1;34;31mtype\033[0m of \033[4;34;92mSandwich and/or Wrap\033[0m:
                                
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        
                else:
                        print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {item['name']}! Only {item['stock']} is available.\033[0m")
        else: 
                print("\n\n\033[1;7;31;91mPlease enter a valid input!\033[0m")


def FruitCups_spec_4(CurrencyCode, SymbolOfCurrency, ConRate):
 while True:
        TheCornerLogoGreen()
        DesignTOP()
        print("""                                              Select a \033[1;34;31mtype\033[0m of \033[4;34;92mFruit Cup\033[0m:
                                
                        \033[1;34;97mCode:                      Name:              Price:               Stock:\033[0m                 
                                                                                                        """)
        Concurrency = {code: round(details["price"] * ConRate, 2) for code, details in fruitcups.items()}
        Nstock = {code: details["stock"] for code, details in fruitcups.items()}

        for code in fruitcups.keys():
             print (f"""                        \033[1;7;31;91m {code:<{codewidth}} \033[0m        \033[1;7;36;96m {fruitcups[code]['name']:<{namewidth}} \033[0m    \033[1;7;32;92m {Concurrency[code]:.2f}{SymbolOfCurrency:>{pricew}} \033[0m          \033[1;7;31;91m {Nstock [code]:<{stockw}}  \033[0m
                                                                                                    """)    
        DesignBOTTOM()

        userchoice = input(                     "\n\n\033[1;7;31;91mEnter the code of your choice:\033[0m \n\n").strip().lower()
        if userchoice.lower() == "EXIT":
                if CurrencyCode == "USD":
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        AdditionalOrder = input("\n\n\033[1;7;36;96mIce Tea is a popular add-on with Fruit Cups! Would you like to add a random Ice Tea Drink?: \033[0m").strip().lower()
                        if AdditionalOrder == "yes":
                                DrinksAvailable = [code for code, details in icetea.items() if details["stock"] > 0]
                                if DrinksAvailable:
                                        AdditionalOrderCODE = random.choice(DrinksAvailable)
                                        SelectedDrinkCB = icetea[AdditionalOrderCODE]
                                        ConvertedAddItem = round(SelectedDrinkCB["price"] * ConRate, 2)
                                        print(f"\n\n\033[1;7;34;94mYour Drink is: {SelectedDrinkCB['name']} which costs {ConvertedAddItem:.2f} {SymbolOfCurrency} \033[0m")
                                        DrinkAMOUNT = int(input(f"\n\n\033[1;7;34;94m Keeping in mind that the available stock is {SelectedDrinkCB['stock']}. Please enter the amount of {SelectedDrinkCB['name']} you would like to purchase: \033[0m"))
                                        print(f"\n\n\033[1;7;34;94mYour Drink is: {SelectedDrinkCB['name']} which costs {ConvertedAddItem:.2f} {SymbolOfCurrency} \n\n\033[0m")
                                        if DrinkAMOUNT <= SelectedDrinkCB["stock"]:
                                                if AdditionalOrderCODE in cart:
                                                        cart[AdditionalOrderCODE]["amount"]     += DrinkAMOUNT
                                                else:
                                                        cart[AdditionalOrderCODE] = {
                                                        "name": SelectedDrinkCB["name"],
                                                        "price": SelectedDrinkCB["price"],
                                                        "amount": DrinkAMOUNT,
                                                        }
                                                SelectedDrinkCB["stock"] -= DrinkAMOUNT
                                                print(f"\033[1;7;36;96m Your Selection of {DrinkAMOUNT} {SelectedDrinkCB['name']} has been added to your cart!\033[0m ")               
                                        else:
                                                print(f"\n\n\033[1;7;31;91mThere isn't enough stock available for {SelectedDrinkCB['name']}! Only {SelectedDrinkCB['stock']} is available.\033[0m")
                                else:
                                        print(f"\n\n\033[1;7;31;91m Ice Tea Drinks are currently out of stock...\033[0m")
                        else:
                                print(f"\n\n\033[1;7;31;91m No add-ons selected. \033[0m")
                        continue
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
                        displayUSD(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "GBP":
                        displayGBP(SymbolOfCurrency, ConRate)
                elif CurrencyCode == "AED":
                        displayAED(SymbolOfCurrency, ConRate)

        elif userchoice == "CART":
                viewcart(SymbolOfCurrency, ConRate)
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
                        print (f"\n\n\033[1;7;32;92m{amount} {item['name']} added to cart.\033[0m")
                        
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
                            |                \033[1;34;92m3.\033[0m \033[7;34;33mCandy\033[0m                               |
                            |                                                       |
                            |                \033[1;34;92m0.\033[0m \033[7;34;33mExit\033[0m                                |
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
                            |                \033[1;34;92m4.\033[0m \033[7;34;33mIce Tea\033[0m                             |
                            |                                                       |
                            |                \033[1;34;92m0.\033[0m \033[7;34;33mExit\033[0m                                |
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
                            |                \033[1;34;92m2.\033[0m \033[7;34;33mSandwiches and Wraps\033[0m                |
                            |                                                       |
                            |                \033[1;34;92m3.\033[0m \033[7;34;33mFruit Cups\033[0m                          |
                            |                                                       |
                            |                \033[1;34;92m4.\033[0m \033[7;34;33mDried Fruit Packets\033[0m                 |
                            |                                                       |
                            |                \033[1;34;92m0.\033[0m \033[7;34;33mExit\033[0m                                |
                            |                                                       |
                            §=======================================================§
""")
        print ("\n" * 4)
       

# The front page for the 3 different categories

def CategorySelection():
        print ("""\
                            §=======================================================§
                            |           \033[1;34;95mWelcome to Vending at 'The Corner'\033[0m          |
                            |                                                       |
                            |         Please select \033[1;34;31m1\033[0m of the \033[1;34;92m3\033[0m categories:          |
                            |                                                       |
                            |                    \033[1;34;92m1.\033[0m \033[7;34;94mSnacks\033[0m                          |
                            |                                                       |
                            |                    \033[1;34;92m2.\033[0m \033[7;34;94mDrinks\033[0m                          |
                            |                                                       |
                            |                    \033[1;34;92m3.\033[0m \033[7;34;94mSpecialties\033[0m                     |
                            |                                                       |
                            |                    \033[1;34;92m4.\033[0m \033[7;34;97mView Cart\033[0m                       |
                            |                                                       |
                            |                    \033[1;34;92m5.\033[0m \033[7;34;97mCheckout\033[0m                        |
                            |                                                       |
                            |                    \033[1;34;92m0.\033[0m \033[7;34;97mReset Currency\033[0m                  |
                            |                                                       |
                            |                                                       |
                            |                      \033[7;35;95mFilters\033[0m                          |
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


cartwidth = 25
pricewidth = 10
amountwdith = 6
totalwidth = 3




def viewcart(SymbolOfCurrency, ConRate):
        if not cart:
                print("\n\n\033[1;7;31;91mYour cart is empty.\033[0m\n\n")
                return
        
        TheCornerLogoGrey()
        DesignTOP()
        print("""                                                    \033[1;7;34;90m Your cart: \033[0m""")
        print("\n")
        print("""                    \033[1;7;37;97m NAME: \033[0m                \033[1;7;32;92m PRICE: \033[0m               \033[1;7;34;94m AMOUNT: \033[0m              \033[1;7;33;93m TOTAL: \033[0m""")
        print("\n")
        totalprice = 0
        for item in cart.values():
                Converted_Price = round(item["price"] * ConRate, 2)
                total = round(Converted_Price * item["amount"], 2)
                print(f"""                    \033[1;7;37;97m {item['name']:<{cartwidth}}\033[0m        \033[1;7;32;92m{Converted_Price:.2f} {SymbolOfCurrency:>} \033[0m         \033[1;7;34;94m{item['amount']:>{amountwdith}} \033[0m          \033[1;7;33;93m {total} {SymbolOfCurrency} \033[0m""")
                totalprice += total
        print(f"""\n                                             \033[1;7;32;92m  Total Price: {totalprice:.2f} {SymbolOfCurrency}  \033[0m\n\n""")
        DesignBOTTOM()


        Proceed_To_Checkout = input("                   \n\n\033[1;7;32;92m Do you wish to proceed to checkout?: \033[0m\n\n").strip().lower()
        
        if Proceed_To_Checkout == 'yes': 
                checkout(SymbolOfCurrency, ConRate)
        elif Proceed_To_Checkout == 'no':
                print("\n\n\033[1;7;31;91mYou chose not to checkout...\033[0m")
                CategorySelection()
        else:
                print("\n\n\033[1;7;31;91m Please type either 'yes' or 'no'.\033[0m")
                viewcart(SymbolOfCurrency, ConRate)



def checkout(SymbolOfCurrency, ConRate):
        totalprice = 0
        for item in cart.values():
                Converted_Price = round(item["price"] * ConRate, 2)
                total = round(Converted_Price * item["amount"], 2)
                totalprice += total 

        TheCornerLogoGrey()
        DesignTOP()
        print("""\n                                               \033[1;7;32;92mYour Checkout Summary:\033[0m\n\n""")
        print("""                    \033[1;7;37;97m NAME: \033[0m                \033[1;7;32;92m PRICE: \033[0m               \033[1;7;34;94m AMOUNT: \033[0m              \033[1;7;33;93m TOTAL: \033[0m\n\n""")
        for item in cart.values():
                Converted_Price = round(item["price"] * ConRate, 2)
                total = round(Converted_Price * item["amount"], 2)
                print(f"""                    \033[1;7;37;97m {item['name']:<{cartwidth}}\033[0m        \033[1;7;32;92m {Converted_Price:.2f} {SymbolOfCurrency:>} \033[0m         \033[1;7;34;94m{item['amount']:>{amountwdith}} \033[0m          \033[1;7;33;93m{total} {SymbolOfCurrency:>{totalwidth}}\033[0m""")
                totalprice += total
        print(f"""\n\n                                               \033[1;7;32;92mTotal Price: {totalprice:.2f} {SymbolOfCurrency} \033[0m\n\n""")
        DesignBOTTOM()



        DesignTOP
        print("""\n                                                    1. \033[1;7;32;92m Cash \033[0m""")
        print("""\n                                                    2. \033[1;7;32;92m Card \033[0m""")
        Proceed_To_Payment = input("\n\n                                  \033[1;7;32;92mPlease enter your preferred payment option: \033[0m").strip().lower()
        if Proceed_To_Payment == "1" or Proceed_To_Payment.lower() in "cash":
          while True:
                CASH = float(input("\n\n                                      \033[1;7;32;95m Enter the Cash amount: \033[0m"))
                if CASH < totalprice:
                        print(f"\n\n           \033[1;7;32;91m You have entered an insufficient amount of cash. To proceed you'll need to enter {totalprice - CASH:.2f} {SymbolOfCurrency} more.\033[0m")
                        print("""\n                                                  1. \033[1;7;32;92m Retry \033[0m""")
                        print("""\n                                                  2. \033[1;7;32;92m Cancel \033[0m""")
                        Try_Again = input("\n          \033[1;7;32;91m Would you like to re-enter a different amount or cancel entirely: \033[0m").strip().lower()
                        if Try_Again.lower() in "Cancel Payment":
                                print("\n\033[1;7;34;47mYour payment has been canceled.\033[0m")
                                break
                
                else: 
                        CHANGE = round(CASH - totalprice, 2)
                        print(f"\n\n                                     \033[1;7;32;92mPayment completed. Your change is {CHANGE:.2f} {SymbolOfCurrency} \033[0m")
                        print("\n\n                                         \033[1;7;37;97mThank you for vending at The Corner.\n\n\033[0m")
                        MainCurrencyDisplay(SymbolOfCurrency, ConRate)
                        cart.clear()
        elif Proceed_To_Payment == "2" or Proceed_To_Payment.lower() in "card":
          while True:
                  CARD_Num = input("\n\n                                             \033[1;7;32;95mEnter your 4 digit PIN code:\033[0m")

                  if len(CARD_Num) < 4: 
                          print ("\n\n                                 \033[1;7;32;95mPlease enter your 4 digit PIN code\033[0m")
                  else: 
                          print(f"\n\n                      \033[1;7;32;92mPayment completed. The amount: {totalprice:.2f} {SymbolOfCurrency} has been charged onto your card.\033[0m")
                          print("\n\n                                         \033[1;7;37;97mThank you for vending at The Corner.\n\n\033[0m")
                          cart.clear()
                          break
        DesignBOTTOM()                        
        MainCurrencyDisplay(SymbolOfCurrency, ConRate)




        if not cart:
                print ("Your cart is empty. Please add items to checkout!")
                return
        viewcart(SymbolOfCurrency, ConRate)
        totalprice = sum( item ["price"] * item ["amount"] for item in cart.values())
        while totalprice> 0:
                payment =float(input(f"your total is ${totalprice:.2f}. Enter payment amount: "))
                if payment >=totalprice:
                        change = payment - totalprice
                        print (f"PAYMENT SUCCESSFUL! Your change is {SymbolOfCurrency}{change:.2f}.")
                        cart.clear()
                else:
                        totalprice -= payment
                        print(f"remaining balance: ${totalprice:.2f}")
        print("Thank you for your purchase!")
        DesignBOTTOM()



def MainCurrencyDisplay(SymbolOfCurrency, ConRate):
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

        if selectcurrency == "1" or selectcurrency.lower() in "dollars usd":
                displayUSD(SymbolOfCurrency, ConRate)
        elif selectcurrency == "2" or selectcurrency.lower() in "pounds gbp":
                displayGBP(SymbolOfCurrency, ConRate)
        elif selectcurrency == "3" or selectcurrency.lower() in "dirhams aed":
                displayAED(SymbolOfCurrency, ConRate)
        print ("\n\nPlease ensure to select an option to continue")
        MainCurrencyDisplay(SymbolOfCurrency, ConRate)


AllItems = {
        "Chocolate Bars": ChocolateBars,
        "Chips": Chips,
        "Candy": Candy,
        "water": water,
        "EnergyDrinks": EnergyDrinks,
        "SodaSoftDrinks": SodaSoftDrinks,
        "icetea": icetea,
        "healthyoptions": healthyoptions,
        "sandwichswraps": sandwichswraps,
        "fruitcups": fruitcups,
        "driedfruitpackets": driedfruitpackets,
}

filterborder = 30

def FactsFilter(tag):
        Items_found = False
        DesignTOP()
        for category, items in AllItems.items():
                for code, details in items.items():
                    if "tags" in details and isinstance(details["tags"], list):    
                        if tag.lower() in [t.lower() for t in details["tags"]]:
                                if details["stock"] > 0:
                                        tags_align = ', '.join(details["tags"])
                                        print(f"                       \033[1;7;34;100m {details['name']:<{filterborder}} --- {tags_align:<{filterborder}}       \033[0m\n")
                                        Items_found = True
        DesignBOTTOM()
        print("\n\n")
        print("\n\n")
        if not Items_found:
                print(f"\033[1;7;36;96mNo items found...\033[0m")


def ShowFilter():
        TheCornerLogoGrey()
        DesignTOP()
        print ("""\
                            §=======================================================§
                            |                                                       |
                            |             Select a \033[1;34;31mFilter\033[0m to \033[4;34;92mobserve\033[0m:               |
                            |                                                       |
                            |                   \033[1;34;92m1.\033[0m \033[7;34;33mVegan\033[0m                            |
                            |                                                       |
                            |                   \033[1;34;92m2.\033[0m \033[7;34;33mGluten Free\033[0m                      |
                            |                                                       |
                            |                   \033[1;34;92m3.\033[0m \033[7;34;33mSugar Free\033[0m                       |
                            |                                                       |
                            |                   \033[1;34;92m0.\033[0m \033[7;34;33mExit\033[0m                             |
                            |                                                       |
                            §=======================================================§
""")
        UserFilter = input("\n\n\033[1;7;36;96m Select a Filter to observe nutritional information of our products: \033[0m").strip().lower()
        if UserFilter == "0" or UserFilter == "exit":
                CategorySelection()
        elif UserFilter == "1" or UserFilter == "vegan":
                FactsFilter("Vegan")
        elif UserFilter == "2" or UserFilter == "gluten free":
                FactsFilter("Gluten Free")
        elif UserFilter == "3" or UserFilter == "sugar free":
                FactsFilter("Sugar Free")
        else: 
                print(f"\033[1;7;36;96mNo items found...\033[0m")
        DesignBOTTOM()


def displayUSD(SymbolOfCurrency, ConRate):
        TheCornerLogoGrey()
        CategorySelection()

        selectUSD  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectUSD}")

        if selectUSD == "1" or selectUSD.lower() in "snacks":
                SnacksDisplay("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "2" or selectUSD.lower() in "drinks":
                DrinksDisplay("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "3" or selectUSD.lower() in "specialties":
                SpecDisplay("USD", symbols["USD"], rates["USD"])
        elif selectUSD == "4" or selectUSD.lower() in "view cart":
                viewcart(SymbolOfCurrency, ConRate)
        elif selectUSD == "5" or selectUSD.lower() in "checkout":
                checkout(SymbolOfCurrency, ConRate)
        elif selectUSD == "0" or selectUSD.lower() in "reset currency":
                MainCurrencyDisplay()
        elif selectUSD == selectUSD.lower() in "filters":
                ShowFilter()
        else: 
                print ("Please ensure to select an option to continue")
                displayUSD(SymbolOfCurrency, ConRate)


def displayGBP(SymbolOfCurrency, ConRate):
        TheCornerLogoGrey()
        CategorySelection()

        selectGBP  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectGBP}")
        if selectGBP == "1" or selectGBP.lower() in "snacks":
                SnacksDisplay("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "2" or selectGBP.lower() in "drinks":
                DrinksDisplay("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "3" or selectGBP.lower() in "specialties":
                SpecDisplay("GBP", symbols["GBP"], rates["GBP"])
        elif selectGBP == "4" or selectGBP.lower() in "view cart":
                viewcart(SymbolOfCurrency, ConRate)
        elif selectGBP == "5" or selectGBP.lower() in "checkout":
                checkout(SymbolOfCurrency, ConRate)
        elif selectGBP == "0" or selectGBP.lower() in "reset currency":
                MainCurrencyDisplay()
        elif selectGBP == selectGBP.lower() in "filters":
                ShowFilter()
        else: 
                print ("Please ensure to select an option to continue")
                displayGBP(SymbolOfCurrency, ConRate)


def displayAED(SymbolOfCurrency, ConRate):
        TheCornerLogoGrey()
        CategorySelection()

        selectAED  = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectAED}")
        if selectAED == "1" or selectAED.lower() in "snacks":
                SnacksDisplay("AED", symbols["AED"], rates["AED"])
        elif selectAED == "2" or selectAED.lower() in "drinks":
                DrinksDisplay("AED", symbols["AED"], rates["AED"])
        elif selectAED == "3" or selectAED.lower() in "specialties":
                SpecDisplay("AED", symbols["AED"], rates["AED"])
        elif selectAED == "4" or selectAED.lower() in "view cart":
                viewcart(SymbolOfCurrency, ConRate)
        elif selectAED == "5" or selectAED.lower() in "checkout":
                checkout(SymbolOfCurrency, ConRate)
        elif selectAED == "0" or selectAED.lower() in "reset currency":
                MainCurrencyDisplay()
        elif selectAED == selectAED.lower() in "filters":
                ShowFilter()
        else: 
                print ("Please ensure to select an option to continue")
                displayAED(SymbolOfCurrency, ConRate)



def SnacksDisplay(codes, symbols, rates):
        TheCornerLogoGrey()
        Subcategory_Snacks()
        
        selectUSD = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectUSD}")

        if selectUSD == "1" or selectUSD.lower() in "chocolate bars":
                chocolateBar_snacks_1(codes, symbols, rates)
        elif selectUSD == "2" or selectUSD.lower() in "chips":
                chips_snacks_2(codes, symbols, rates)
        elif selectUSD == "3" or selectUSD.lower() in "candy":
                candy_snacks_4(codes, symbols, rates)
        elif selectUSD == "0" or selectUSD.lower() in "exit":
                MainCurrencyDisplay(symbols, rates)
        else: 
                print ("Please ensure to select an option to continue")
                SnacksDisplay(codes, symbols, rates)



def DrinksDisplay(codes, symbols, rates):
        TheCornerLogoGrey()
        Subcategory_Drinks()
        
        selectUSD = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectUSD}")

        if selectUSD == "1" or selectUSD.lower() in "water":
                water_drinks_1(codes, symbols, rates)
        elif selectUSD == "2" or selectUSD.lower() in "energy drinks":
                EnergyDrink_drinks_2(codes, symbols, rates)
        elif selectUSD == "3" or selectUSD.lower() in "soda & soft drinks" "soda and soft drinks":
                SodaSoftDrinks_drinks_3(codes, symbols, rates)
        elif selectUSD == "4" or selectUSD.lower() in "ice tea":
                IceTea_drinks_5(codes, symbols, rates)
        elif selectUSD == "0" or selectUSD.lower() in "exit":
                MainCurrencyDisplay(symbols, rates)
        else: 
                print ("Please ensure to select an option to continue")
                DrinksDisplay(codes, symbols, rates)



def SpecDisplay(codes, symbols, rates):
        TheCornerLogoGrey()
        Subcategory_Spec()

        selectSpec = ( " " * 40 + input ( " " * 40 + "\033[1;107;90mYOUR SELECTION:\033[0m ") ).strip()
        print(f"\n\nUser Selected -> {selectSpec}")

        if selectSpec == "1" or selectSpec.lower() in "healthy options":
                HealthyOptions_spec_1(codes, symbols, rates)
        elif selectSpec == "2" or selectSpec.lower() in "sandwiches and wraps":
                SandWraps_spec_3(codes, symbols, rates)
        elif selectSpec == "3" or selectSpec.lower() in "fruit cups":
                FruitCups_spec_4(codes, symbols, rates)
        elif selectSpec == "4" or selectSpec.lower() in "dried fruit packets":
                DriedFruitPackets_spec_5(codes, symbols, rates)
        elif selectSpec == "0" or selectSpec.lower() in "exit":
                MainCurrencyDisplay(symbols, rates)
        else: 
                print ("Please ensure to select an option to continue")
                SpecDisplay(codes, symbols, rates)















SymbolOfCurrency = "$"

rates = {
        "AED" : 3.67,
        "USD" : 1,
        "GBP" : 0.8,
}

MainCurrencyDisplay(SymbolOfCurrency, rates)






