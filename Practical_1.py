is_day_light_present = input("Is there sunlight? (YES/NO): ").upper()
is_human_presence = input("Is someone present there? (YES/NO): ").upper()

if is_day_light_present == "YES" and is_human_presence == "YES":
    print("LIGHT WILL BE OFF")
else:
    print("LIGHT WILL BE ON")

is_vehicle_there = input("Have you entered with a vehicle? (1 for Yes / 0 for No): ")
is_cash_deduct = input("Is cash is deduct? (1 for Yes / 0 for No): ")

if is_vehicle_there == "1" and is_cash_deduct == "1":
    print("OPEN GATE")
else:
    print("CLOSE GATE")