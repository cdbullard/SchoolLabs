def diabeetus(FPG):
    if FPG > 125:
        print("This patient has diabetes")
    elif FPG > 100 <= 125:
        print("This patient has pre-diabetes")
    else:
        print("This patient has healthy fpg levels")


if __name__ == "__main__":
    next_patient = "y"
    while next_patient == "y":
        FPG = int(input("Enter fasting plasma glucose level: "))
        diabeetus(FPG)
        next_patient = input("Checking diabetes for another patient? [y/n] ")
