#!/usr/bin/env python

import json
import redis

stats = redis.StrictRedis()
times = [s.split('-', 1)[1] for s in stats.keys('tweets-*')]
times.sort()

def counts(key):
    totals = {}
    for time in times:
        for tag, score in stats.zrevrange('%s-%s' % (key, time), 0, 10, withscores=True):
            totals[tag] = totals.get(tag, 0) + score

    members = totals.keys()
    members.sort(lambda a, b: cmp(totals[b], totals[a]))

    counts = {} 
    for m in members:
        member_counts = []
        for time in times:
            member_counts.append((time, stats.zrank('%s-%s' % (key, time), m) or 0))
        counts[m] = member_counts

    return counts

json.dump(counts('hashtags'), open('hashtags.json', 'w'), indent=2)
json.dump(counts('users'), open('users.json', 'w'), indent=2)
