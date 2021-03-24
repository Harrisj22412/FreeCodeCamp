#Distance converter converting kilometers to miles.


name = input('First name: ')
distance = input('Enter distance in km : ')
distance_miles = float(distance) / 1.609
print(f'Hi {name.title()}! {distance}km is equivalent to {round(distance_miles, 1)} miles.')



