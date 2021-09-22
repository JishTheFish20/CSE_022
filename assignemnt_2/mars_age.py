age = int(input("Enter your age: "))

minutes = 59356800 / 60
hours = minutes / 60
days = hours / 24
martianYear = days / 365.25
years = age / martianYear

print("On Mars, you would be about %.2f" % years)