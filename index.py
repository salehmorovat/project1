def meter_to_kilometer(meter):
    kilometer = meter / 1000
    return kilometer
meter = float(input("Please enter the meter value: "))
kilometer = meter_to_kilometer(meter)
print("The amount of kilometers is equivalent to:", kilometer)
