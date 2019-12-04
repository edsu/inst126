import pandas

buildings = pandas.read_csv('buildings.csv', index_col='name')
energy = pandas.read_csv('energy.csv', parse_dates=['date'])

# filter out missing energy rows
energy = energy[energy['kBtu'] > 0]

# pivot the building data to get a dataframe where the index 
# is the time and the columns are all the individual buildings
energy = energy.pivot(index='date', columns='building', values='kBtu')

# calculate the average energy used by building, and assign
buildings['kBtu'] = energy.mean()

# calculate the average energy used per square foot
buildings['kBtu/sqft'] = buildings['kBtu'] / buildings['area']

# sort the buildings j
buildings = buildings.sort_values('kBtu/sqft', ascending=False)
print("Top 10")

buildings = buildings.sort_values('kBtu/sqft', ascending=False)
print(buildings.head(10))

buildings.to_csv('buildings_energy.csv')
