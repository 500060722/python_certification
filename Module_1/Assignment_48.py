print("Hello Everyone! Welcome to Retail store. The follwing are the stats of items \
we sell")
print("Retail Store Prices")
item_price=[1050,2200,8575,485,234,150,399]
customer_name=input("Enter the customer name: ")
print("Hello",customer_name)
print("1) Price of the costliest item sold in Retail Store is:",max(item_price))
print("2) Number of items in Retail Store are:",len(item_price))
print("3) Prices of items in increasing order are:",(sorted(item_price)))
print("4) Prices of items in decreasing order are:",(sorted(item_price, reverse=True)))
