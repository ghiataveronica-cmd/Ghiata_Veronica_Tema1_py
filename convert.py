KM_PER_MILE = 1.609344

value = float(input("Enter value: "))
unit = input("Enter unit (km or mi): ")

if unit == "km":
    result = value / KM_PER_MILE
    print(f"{value} km = {result:.3f} mi")

elif unit == "mi":
    result = value * KM_PER_MILE
    print(f"{value} mi = {result:.3f} km")

else:
    print("Invalid unit! Please enter km or mi.")