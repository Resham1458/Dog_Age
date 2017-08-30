def gogo():
    age = int(input("Enter your dog's age in human years:"))
    if age < 0:
        print("Age must be positive number.")
        print("Try again")
        gogo()

    else:
        dog_years = age / 7
        print("Your dog's age in dog's years is", dog_years)
gogo()