#!/bin/bash

bags=(
  # one year anniversary
  '185A16A4-82D9-4810-8568-B52D83BBAAD6'
  # doj report
  '6DC120C7-8901-417B-B387-0C6AFECEE9E8'
  # indictment
  'AF330002-664C-4321-98D2-E753BE8DD025'
  # killing
  'fe28a093-d3f4-42d7-83ba-f5ba1b1cc765'
  # aug 8-10
  'D651C3F6-5619-4A42-A8BC-7C22B7A9A44A'
);

for bag_id in ${bags[@]}
do
    dest="data/$bag_id"
    if [ ! -d $dest ]; then
        mkdir -p $dest
    fi;
    aws s3 sync s3://mith-bags/$bag_id $dest 
done
