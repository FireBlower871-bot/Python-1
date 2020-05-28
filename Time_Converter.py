# Function for if the user wants to convert minutes to seconds
def min_to_sec():
    minutes = int(input("Minutes: "))

    while minutes < 1:
        minutes = int(input("Minutes: "))

    seconds = minutes * 60

    print("Seconds:", seconds)

# Function for if the user wants to convert seconds to minutes
def sec_to_min():
    seconds = int(input("Seconds: "))

    while seconds < 1:
        seconds = int(input("Seconds: "))

    minutes = seconds // 60

    print("Minutes:", minutes)

# Function for if the user wants to convert minutes to hours
def min_to_hour():
    minutes = int(input("Minutes: "))

    while minutes < 1:
        minutes = int(input("Minutes: "))

    hours = minutes // 60

    print("Hours:", hours)

# Function for if the user wants to convert seconds to hours.
def sec_to_hour():
    seconds = int(input("Seconds: "))

    while seconds < 1:
        seconds = int(input("Seconds: "))

    hours = seconds // 3600

    print("Hours:", hours)

# Function for if the user wants to convert hours to days.
def hour_to_day():
    hours = int(input("Hours: "))

    while hours < 1:
        hours = int(input("Hours: "))

    days = hours // 24
    remainder = hours % 24

    print(f"There are {days} days and {remainder} hours in {hours} hours!")


# Function that asks the user which converter they want to use, and runs the converter that the user selected
def choices():
    converter = input("Which converter do you want to use?\nType in 1 is you want to use the minutes to seconds converter.\nType in 2 if you want to use the seconds to minutes converter.\nType in 3 if you want to use the minutes to hours converter.\nType in 4 if you want to use the seconds to hours converter.\nOr type in 5 if you want to use the hours to days converter.\n")

    if converter == "1":
        min_to_sec()
    elif converter == "2":
        sec_to_min()
    elif converter == "3":
        min_to_hour()
    elif converter == "4":
        sec_to_hour()
    elif converter == "5":
        hour_to_day()
    else:
        print("Please type in 1 is you want to use the minutes to seconds converter.\nType in 2 if you want to use the seconds to minutes converter.\nType in 3 if you want to use the minutes to hours converter.\nType in 4 if you want to use the seconds to hours converter.\nOr type in 5 if you want to use the hours to days converter.\n")
        choices()


choices()



