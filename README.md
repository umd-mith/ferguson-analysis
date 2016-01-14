This project hosts some scripts for loading features from several Ferguson 
related Twitter datasets housed at [MITH]. Once loaded into [Redis] the 
features are used to generate a [report] of summary statistics.

Unfortunately Twitter's terms of service do not currently allow the 
four datasets used in this study to be made publicly available. They do
however let 3rd parties distribute datasets of tweet IDs. This repository
includes the tweet identifiers for 31,689,607 tweets from 5 time periods.
Each one was obtained by either search the Twitter API for the word `ferguson`
or using filter streaming API for the word `ferguson`.

More details about these datasets can be obtained from the [Maryland Institute for Technology in the Humanities].

To get started you'll want to install Python and then:

    pip install -r requirements.txt

Then you'll need to reconstitute the Twitter data. Unfortunately you'll need to
run this for a few weeks to get all 31 million tweets again, or at least the
ones that have not been deleted:

    ./hydrate.sh

Once that's done you can run your analysis on the resulting json data or load
the data into [Redis] to generate our report.

    ./load.py
    ./report.py

[MITH]: http://mith.umd.edu
[report]: https://github.com/edsu/ferguson-analysis/blob/master/report.md
[Redis]: http://redis.io
[Maryland Institute for Technology in the Humanities]: http://mith.umd.edu
