#!/bin/bash
source const.bash

scp -i $KEY $USER@$ADDR:'~/MoodOfTheSong/code/*.png' .
