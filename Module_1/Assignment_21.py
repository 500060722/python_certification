print('Hello Everyone! Welcome to "Variety retail store". Here is the \
list of the items and there prices.')
furniture=['Sofa Set','Dining Table','T.V. Stand','Cupboard']
cost=['20,000','8,500','4,599','13,920']
qty=['12','0','13','10']
for i in range(0,4,1):
    print("Item:",furniture[i])
    print("Cost:",cost[i])
    print("Quantity:",qty[i])
purchasing_item=[]
purchasing_qty=[]
no_of_item=int(input("Enter no. of items: "))
for i in range(0,no_of_item,1):
    item=input("Enter item you want to purchase: ")
    quantity=int(input("Enter the quantity you want to buy: "))
    for i in range(0,4,1):
        if furniture[i]==item:
            purchasing_item.insert(i,item)
        else:
            print("Item Not present!!!!! PLEASE TRY AGAIN")
            break
        if quantity<qty[i]:
            purchasing_qty.insert(i,quantity)
        elif qty[i]==0:
            print("The Item is OUT OF STOCK!!!!!")            
        else:
            print("The quantity you are trying to order is less")
        
print("So That is the list of the items you want to buy:",purchasing_item,purchasing_qty)

    
