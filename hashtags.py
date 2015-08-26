#!/usr/bin/env python

import json
import redis

stats = redis.StrictRedis()
times = [s.split('-', 1)[1] for s in stats.keys('tweets-*')]
times.sort()

tag_totals = {}

for time in times:
    for tag, score in stats.zrevrange('hashtags-%s' % time, 0, 10, withscores=True):
        tag_totals[tag] = tag_totals.get(tag, 0) + score

tags = tag_totals.keys()
tags.sort(lambda a, b: cmp(tag_totals[b], tag_totals[a]))

sparklines = []

for tag in tags:
    sparkline = [tag]
    for time in times:
        sparkline.append(stats.zrank('hashtags-%s' % time, tag) or 0)
    sparklines.append(sparkline)

json.dump(sparklines, open('hashtags.json', 'w'), indent=2)




