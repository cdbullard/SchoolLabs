def standard_shipping(weight):
    rate = float()
    if weight <= 4:
        rate = weight * 1.05
    elif weight > 4 <= 8:
        rate = weight * 0.95
    elif weight > 8 <= 15:
        rate = weight * 0.85
    elif weight > 15:
        rate = weight * 0.80
    print("Shipping charge: ", rate)


def express_shipping(weight):
    rate = float()
    if weight <= 2:
        rate = weight * 3.25
    elif weight > 2 <= 5:
        rate = weight * 2.95
    elif weight > 5 <= 10:
        rate = weight * 2.75
    print("Shipping charge: ", rate)


if __name__ == "__main__":
    shipping_type = input("Enter S for standard shipping, E for express: ")
    weight = float(input("Enter weight (lbs): "))

    if shipping_type is "S":
        standard_shipping(weight)
    elif shipping_type is "E" and weight <= 10:
        express_shipping(weight)
    else:
        raise ValueError("You cannot do express shipping for packages weighing more than 10 lbs")
