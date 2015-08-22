#!/usr/bin/env python

import redis

stats = redis.StrictRedis()

times = stats.keys('tweets-*')
times.sort()

total = 0
for time in times:
    num = int(stats.get(time))
    print time, num
    total += num

print "total: %s" % total

