

def read_file():
    #Opening laptops.txt
    file = open("laptops.txt", "r")
    lines = file.readlines()#Calling read_file function
    L = []#Creating list
    for line in lines:
        L.append(line.replace("\n", "").split(","))
    file.close()#Closing laptops.txt
    print("Following products are avilable in our Store")
    print("-----------------------------------------------------------------------------------------------------")
    print("PRODUCT\t\tPRICE\t\tQUANTITY\t\tPROCESSER DETAILS\t\tGRAPHIC CARD")
    print("-----------------------------------------------------------------------------------------------------")
    for i in range(len(L)):
        print(L[i][0], "\t\t", L[i][1], "\t", L[i][2], "\t\t\t", L[i][3], "\t\t\t", L[i][4])
    print("-----------------------------------------------------------------------------------------------------")
    return L


