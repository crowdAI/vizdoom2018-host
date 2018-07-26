#!/bin/bash

cd /home/crowdai/
mkdir -p output
ls -lha

echo "================================================================================"
echo "Beginning execution of host.py (grader) and save output"
echo "================================================================================"

/home/crowdai/host.py $@
