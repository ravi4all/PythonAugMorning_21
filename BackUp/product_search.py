products = [
    {"p_name":"Apple Iphone 11","brand":"Apple","Category":"Mobile","price":98000},
    {"p_name":"Redmi Note 6","brand":"Xiaomi","Category":"Mobile","price":15000},
    {"p_name":"Sports Shoes","brand":"Puma","Category":"Shoes","price":3400},
    {"p_name":"JBL Headphones bluetooth","brand":"JBL","Category":"Headphones","price":1200},
    {"p_name":"Leather Jacket","brand":"Zara","Category":"Clothes","price":4500},
    {"p_name":"Puma Shoes","brand":"Puma","Category":"Shoes","price":2070},
    {"p_name":"Adidas Sports Shoes","brand":"Adidas","Category":"Shoes","price":1900},
    {"p_name":"Macbook Pro","brand":"Apple","Category":"Laptop","price":128000},
    {"p_name":"Lenovo thinkpad","brand":"Lenovo","Category":"Laptop","price":78000},
    {"p_name":"Asus Zenbook","brand":"Asus","Category":"Laptop","price":88000},
    ]

to_search = input("Enter your search : ")
to_search = to_search.lower()
'''
1. User can enter either product name or brand or category
2. Store search results in a list
3. Ask user if he/she wants to filter data based on price
  a. low to high
  b. high to low
'''

results = []
for i in range(len(products)):
    cond_1 = to_search in products[i]["p_name"].lower()
    cond_2 = to_search in products[i]["brand"].lower()
    cond_3 = to_search in products[i]["Category"].lower()

    if cond_1 or cond_2 or cond_3:
        print(products[i])
        results.append(products[i])
    
def returnPrice(x):
    return x["price"]

ch = input("Do you want to sort results based on price : [y/n]")
if ch.lower() == "y":
    print("""
    1. Low to High
    2. High to Low
""")
    choice = input("Enter your choice : ")
    if choice == "1":
        print(sorted(results, key=returnPrice))
    else:
        print(sorted(results, key=returnPrice, reverse=True))


