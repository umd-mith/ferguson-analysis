#!/usr/bin/env python

"""
This is a script to extract some data for Dr Ray.
"""

import os
import bz2
import sys
import gzip
import json

deray = open("deray.json", "w")
tcot_blm = open("tcot_blm.json", "w")

blm_sample = open("blm_sample.json", "w")
blm_count = 0

tcot_sample = open("tcot_sample.json", "w")
tcot_count = 0

def analyze(data_dir):
    global blm_count
    global tcot_count

    for tweet, line in tweets(data_dir):
        if tweet['user']['screen_name'] == 'deray':
            deray.write(line)

        if 'entities' not in tweet:
            continue

        tags = [tag['text'].lower() for tag in tweet['entities']['hashtags']]
        blm = 'blacklivesmatter' in tags
        tcot = 'tcot' in tags
    
        if blm and tcot:
            tcot_blm.write(line)

        if blm:
            blm_count += 1
            if blm_count % 50 == 0:
                blm_sample.write(line)

        if tcot:
            tcot_count += 1
            if tcot_count % 50 == 0:
                tcot_sample.write(line)

def tweets(data_dir):
    count = 0
    for filename in os.listdir(data_dir):
        path = os.path.join(data_dir, filename)
        print "loading %s" % path
        if filename.endswith('json.bz2'):
            fh = bz2.BZ2File(path)
        elif filename.endswith('json.gz'):
            fh = gzip.GzipFile(path)
        else:
            continue
        for line in fh:
            count += 1
            if count % 10000 == 0:
                sys.stdout.write('.')
                sys.stdout.flush()
            try:
                yield json.loads(line), line
            except:
                sys.stdout.write('x')
                sys.stdout.flush()

for bag_dir in os.listdir('data'):
    analyze(os.path.join('data', bag_dir, 'data'))
