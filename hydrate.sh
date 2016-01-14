#!/bin/bash

# To run the hydration commands you will need to get API keys and set 
# some environment variables. Details are at https://github.com/edsu/twarc

gunzip data/*.gz

echo "hydrating 20140708-20140710-ids.txt"
twarc.py --hydrate data/20140708-20140710-ids.txt > data/20140708-20140710.json 

echo "hydrating 20141111-20141208-ids.txt"
twarc.py --hydrate data/20141111-20141208-ids.txt > data/20141111-20141208.json

echo "hydrating 20150225-20150321-ids.txt"
twarc.py --hydrate data/20150225-20150321-ids.txt > data/20150225-20150321.json

echo "hydrating data/20150730-20150811-ids.txt"
twarc.py --hydrate data/20150730-20150811-ids.txt > data/20150730-20150811.json

echo "hydrating 20150810-20150827-ids.txt"
twarc.py --hydrate data/20150810-20150827-ids.txt > data/20150810-20150827.json

echo "done!"
