customer_details={1001:"John",1004:"Jill",1005:"Joe",1003:"Jack"}
print("The details of the customer are:\n",customer_details.values())
print("The number or the customer_id of the customers is:\n",customer_details.keys())
print("The details of the customers in ascending order:\n",sorted(customer_details.values()))
del customer_details[1005]
print("The details of the customer after deleting id=1005",customer_details)
customer_details[1003]="Mary"
print("The updated dictionary after updating the name to 'mary' in 1003",customer_details)
if customer_details.values()==1002 in customer_details:
    print("Yes details of customer with customer id = 1002 exists in the dictionary.")
else:
    print("Details of customer with customer id = 1002 does'nt exist!!!")
