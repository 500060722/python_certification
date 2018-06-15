print('Hello Everyone! Welcome to "Variety retail store". Here is the \
list of the items and there prices.')
furniture=["Sofa Set","Dining Table","T.V. Stand","Cupboard"]
cost=['20,000','8,500','4,599','13,920']
qty=['12','0','13','10']
for i in range(0,4,1):
    print("Item:",furniture[i])
    print("Cost:",cost[i])
    print("Quantity:",qty[i])
purchased_list=[]
for i in (0,3,1):
    item_name=input("Enter the item name you want to buy from the above shown list")
    if item_name in furniture == True:
        purchased_list.insert(i,item)
        print("The following item is:\n",purchased_list)
    else:
        print("Item is not available!!!!")
print("The following items:\n",purchased_list)

    
