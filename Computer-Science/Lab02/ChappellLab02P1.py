flat_fee = 30
num_of_minutes = int(input("Enter the number of minutes used: "))
cost = 0
overage_fee = 0.45

if num_of_minutes > 300:
    print(f"The cost for {num_of_minutes} minutes is {(num_of_minutes - 300) * overage_fee + flat_fee}")
else:
    print(f"The cost for {num_of_minutes} minutes is {flat_fee}")