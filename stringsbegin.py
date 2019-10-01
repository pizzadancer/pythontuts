first_name = "jim"
last_name = "bob"

#output = "Hello, {1}, {0}".format(first_name, last_name)
output = f"Hello, {first_name} {last_name}"
print(output)

name = input("Who the hell are ya? \n") #asks user for first/last name
output = f"Hello {name}"
print(output)

fav_car = input("What's your favorite car? ")

print(f"{fav_car} very nice")