import csv

names = []
years = []

buildings = csv.reader(open('buildings.csv'))
header = next(buildings)

for row in buildings:
    names.append(row[0])
    years.append(int(row[2]))

avg = sum(years) / len(years)
print('The average age of buldings on campus is {}'.format(int(avg)))

oldest_year = min(years)
oldest_name = names[years.index(oldest_year)]
print('The oldest building is {}, built in {}.'.format(oldest_name, oldest_year))

newest_year = max(years)
newest_name = names[years.index(newest_year)]
print('The newest building is {}, built in {}.'.format(newest_name, newest_year))
