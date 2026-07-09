seat_type = input("enter seat type (Sleeper/AC/general/luxury) : ").lower()

match seat_type :
    case "sleeper":
        print("Sleepr - beds are available")
    
    case "ac":
        print("AC - beds with air coinditoned, comfy ride")

    case "general" :
        print("No Reservation only seating availablity")

    case "luxury":
        print("Luxury premium seats and beds with meals")

    case _:
        print("Invaild Seat Type")