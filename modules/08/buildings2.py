import pandas

df = pandas.read_csv('buildings.csv')

max_id = df['built'].idxmax()
newest = df.loc[max_id]
print("The newest building is {}, built in {}.".format(newest['name'], newest['built']))

min_id = df['built'].idxmin()
oldest = df.loc[min_id]
print("The oldest building is {}, built in {}.".format(oldest['name'], oldest['built']))

print('The average building age is {}.'.format(int(df['built'].mean())))


