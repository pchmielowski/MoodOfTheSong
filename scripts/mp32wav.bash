#!/bin/bash
set -e

function convert_each_file {
  ls "$1" \
    | while read FILE; do
        mpg123 -q -w "$1"/"$FILE".wav "$1"/"$FILE"
        rm "$1"/"$FILE"
      done
}

DATASET='../dataset/emotion-recognition-236f22a6fde0/4. dataset (audio)'
ls "$DATASET" \
  | while read DIR; do
      convert_each_file "$DATASET"/"$DIR"
    done

