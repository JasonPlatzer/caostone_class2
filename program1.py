from datetime import datetime, date, time

today = date.today()
print(today)

tommorow = date(2021, 8, 29)
print(tommorow)

next_week = date.fromisoformat('2021-09-03')
print(next_week)
# all make date objects


right_now = datetime.now()
print(right_now)

#counts number of seconds since countin
print(right_now.timestamp())

# prints date when timestamp ccured
my_date = datetime.fromtimestamp(1500000000)
print(my_date)

# a list of tuples
city_state = [('Seatle', 'WA'), ('Portland'), ('San Franscisco', 'CA')]

first_city_state = city_state[0]
city, state = first_city_state
print(city)

cats = set()
cats.add('Lion')
cats.add('Tiger')

bird_list = ['robin', 'swan', 'swan', 'eagle', 'swan']
bird_list_no_doubles = list(set(bird_list))

try:
    print(bird_list[9])
except:
    print('doesnt work')