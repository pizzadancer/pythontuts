
country = input("what country are you from? ")


if country == "canada":
    province = input("where are from, canadian? ")
    province = province.lower()
    
    if province in("alberta," \
            "nunavut", "yukon"):
        tax = 0.05
    elif province == "ontario":
        tax = 0.13
    else: 
        tax = 0.15
else:
    print("enjoy your stay " + country + " person!")
print(tax)