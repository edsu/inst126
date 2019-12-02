import pandas

buildings = pandas.read_csv('buildings.csv', index_col='name')
print(buildings.head())

energy = pandas.read_csv('energy.csv', index_col='date', parse_dates=['date'])
energy = energy.resample('1Y').sum()
print(energy.head())

"""
energy = energy.pivot(index='date', columns='building', values='kBtu')

buildings['energy'] = energy.mean()
buildings['energy/area'] = buildings['energy'] / buildings['area']
buildings = buildings.sort_values('energy/area', ascending=False)
print(buildings.head(10))

buildings = buildings.sort_values('energy', ascending=False)
print(buildings.head(10))
"""
