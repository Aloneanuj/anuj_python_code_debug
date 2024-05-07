# Convert meters to feet.=
# To convert a measurement from meters to feet, you can use the following conversion formula:
# feet=meters×3.28084

def convert_meters_to_feet(length):
    feet = length * 3.28084
    print(feet)

length = float(input("Enter the length in meter : "))
convert_meters_to_feet(length)

