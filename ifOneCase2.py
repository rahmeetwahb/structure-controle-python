#make tuple
dayName = ('sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday')

#make prompt input
day = input("enter the name of the day: ")

if day.lower() == dayName[0] or day.lower() == dayName[6]:
    print("%s is a holiday!!" % day)