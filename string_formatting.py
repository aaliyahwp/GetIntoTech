planets = {'Mercury': 57.91, 'Venus': 108.2, 'Earth': 149.597870, 'Mars': 227.94}
print(planets)
print(type(planets))

# could be a dictionary or a set- this is the style of braces they use
# How far away mercury is from the sun in gigameters

for planet in planets.keys():
    print(planet)
    # as a defult it's given the keys only and not the values
# we want to include the values so we have the distances and we also want to include the row number

# For loop variable in collection:
#   loop body


for row_number, planet in enumerate(planets.keys(), 1):
    print(row_number, planet, planets[planet])

for row_number, planet in enumerate(planets.keys(), 1):
        print("{:2d} Planet {:<10s} Distance {:06.2f} Gm".format(row_number, planet, planets[planet]))
    #     The square brackets are the format identifier

    #  {} is a format specifier
    # < means left aligned, > means right alined, s means string
    # The 0 means pad any space around it with, the .2 float means to two decimal places

    # ennumerate returns you the number and the planet
    # Add in between the last bracket to amend the starting integer
    # When we use a dictionary we put the key in to get the value- you looked up the key to get the value- so when you say go to your planet dictionary it goes and looks up the value
    # We now also want to include the value

# in a dictionary there are two things, the keys and the values- the key is first the value is second

# literal string interpolation (interpreting)
# aka "f" strings
for row_number, planet in enumerate(planets.keys(), 1):
    print(f"{row_number:2d} Planet {planet:<10s} Distance {planets[planet]:06.2f}Gm")
    # A literal string interpolation is more simpler