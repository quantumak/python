#product_invetory.py

#Programmer: Andrew Kuipers
#Class: CSCI1301 Sec-HY8, Fall 2022
#Purpose: Take inventory and manage items

#lists for functions
productlist = [ ]
pricelist = [ ]
popval = []

#first product function
print("Name of product 1: ", end = "")
productlist.append(input())
print("Price of the product: ")
pricelist.append(float(input()))

print("Inventory after the 1st product is added to it:")
print(productlist,pricelist)
print("")
#--------------------------------------------------------------------------------------
#second product function
print("Name of product 2 to add to the end: ", end = "")
productlist.append(input())
print("Price of the product: ")
pricelist.append(float(input()))

print("Inventory after the 2nd product is added to the end:")
print(productlist,pricelist)
print("")
#--------------------------------------------------------------------------------------
#third product function
print("Name of product 3 to add after the 1st product: ", end = "")
productlist.insert(1 , (input()))
print("Price of the product: ")
pricelist.insert(1 , (float(input())))

print("Inventory after the 3rd product is added after the 1st product:")
print(productlist,pricelist)
print("")
#--------------------------------------------------------------------------------------
#fourth product function
print("Name of product 4 to insert in position 3 of inventory: ", end = "")
productlist.insert(2, (input()))
print("Price of the product: ")
pricelist.insert(2 , (float(input())))

print("Inventory after the 4th product is added to position 3:")
print(productlist,pricelist)
print("")
#--------------------------------------------------------------------------------------
#fifth product function
print("Name of product 5 to add to the end of the inventory: ", end = "")
productlist.append(input())
print("Price of the product: ")
pricelist.append(float(input()))

print("Inventory after the 5th product is added to the end of inventory:")
print(productlist,pricelist)
print("")
#--------------------------------------------------------------------------------------
#Function to raise value of entire price list by a percent
print("By what percentage do you want to increase the product prices? (0-100): ", end = "")
percent = (int(input()))

one_percent = ([int(pricelist) / 100 for pricelist in pricelist])
percent_increase = ([one_percent * percent for one_percent in one_percent])
percent_increased = ([pricelist[int] + percent_increase[int] for int in range(len(pricelist))])

print("\nInventory after all the prices are increased by", percent, "percent:")
print(productlist,percent_increased, "\n")
#--------------------------------------------------------------------------------------
#Function to remove object and price

print("Name of the product to removed from inventory: ", end = " ")
popval.append(input())

poplist_name = ([productlist.index(str) for str in popval])
([percent_increased.pop(index) for index in poplist_name])
([productlist.pop(index) for index in poplist_name])

print("")

print("Inventory after", *popval, "is removed from the inventory:")
print(productlist,percent_increased)
print("")

#--------------------------------------------------------------------------------------

#Function to average the list of prices
listsum = sum(percent_increased)
average_price = listsum / len(productlist)
print("The average price of" , len(productlist), "products is", average_price)

print('\n')

#--------------------------------------------------------------------------------------

#Function to print the inventory forwards and backwards
print('Original inventory: \n', productlist , percent_increased)

print("")

reverselist = productlist.copy()
reverselist.reverse()

reverselist_val = percent_increased.copy()
reverselist_val.reverse()

print("Reversed inventory: \n", reverselist , reverselist_val)

print('\n')
#--------------------------------------------------------------------------------------

#Function to find the least expensive product
val_min = (percent_increased.index(min(percent_increased)))
val_int = int(val_min)

print("The least expensive product" , productlist[val_int], "costs", percent_increased[val_int] , "Dollars.")

#--------------------------------------------------------------------------------------

#Function to print a table with the products and prices
print("")
print("")

print('Products and respective prices side by side: \nProduct   Price \n-------  ------')
print(productlist[0],"      ",percent_increased[0])
print(productlist[1],"      ",percent_increased[1])
print(productlist[2],"      ",percent_increased[2])
print(productlist[3],"      ",percent_increased[3])

print("")
print("")
print('Have a nice day!')
