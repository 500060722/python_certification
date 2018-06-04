print("Hello User! Welocome to discount portal of the store. This portal will\
 calculate the discount on your bill amount. To begin with please: ")
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
print("HAPPY SHOPPING!!!!!!!")
