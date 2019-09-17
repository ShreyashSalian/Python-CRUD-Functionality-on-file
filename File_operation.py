
print("Please Select any one option from below option!!!!")
print("1. Adding Data to file : ")
print("2. Displaying the Data : ")
print("3. Searching the Record : ")
print("4. Deleting the Reocrd : ")
print("5. Updating the Record: ")
x = int(input("Please Enter your choice : "))

if x == 1:
    wish = "Y"
    invfile = open("inventory.txt", "a")
    while wish == "Y" or wish == "y":
        itemname = input("Enter itemname : ")
        qty = int(input("Enter Quantity : "))
        invfile.write(itemname + "\n")
        invfile.write(str(qty) + "\n")
        wish = input("Do You Wanted To Enter New Record ? (Y/N) : ")
    invfile.close()
    print("INventory data added sucessfully")



elif x == 2:
    v = open("inventory.txt", "r")
    print("ItemName \tQuantity")
    itemname = v.readline()
    while itemname:
        qty = int(v.readline())
        itemname = itemname.rstrip("\n")
        print("%s \t\t%d" % (itemname, qty))
        itemname = v.readline()
    v.close()

elif x == 3:
    v = open("inventory.txt", "r")
    found = False
    search = input("Enter itemname to search : ")
    itemname = v.readline()
    while itemname:
        qty = int(v.readline())
        itemname = itemname.rstrip("\n")
        if itemname.lower() == search.lower():
            print("itemname %s" % itemname)
            print("Quantity is %s" % qty)
            found = True
        itemname = v.readline()
    v.close()
    if not found:
        print("%s is not found in file" % search)

elif x == 4:
    v = open("inventory.txt", "r")
    found = False
    search = input("Enter itemname to search : ")
    itemname = v.readline()
    while itemname:
        qty = int(v.readline())
        itemname = itemname.rstrip("\n")
        if itemname.lower() == search.lower():
            v.remove(itemname)
            v.remove(qty)
            print("The item deleted sucessfully")
            found = True
        itemname = v.readline()
    v.close()
    if not found:
        print("%s is not found in file" % search)

elif x == 5:
    # wap to allow user to modify the quantity of an item from inventory.txt file
    import os

    v = open("inventory.txt", "r")
    Found = False
    search = input("Enter The itemname to search : ")
    newqty = input("Enter the quantity you wanted to enter : ")
    tempfile = open("temp.txt", "w")
    itemname = v.readline()
    while itemname:
        qty = int(v.readline())
        itemname = itemname.rstrip("\n")
        tempfile.write(itemname + "\n")
        if search.lower() == itemname.lower():
            tempfile.write(str(newqty) + "\n")
            found = True
        else:
            tempfile.write(str(qty) + "\n")
        itemname = v.readline()
    v.close()
    tempfile.close()
    os.remove("inventory.txt")
    os.replace("temp.txt", "inventory.txt")
    if found:
        print("file is updated")
    else:
        print("File is not found in the folder" % search)
else:
    print("Please Enter a valid option")