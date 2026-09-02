import keyword
day = input("what day it is?").strip().capitalize()
print()
print(day)
print(" - " * 35 )
if day in ("Saturtday" , "Sunday"):
     print("enjoy your free time")
else:
     print("work")
