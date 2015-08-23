#!/usr/bin/env python

# you'll need to run load.py before you can run this

import redis

stats = redis.StrictRedis()
times = [s.split('-', 1)[1] for s in stats.keys('tweets-*')]
times.sort()

def main():
    print "# Ferguson Tweet Analysis"
    print \
"""
The following data was derived from 4 periods of Twitter data
collection using the keyword *ferguson*.
"""
    tweets()
    retweets()
    users()
    hashtags()
    media()
    urls()

def hashtags():
    print "## Hashtags"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('hashtags-%s' % time, 0, 10, withscores=True):
            print '- %s (%i)' % tag

def media():
    print "## Media"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('media-%s' % time, 0, 5, withscores=True):
            print '- %s (%i)' % tag

def retweets():
    print "## Retweets"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('retweets-%s' % time, 0, 10, withscores=True):
            print '- %s (%i)' % tag

def tweets():
    print "## Tweets"
    total = 0
    for time in times:
        num = int(stats.get('tweets-%s' % time))
        print time, num
        total += num
    print "total: %s" % total

def urls():
    print "## URLs"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('urls-%s' % time, 0, 10, withscores=True):
            print '- %s (%i)' % tag

def users():
    print "## Users"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('users-%s' % time, 0, 10, withscores=True):
            print '- %s (%i)' % tag

if __name__ == "__main__":
    main()
