#!/bin/bash
source const.bash

ssh -i $KEY $USER@$ADDR 'rm -rf ~/MoodOfTheSong/code/*'
scp -i $KEY ~/dsp/code/*.py $USER@$ADDR:'~/MoodOfTheSong/code/'
