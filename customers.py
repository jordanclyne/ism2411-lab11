#Exercise 1: One Customer
customer1 = {
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "tier": "Gold",
    "ytd_spend": 1500.00
}

print(customer1["name"])
print(customer1["email"])
print(customer1["tier"])
print(customer1["ytd_spend"])
print(customer1)

#Exercise 2: Update and Add
customer1["phone"] = "555-1234"
print(customer1)
customer1["tier"] = "Platinum"
print(customer1)
del customer1["email"]
print(customer1)

#Exercise 3: Safe Lookup
#print(customer1.get("email", "no email on file"))
#print(customer1["email"])

#Exercise 4: Iterate
for key, val in customer1.items():
    print(f"{key}: {val}")
#Using .items() yields both the key and value in the form of a tuple.
for key in customer1:
    print(f"{key}: {customer1[key]}")
#This form of interation yields the key, which is used to access the value.