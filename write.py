

def over_write(List, Dictionary):
    L = List #Assign list
    d = Dictionary #Assign Dictionary
    """
    Update product quantity and print remaining inventory after a customer purchases a specific product quantity.
    Then print the closeout products.
    """
    for keys in d.keys():
        if keys == "DELL":
            L[0][2] = str(int(L[0][2])-d['DELL'])
        elif keys == "HP":
            L[1][2] = str(int(L[1][2])-d['HP'])
        elif keys == "ASUS":
            L[2][2] = str(int(L[2][2])-d['ASUS'])
        elif keys == "LENOVO":
            L[3][2] = str(int(L[3][2])-d['LENOVO'])
        else:
            L[4][2] = str(int(L[4][2])-d['MSI'])
    print("\nRemaining Stock Products:\n",L)
        
    files = open("laptops.txt", "w")  #Opening laptops.txt
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()#Closing laptops.txt
    return

def over_write2(List, Dictionary):
    L = List    #Assign list
    d = Dictionary    #Assign Dictionary
    """
    After a customer purchases a certain quantity of a product, update the quantity of the product.
    Then print the closeout products.
    """
    for keys in d.keys():
        if keys == "DELL":
            L[0][2] = str(int(L[0][2])+d['DELL'])
        elif keys == "HP":
            L[1][2] = str(int(L[1][2])+d['HP'])
        elif keys == "ASUS":
            L[2][2] = str(int(L[2][2])+d['ASUS'])
        elif keys == "LENOVO":
            L[3][2] = str(int(L[3][2])+d['LENOVO'])
        else:
            L[4][2] = str(int(L[4][2])+d['MSI'])
    print("\nRemaining Stock Products:\n",L)
        
    files = open("laptops.txt", "w")  #Opening laptops.txt
    for each in L:
        files.write(str(",".join(each)))
        files.write("\n")         
    files.close()#Closing laptops.txt
    return

