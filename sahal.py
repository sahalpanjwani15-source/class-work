# part 1: ask today's temperature
temperature = int(input("entere today's temperature in celsius : " ))
if temperature < 20:
    outfit ="jackit"
    print("it is cold today.") 
    print("waer a", outfit)
else:
    outfit = "t-shirt"
    print("it is warm today.")
    print("waer a", outfit)

is_raining = input ("Is it rainig today? (yes/no):")

if is_raining == "yes":
    print("bring an umbrella!")

wind_speed = inp(input("enter the wind speed in km/h:  "))

if wind_speed > 30:
    needs_windreaker = "yes"
    print("Is is windy today.")
    print("wear a windreaker over your" outfit)
else:
    needs_windreaker = "on"
    print("Is is windy today.") 
    print("wear a windreaker over your", outfit)

 # part 7: ask whether there are puddles on the ground
ha_puddles = input("are there puddles on the ground? (yes/no) ")

if has_puddles == "yes":
    shoes = "bools"
    print("the ground is wet.")
    print("wear", shoes)
else:
    shoes = "sneakers"
    print("the ground is dry. ")
    print("wear", shoes)

    print("")
    print("wearther check complete!")

    print("==== wearther outfit picker")
    print("temperature:", temperature)
    print("outfit chosen:",outfit)
    print("raining:", is_raining)
    print("windbreaker needed:", needs_windreaker)
    print("shoes chosen:", shoes)
    print("===================================")
    



    