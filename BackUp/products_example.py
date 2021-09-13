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
    # if to_search == products[i]['p_name'].lower() or to_search == products[i]['brand'].lower() or to_search == products[i]['Category'].lower():
    #     print(products[i])
    condition_1 = to_search in products[i]['p_name'].lower()
    condition_2 = to_search in products[i]['brand'].lower()
    condition_3 = to_search in products[i]['Category'].lower()
    if condition_1 or condition_2 or condition_3:
        print(products[i])
        results.append(products[i])

choice = input("Do you want to sort data based on price Y/N ? ")
if choice == "y" or choice == "Y":
    print("""
    1. Press 1 for low to high
    2. Press 2 for high to low
    """)
    ch = input(":: ")
    if ch == "1":
        output = sorted(results, key=lambda x: x['price'])
    else:
        output = sorted(results, key=lambda x: x['price'], reverse=True)
    print("----Sorted Output----")
    for i in range(len(results)):
        print(results[i])