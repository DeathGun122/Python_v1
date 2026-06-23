def day_of_week(day):
    match day:
        case 1:
            return "Sunday"
        case 2:
            return "Monday"
        case 3:
            return "Tuesday"
        case 4:
            return "Wednesday"
        case 5:
            return "Thursday"
        case 6:
            return "Friday"
        case 7:
            return "Saturday"
        case _:
            return "Invalid day"
        
print(day_of_week(1))  # Output: Sunday
print(day_of_week(6))  # Output: Saturday
print(day_of_week(7))  # Output: Invalid day


def isWeekend(day):
    match day:
        case "Sunday" | "Saturday":
            return True
        case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
            return False
        case _:
            return "Invalid day"
        
print(isWeekend("Sunday"))