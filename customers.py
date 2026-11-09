#1. I would use .get() in real work when I am uncertain if the value I'm searching for exists because 
# I can provide a default value and avoid errors. I would use the bracket notation when I am certain 
# that the value exists and I want to access it directly. The rule of thumb is my certainty on whether
# or not the value exists.
#2. The pattern in Exercise 8 reminds me of the Excel pattern of using a table to summarize data.
# The Python version is more useful than the Excel version because it doesn't require manual updating.


#Exercise 1: One Customer
customer1 = {
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "tier": "gold",
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
customer1["tier"] = "platinum"
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

#Exercise 5: Lookup Table
tier_discounts = {
    "bronze": 0, 
    "silver": .05, 
    "gold": .10, 
    "platinum": .15}

discount = tier_discounts.get(customer1["tier"], 0)
purchase = 200
discounted_price = purchase * (1 - discount)
print(f"Tier: {customer1['tier']}")
print(f"Discount rate: {discount * 100}%")
print(f"Final price: {discounted_price}")

#Exercise 6: List of Dicts
dict1 = {
    "name": "Jeff", 
    "tier": "platinum"
    }
dict2 = {
    "name": "Sally",
    "tier": "gold"
    }
dict3 = {
    "name": "Bob",
    "tier": "silver"
    }

customers = [dict1, dict2, dict3]
for customer in customers:
    print(f"{customer['name']} is a {customer['tier']} member and receives a {tier_discounts[customer['tier']]*100}% discount.")

#Exercise 7: Nested Catalog
catalog = {"Widget A": {"price": 9.99, "stock": 150}, 
           "Gadget C": {"price": 49.99, "stock": 8}}
for item, details in catalog.items():
    if details["stock"] < 20:
        print(f"{item}: LOW STOCK")

#Exercise 8: Sales by Region
sales_by_region = [
    {"region": "North", "amount": 100},
    {"region": "South", "amount": 150},
    {"region": "East", "amount": 200},
    {"region": "West", "amount": 250},
    {"region": "North", "amount": 300},
    {"region": "South", "amount": 400},
]
summary = {}
for sale in sales_by_region:
    region = sale["region"]
    summary[region] = summary.get(region, 0) + sale["amount"]

for region in summary:
    print(f"{region}: ${summary[region]}")
