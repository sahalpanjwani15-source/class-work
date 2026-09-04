import keyword
day = input("what day it is?").strip().capitalize()
print()
print(day)
print(" - " * 35 )
if day in ("Saturtday" , "Sunday"):
     print("enjoy your free time")
else:
     print("word")
elif day == " monday":
     print("Day type  : first day of the week. pack your weeekly
plaaner.")
elif day == "friday":
     print("day type   : last school day. return library books 
today.")
elif day in ("tuesday", "wednesday", "thursday"):
     print("day type     : regular school day. stay focused!")
else:
    print("day type   : day not recognised. please check the 
spelling.")
if weather == "sunny" and homewrod == "yes":
    print("after school: head to the park - great weather and 
homeword is done!")
if wearther == "sunny" and homeword == "yes":
    print("weather tip : pack your umbrella - it may get wet 
outside.")

if not (homeword == "yes"):
    print("homeword    : not done yet. finsih it before going out!")
if weather == "rainy" and not (homeword == "yes"):
     print("best plan   : stay in, finoish homework, then watch your
 favourite show.")
 elif weather == "sunny" and homeword == "yes" and not (day in 
("saturday", "sunday" )):
    print("best plan  : all set for a great school day - you are 
prepared!")
elif day in ("saturday", "sunday") and wearther == "sunny":
    print("best plan  : perfect weekend weather - head outside and 
have fun!")
else:
     print("best plan  : take it one step at a time - you have got this!") 
print()
print("plan complete! have a wonderful day!")