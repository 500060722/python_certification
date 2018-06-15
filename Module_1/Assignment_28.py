print("Hello and welcome to the airport portal.To continue please enter the\
traveller_id and traveler_name")
def check_baggage(baggage_weight):
    if 40>baggage_weight>=0:
        return True
    else:
         return False
def check_immigration(expiry_year):
    if 2025>expiry_year>=2001:
        return True
    else:
        return False
def check_security(noc_status):
    if noc_status=="valid" or "VALID":
        return True
    else:
        return False
def traveler():
    traveler_id=int(input("Enter the traveler_id: "))
    traveler_name=input("Enter the traveler name: ")
    baggage_weight=int(input("Enter the baggage weight of the traveller: "))
    a=check_baggage(baggage_weight)
    expiry_year=int(input("Enter the expiry year of the passport: "))
    b=check_immigration(expiry_year)
    noc_status=input("Enter the status of noc: ")
    c=check_security(noc_status)
    if a==True and b==True and c==True:
        print("The traveler name with name",traveler_name,"and","traveler_id",
              traveler_id,"is allowed to fly")
    else:
        print("Detain Traveler for Re-checking!!!!")
traveler()
