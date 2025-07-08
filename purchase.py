
def purchase(List):
    L = List  #Assign list
    a_name = input("Please enter your name: ")
    print("\nHello " + a_name + "! Welcome to our Electronic Store.\nPlease select product as per your choice.")
    q = {}  #Assign empty dictionary
    flag = "Y"
    while flag.upper() == "Y":
        product = input("\nWhat product do you want? ")
        product_name = product.upper()  #Change to upper case.

        if product_name == L[0][0].upper() \
                or product_name == L[1][0].upper() \
                or product_name == L[2][0].upper() \
                or product_name == L[3][0].upper() \
                or product_name == L[4][0].upper():
            p = True
            while p == True:
                try:
                    p_quantity = int(input("How many " + product + " do you want: "))
                    p = False
                except:  #Executes, if error is found.
                    print("\t\tError!!!\nPlease enter integer value!! ")
            if product_name == L[0][0].upper() and p_quantity <= int(L[0][2]):
                q[product_name] = p_quantity
            elif product_name == L[1][0].upper() and p_quantity <= int(L[1][2]):
                q[product_name] = p_quantity
            elif product_name == L[2][0].upper() and p_quantity <= int(L[2][2]):
                q[product_name] = p_quantity
            elif product_name == L[3][0].upper() and p_quantity <= int(L[3][2]):
                q[product_name] = p_quantity
            elif product_name == L[4][0].upper() and p_quantity <= int(L[4][2]):
                q[product_name] = p_quantity
            else:
                print(
                    "\nSorry!! " + a_name + "!, " + product + " is out of stock.\nWe will add stock of " + product + " later.")

            flag = (input(a_name + " do you want to shop more?(Y/N)"))
        else:
            print("Sorry!! " + product + " is not available in our store.")
            print("\nChoose from following products please!")
            print("--------------------------------------------")
            print("PRODUCT\t\tPRICE\t\tQUANTITY")
            print("--------------------------------------------")
            for i in range(len(L)):
                print(L[i][0], "\t\t", L[i][1], "\t", L[i][2], "\t\t\t", L[i][3], "\t\t\t", L[i][4])  # print, last updated product name, quantity and price.
            print("--------------------------------------------")

    print("\nYou Choosed Items and it's Quantity respectively:\n", q, "\n")

    f_amount = 0  #Amount
    for keys in q.keys():
        if keys == L[0][0].upper():  # Perform this operation if Dell entered by customer.
            p_price0 = int (str(L[0][1]).replace("$",""))
            p_num = int(q[keys])
            p_amount = (p_price0 * p_num)
            f_amount += (p_price0 * p_num)
            print("\nTotal cost for Dell: ", p_amount)
        elif keys == L[1][0].upper():  # Perform this operation if HP entered by customer.
            l_price0 = int (str(L[1][1]).replace("$",""))
            l_num = int(q[keys])
            l_amount = (l_price0 * l_num)
            f_amount += (l_price0 * l_num)
            print("Total cost for HP: ", l_amount)
        elif keys == L[2][0].upper():  # Perform this operation if ASUS entered by customer.
            a_price0 = int (str(L[2][1]).replace("$",""))
            a_num = int(q[keys])
            a_amount = (a_price0 * a_num)
            f_amount += (a_price0 * a_num)
            print("Total cost for ASUS: ", a_amount)
        elif keys == L[3][0].upper():  # Perform this operation if Lenovo entered by customer.
            b_price0 = int (str(L[3][1]).replace("$",""))
            b_num = int(q[keys])
            b_amount = (b_price0 * b_num)
            f_amount += (b_price0 * b_num)
            print("Total cost for Lenovo: ", b_amount)
        else:  # Perform this operation if MSI entered by customer.
            c_price0 = int (str(L[4][1]).replace("$",""))
            c_num = int(q[keys])
            c_amount = (c_price0 * c_num)
            f_amount += (c_price0 * c_num)
            print("Total cost for MSI: ", c_amount)          
   
                
    # Shipping cost and VAT amount
    shipping_cost = 500
    vat_amount = 0.13 * f_amount
    grand_total = f_amount + shipping_cost + vat_amount

    import datetime  # import system date and time.
    dt = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day) + "-" + str(datetime.datetime.now().hour) + "-" + str(
        datetime.datetime.now().minute) + "-" + str(datetime.datetime.now().second)
    invoice = str(dt)
    t = str(datetime.datetime.now().year) + "-" + str(datetime.datetime.now().month) + "-" + str(
        datetime.datetime.now().day)
    d = str(t)
    u = str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute) + ":" + str(
        datetime.datetime.now().second)
    e = str(u)

    file = open(invoice + " (" + a_name + ").txt", "w")  #Generate a bill.
    file.write("=======================================================================")
    file.write("\n")
    file.write("\t\t\tELECTRONIC STORE\t\t\t")
    file.write("\n")
    file.write("Date: " + d + "\nTime: " + e + "")
    file.write("\nName of Customer: " + str(a_name) + "")
    file.write("\n=======================================================================")
    file.write("\nPARTICULAR\tQUANTITY\t\tUNIT PRICE\t\tTOTAL")
    file.write("\n--------------------------------------------------------------------------------------------------------------------------------------------")

    for keys in q.keys():
        if keys == "DELL":
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['DELL']) + " \t\t " + str(L[0][1]) + " \t\t " + str(p_amount)))
        elif keys == "HP":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['HP']) + " \t\t " + str(L[1][1]) + " \t\t " + str(l_amount)))
        elif keys == "ASUS":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['ASUS']) + " \t\t " + str(L[1][1]) + " \t\t " + str(a_amount)))
        elif keys == "LENOVO":
            file.write(str(
                "\n" + str(keys) + " \t\t " + str(q['LENOVO']) + " \t\t " + str(L[1][1]) + " \t\t " + str(b_amount)))
        else:
            file.write(
                str("\n" + str(keys) + " \t\t " + str(q['MSI']) + " \t\t " + str(L[2][1]) + " \t\t " + str(c_amount)))

    file.write("\n\n--------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n")
    file.write("Total Amount (Excluding VAT):" + str( f_amount))
    file.write("\n")
    file.write("\n")
    file.write("Shipping Cost: "+str( shipping_cost))
    file.write("\n")
    file.write("VAT Amount (13%): "+str(vat_amount))
    file.write("\n")
    file.write("Grand Total (Including VAT):"+ str(grand_total))
    file.write("\n")
    file.write("\n----------------------------------------------------------------------------------------------------------------------------------------------")
    file.write("\n\n\t\t\tThank You " + str(a_name) + " for your shopping.\n\t\t\t\tSee you again!")
    file.write("\n=======================================================================")
    file.close()
    return q
