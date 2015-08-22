#!/usr/bin/env python

import redis

stats = redis.StrictRedis()

times = [s.split('-', 1)[1] for s in stats.keys('tweets-*')]
times.sort()

for time in times:
    print
    print time
    for tag in stats.zrevrange('hashtags-%s' % time, 0, 5, withscores=True):
        print '- %s (%i)' % tag

