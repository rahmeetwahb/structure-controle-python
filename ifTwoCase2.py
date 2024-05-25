#make tuple
dayName = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

day = input("enter the name of the day: ")

if day.lower() == dayName[0] or day.lower() == dayName[6]:
    print("%s is a holiday" %day)
else:
    print("%s is a working day" %day)