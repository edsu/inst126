import json

fh = open('aoc.json')
tweets = json.load(fh)

most_retweeted = None
most_retweeted_video = None

for tweet in tweets:
    rt_count = tweet["retweets_count"]

    if most_retweeted is None:
        most_retweeted = tweet
    elif rt_count > most_retweeted["retweets_count"]:
        most_retweeted = tweet

    if tweet['video'] >= 1:
        if most_retweeted_video is None:
            most_retweeted_video = tweet
        elif rt_count > most_retweeted_video["retweets_count"]:
            most_retweeted_video = tweet

print(most_retweeted['link'])
print(most_retweeted_video['link'])

