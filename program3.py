classes = ['ITEC 1150', 'ITEC 1100', 'ENGL 1340', 'MATH 1100' ]
# a list comprehension
only_itec = [c.lower() for c in classes if c.startswith('ITEC')]
print(only_itec)

# -1 is not valid
high_temps = [-1, 78, 67, -1, 51, 87, -1, 54, 67, 78, -1, 70]
only_real = [temp for temp in high_temps if temp != -1]
print(only_real)
celsius = [(temp_f -32) * 5 / 9 for temp_f in only_real]
print(celsius)
average = sum(celsius) / len(celsius)
print(f'average is {average:.2f}' )

foods = ['cheese pizza', 'peperooni pizza', 'ice cream',]
pizzas = [food for food in foods if 'pizza' in food]
print(pizzas)