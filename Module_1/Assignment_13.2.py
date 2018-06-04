print("Hello User! Welcome to discount portal of the store. This portal will\
 calculate the discount on your bill amount. To begin with please: ")
customer_id=int(input("Enter your customer Id by which you got yourself registered \
in the store: "))
if 1000 > customer_id >= 101:
    bill_amount=int(input("Enter the bill amount."))
    if bill_amount >= 1000:
        print("Congrats You avail 5% discount")
        bill= bill_amount - bill_amount*0.05
        print("Discount applied to your bill is ",bill_amount*0.05," and total due bill is ",bill)
    elif 1000>bill_amount>=500:
        print("You avail 2% discount")
        bill= bill_amount - bill_amount*0.02
        print("Discount applied to your bill is",bill_amount*0.02,"and total due bill is ",bill)
    else:
        print("You avail 1% discount")
        bill=bill_amount-bill_amount*0.01
        print("Discount applied to your bill is",bill_amount*0.01,"and total due bill is ",bill)
else:
    print("You are not a valid customer please sign in with the right customer ID")
print("HAPPY SHOPPING!!!!!!!")
