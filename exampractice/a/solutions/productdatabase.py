products = []
prices = []

name = ""
while name != "STOP":
    name = input("Enter product name (or STOP to finish): ")

    if name != "STOP":
        products.append(name)

        price = input("Enter price: ")
        prices.append(float(price))

searchName = input("Enter product name to search for: ")

found = False

for i in range(len(products)): # REMEMBER THAT IT IS LEN(PRODUCTS), AS RANGE IS NOT END-INCLUSIVE!!
    if products[i] == searchName:
        print("Price: ", prices[i])
        found = True

if found == False:
    print("Product not found")

total = 0

for i in range(len(prices)):
    total = total + prices[i]
    # make sure to copy it exactly, not in any shorthand ways like +=

average = total / len(prices)

print("Average price: ", average)