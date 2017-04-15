#!/bin/bash
source const.bash

ssh -X -i $KEY $USER@$ADDR '(cd ~/MoodOfTheSong/code; python3.5 main.py)'
