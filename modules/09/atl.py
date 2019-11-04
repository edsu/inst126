import json

fh = open('atl.json', encoding='utf8')
atl = json.load(fh)

elec = atl['utilities']['electricity']['yearly']

max_elec = None

for month in elec:
    if max_elec is None:
        max_elec = month
    elif month['value'] > max_elec['value']:
        max_elec = month

print(max_elec)