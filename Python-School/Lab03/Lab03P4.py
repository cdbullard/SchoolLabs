customer_type = input("Enter R for residential customer or B for business customer: ")
num_gallons_used = float(input("How many gallons of water were used? "))

if customer_type.upper() == "R":
    if num_gallons_used <= 6000:
        print(f'Please pay {int(num_gallons_used * 0.006)}')
    elif num_gallons_used > 6000:
        gallons_over = num_gallons_used - 6000
        print(f'Please pay {int(gallons_over * 0.007+ 30)}')
elif customer_type.upper() == "B":
    if num_gallons_used <= 8000:
        print(f'Please pay {int(num_gallons_used * 0.006)}')
    elif num_gallons_used > 8000:
        gallons_over = num_gallons_used - 8000
        print(f'Please pay {int(num_gallons_used * 0.008 + 48)}')


