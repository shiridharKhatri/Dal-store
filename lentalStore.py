'''
Q1. WAP to calculate the bill for the purchase of items. Provided are the two lists 
dal_type = [“musuro”, “moong”, “toor”, “chana”, “urad”, “arhar”]
price_kg = [180,210,100,210,200,180]
Display the items with their prices and ask customers which and kg they want to 
buy. Calculate total price and if this amounts to value above Rs 1000 provide 5% 
discount and if above Rs. 2500 provide 8% discount on the total. Display the final 
bill. The program should terminate on user request only.
Provide proper comments, input arguments and return type of the methods used. 
The variables should have proper naming. Show the data type of the variable used 
in the program.
'''
import math
dalType = ["musuro", "moong", "toor", "chana", "urad", "arhar"]
priceKg = [180,210,100,210,200,180]

def printBillAfterDiscount(dalName, price, qty, discount):
    print(f"\n🎉 Congratulations! You've got a {discount}% discount! 🎉\n")
    print("="*25)
    print("Your Bill")
    print("="*25)
    print(f"Product : {dalName}\nPrice : {price}\nQuantity: {qty} \nDiscount : {price - (price )* discount/100} -{discount}% OFF\n{'-' * 25}\nTotal : {(math.floor(price - (price )* discount/100) * qty)}\n{'-' * 25}\n")

def printBillWithNoDiscount(dalName, price, qty):
    print("\nOops! You've got no discount 🥲\n")
    print("="*25)
    print("Your Bill")
    print("="*25)
    print(f"Product : {dalName}\nPrice : {price}\nQuantity: {qty} \nDiscount : {price * qty} -0% OFF\n{'-' * 25}\nTotal : {price * qty }\n{'-' * 25}\n")

while True :
    print('\n')
    print("=" * 25)
    print("Dal \t\t Price")
    print("=" * 25)
    for i in range(len(dalType)):
        print(f"{dalType[i].title()}\t\t₹ {priceKg[i]}/k")
    print("-" * 25)
    print('\n')

    try: 
        dalName = input("Enter dal name from table you want to buy >> ")
        dalFound = False
        dalChoosen = str()
        for dal in dalType:
            if dalName.upper() == dal.upper():
                print("\n"+ dal + " found in table"+"\n")
                dalChoosen = dal
                dalFound = True
        if dalFound == False :
            print("\n"+dalName + " is not available in the table")
        else:
            discount = 0
            priceOfChoosenDal = priceKg[dalType.index(dalChoosen)]
            print("\nGet a 5% discount on purchases over ₹1000 and an 8% discount on purchases over ₹2500 🤑")
            while True:
                try:
                    costumerDesiredQuantity = float(input("Enter how much "+ dalChoosen + " you want to buy in kg >> "))
                    break
                except:
                    print("\nPlease enter quantity in number  only !\n")
            # Determine discount based on purchase amount
            if costumerDesiredQuantity*priceOfChoosenDal > 1000 and costumerDesiredQuantity*priceOfChoosenDal < 2500 :
                discount = 5
            elif costumerDesiredQuantity*priceOfChoosenDal > 2500 :
                discount = 8
            else:
                discount = 0
            # Print bill with or without discount
            if discount > 0 : 
                printBillAfterDiscount(dalChoosen, priceOfChoosenDal, costumerDesiredQuantity, discount)
            else:
                printBillWithNoDiscount(dalChoosen, priceOfChoosenDal, costumerDesiredQuantity)
            userFinalChoice = None
            while True :
                print(f"{'Do you want to :''\n''1. Add more quantity''\n''2. Re-purchase Dal''\n''3. Exit'}")
                while True:
                    try:
                        userChoice = int(input("\nPlease enter your choice >> "))
                        userFinalChoice = userChoice
                        break
                    except:
                        print("Please Enter your choice in number 1,2 and 3 only")
                # Handle user's choice to add more quantity
                if userChoice == 1:
                    while True:
                        try:
                            addedQty = float(input("How many quantity you want to add more ? >> "))
                            break
                        except:
                            print("\nPlease enter quantity in number  only !\n")
                    costumerDesiredQuantity+=addedQty
                    # Recalculate discount based on new total amount
                    if costumerDesiredQuantity*priceOfChoosenDal > 1000 and costumerDesiredQuantity*priceOfChoosenDal < 2500 :
                        discount = 5
                    elif costumerDesiredQuantity*priceOfChoosenDal > 2500 :
                        discount = 8
                    else:
                        discount = 0 
                    if discount > 0 :
                        printBillAfterDiscount(dalChoosen, priceOfChoosenDal, costumerDesiredQuantity, discount)
                    else:
                        printBillWithNoDiscount(dalChoosen, priceOfChoosenDal, costumerDesiredQuantity)
                # Handle user's choice to re-purchase or exit
                elif userChoice == 2 or userChoice == 3:
                    break
                else:
                    print("\nPlease choose number 1,2 or 3 only !!\n")
            if userFinalChoice == 3 :
                print("\nThank you for purchasing !! \n\n")
                # This code shows the data type of all the variable used in the code 
                print("Data Types of used variable: ")
                print(f"dalType: {type(dalType)}")
                print(f"priceKg: {type(priceKg)}")
                print(f"dalName: {type(dalName)}")
                print(f"dalFound: {type(dalFound)}")
                print(f"dalChoosen: {type(dalChoosen)}")
                print(f"discount: {type(discount)}")
                print(f"priceOfChoosenDal: {type(priceOfChoosenDal)}")
                print(f"costumerDesiredQuantity: {type(costumerDesiredQuantity)}")
                print(f"userFinalChoice: {type(userFinalChoice)}")
                print(f"userChoice: {type(userChoice)}")
                break
    except:
        print("\nPlease enter valid inputs\n")