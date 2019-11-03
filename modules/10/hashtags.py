import json


def get_hashtags(filename):
    hashtags = set()
    for tweet in json.load(open(filename)):
        if tweet['date'][0:4] == '2019':
            for ht in tweet['hashtags']:
                hashtags.add(ht.lower())
    return hashtags

trump = get_hashtags('trump.json')
aoc = get_hashtags('aoc.json')

print(aoc - trump)
print(trump - aoc)



