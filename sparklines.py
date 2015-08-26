#!/usr/bin/env python

import json
import redis

stats = redis.StrictRedis()
times = [s.split('-', 1)[1] for s in stats.keys('tweets-*')]
times.sort()

def sparklines(key):
    totals = {}
    for time in times:
        for tag, score in stats.zrevrange('%s-%s' % (key, time), 0, 10, withscores=True):
            totals[tag] = totals.get(tag, 0) + score

    members = totals.keys()
    members.sort(lambda a, b: cmp(totals[b], totals[a]))

    sparklines_data = []
    for m in members:
        sparkline = [m]
        for time in times:
            sparkline.append(stats.zrank('%s-%s' % (key, time), m) or 0)
        sparklines_data.append(sparkline)

    return sparklines_data

json.dump(sparklines('hashtags'), open('hashtags.json', 'w'), indent=2)
json.dump(sparklines('users'), open('users.json', 'w'), indent=2)




