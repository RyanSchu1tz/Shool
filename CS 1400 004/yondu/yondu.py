'''
By: Ryan Schultz
Date: 8/31/2023
'''
# total pirate input
print("How many pirates:")
pirates = input()
pirates = int(pirates)

# total unit input
print("How many units:")
units = input()
units = int(units)

# pirates taking 3 each
T_Share = units
T_Share = (units - (3 * (pirates-2)))

# Yondu takes 13%
Yondu = (T_Share * 0.13)
T_Share = (T_Share - Yondu)

# Peter Takes 11%
Peter = (T_Share * 0.11)
T_Share = (T_Share - Peter)

# the rest of the unit to the everyone
Crew_S = (T_Share / (pirates))
Yondu = (Yondu + Crew_S)
Peter = (Peter + Crew_S)
Crew_S = (Crew_S + 3)


# Rounding
Yondu = round(Yondu, 2)
Peter = round(Peter, 2)
Crew_S = round(Crew_S, 2)

# Printing
print("Yondu's share: ", Yondu)
print("Peter's Share: ",Peter)
print("Crew's share: ", Crew_S)
