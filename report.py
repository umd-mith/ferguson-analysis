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
The following data was derived from 31,657,545 tweets mentioning the
word *ferguson* during 4 pivotal moments in the 2014-2015 protests 
about the killing of Michael Brown in Ferguson, Missouri:

* August 10 - August 27, 2014: Killing of Michael Brown
* November 11 - December 8, 2014: Non-indictment of Darren Wilson
* February 25 - March 3, 2015: Justice of Department Report on Ferguson Police Department
* July 30 - August 11, 2015: One year after killing of Michael Brown

The twitter JSON data is parsed and features are stored in Redis where
they can be counted easily.

"""
    tweets()
    users()
    hashtags()
    media()
    urls()
    retweets()

def hashtags():
    print
    print "## Hashtags"
    print "| Hashtag | Tweets |"
    print "| ------- | ------:|"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('hashtags-%s' % time, 0, 10, withscores=True):
            print '| %s | %i |' % tag

def media():
    print
    print "## Media"
    print "| Media | Tweets |"
    print "| ----- | ------:|"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('media-%s' % time, 0, 5, withscores=True):
            print '| %s | %i |' % tag

def retweets():
    print
    print "## Retweets"
    print "| Tweet | Retweets |"
    print "| ----- | --------:|"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('retweets-%s' % time, 0, 10, withscores=True):
            print '| %s | %i |' % tag

def tweets():
    print
    print "## Tweets"
    print "| Date | Tweets |"
    print "| ---- | ------:|"
    total = 0
    for time in times:
        num = int(stats.get('tweets-%s' % time))
        print "| %s | %s |" % (time, num)
        total += num
    print "| total | %s |" % total

def urls():
    print
    print "## URLs"
    print "| URL | Tweets |"
    print "| --- | ------:|"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('urls-%s' % time, 0, 10, withscores=True):
            print '|%s|%i|' % tag

def users():
    print
    print "## Users"
    print "| Username | Re(tweets) |"
    print "| -------- | ----------:|"
    for time in times:
        print
        print time
        for tag in stats.zrevrange('users-%s' % time, 0, 10, withscores=True):
            print '|[%s](http://twitter.com/%s)|%i|' % (tag[0], tag[0], tag[1])

if __name__ == "__main__":
    main()
