#Jackie-Merritt_Lab-1-Ch3_6/17/2025

choice = "y"
while choice.lower() == "y":

    day = input("Enter in the numeric value of the workday you wish to translate: ")
    print()

    if int(day) == 0:
        print("The workday is a weekend")
    elif int(day) == 1:
        print("The workday is Monday")
    elif int(day) == 2:
        print("The worday is Tuesday")
    elif int(day) == 3:
        print("The workday is Wednesday")
    elif int(day) == 4:
        print("The workday is Thursday")
    elif int(day) == 5:
        print("The workday is Friday")
    elif int(day) == 6:
        print("The workday is a weekend")
    elif int(day) == 7:
        print("The workday is a weekend")
    else:
        print("The workday is invalid")

    choice = input("Continue? (y/n): ")
    print()

print("End.")
