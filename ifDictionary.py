#make dictionary
day = {
    1: "Sunday",
    2: "Monday",
    3: "Tuesday",
    4: "Wednesday",
    5: "Thursday",
    6: "Friday",
    7: "Saturday"
}

numDay = int(input("Enter the day number: "))

print("day %d is %s" %(numDay, day[numDay]))