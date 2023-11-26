# Receive miles and convert to kms
# Formulae: Kms = miles * 1.609
# User enter miles
# OUtput format is for ex 5 miles equals 8.04 kilometres

miles = input('Enter distance in miles: ')

# Convert sitring to integer
miles = int(miles)
kilometres = miles * 1.6094
print("{0} miles equals to {1} kilometres".format(miles, kilometres))
