day = input("Enter the day: ").lower()

match day:
    case "monday":
        print("Monday")
        print("Breakfast: Uthappam")
        print("Lunch: ")
        print("Dinner")

    case "tuesday":
        print("Tuesday")
        print("Breakfast")
        print("Lunch")
        print("Dinner")

    case "wednesday":
        print("Wednesday")
        print("Breakfast")
        print("Lunch")
        print("Dinner")

    case "thursday":
        print("Thursday")
        print("Breakfast")
        print("Lunch")
        print("Dinner")

    case "friday":
        print("Friday")
        print("Breakfast")
        print("Lunch")
        print("Dinner")

    case "saturday":
        print("Saturday")
        print("Breakfast")
        print("Lunch")
        print("Dinner")

    case "sunday":
        print("Sunday")
        print("Breakfast")
        print("Lunch")
        print("Dinner")

    case _:
        print("Invalid day")