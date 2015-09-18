#!/usr/bin/env python

# http://nbviewer.ipython.org/gist/anonymous/b2da7e22ecb1fd5a3956

from __future__ import division
from itertools import cycle

import json
import pandas
import matplotlib.pylab 
import scipy.interpolate

hashtag_counts = json.load(open('hashtags.json'))
hashtags = hashtag_counts.keys()

print len(hashtags)








