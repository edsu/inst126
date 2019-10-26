import csv

fh = open('buildings.csv')
building_data = csv.reader(fh)

min_name = None
max_name = None
years = []

for row in building_data:
    name = row[0]
    built = row[2]

    if built != "built":
        built = int(built)

        if years and built > max(years):
            max_name = name

        if years and built < min(years):
            min_name = name

        years.append(built)

print(max_name, max(years))
print(min_name, min(years))