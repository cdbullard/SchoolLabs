age = int(input("Enter your age: "))   # line 1
if age < 12:
    price = 4
if age < 18:
    price = 7
else:
    price = 10
print("Plase pay this price: ", price)