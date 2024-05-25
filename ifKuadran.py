print('enter coordinate data')
x = int(input("enter x value: "))
y = int(input("enter y value: "))

if x > 0 and y > 0:
    print("coordinate I")
elif x < 0 and y > 0:
    print("coordinate II")
elif x < 0 and y < 0:
    print("coordinate III")
elif x > 0 and y < 0:
    print("coordinate IV")
else:
    pass