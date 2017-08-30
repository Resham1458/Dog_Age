def gogo():
    age = int(input("Enter your dog's age in human years:"))
    if age < 0: #checks whether the input number is positive or negative
        print("Age must be positive number.")
        print("Try again")
        gogo()

    else:
        dog_years = age / 7 #converts the dog’s age in human years into dog’s years
        print("Your dog's age in dog's years is", "{0:.2f}".format(dog_years))
gogo()
