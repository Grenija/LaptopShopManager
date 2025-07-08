
import read
import purchase
import write

again = "Y"
while again.upper() == "Y":
    valid = "Y"
    while valid == "Y":
        #Checking if the customer wants to buy or sell the product.
        statement = input("Do you want to sell or buy the laptops?")
        if statement.upper() == "SELL":
            a = read.read_file()#Calling read_file function
            b = purchase.purchase(a)#Calling purchase function
            write.over_write(a, b)#Calling over_write function
            valid = "N"
        elif statement.upper() == "BUY":
            a = read.read_file()#Calling read_file function
            c = purchase.purchase(a)#Calling purchase function
            write.over_write2(a, c)#Calling over_write function
            valid = "N"
        else:
            valid = "N"
            print ("Error found try again")
    again = input("\nAre there any new customers? ")
print("\nThank you for shopping from our store!!")
print("Please check your invoice for your shopping details, \nWhich we have created in .txt file format.")
