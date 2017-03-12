#!/bin/bash
set -e

ARCHIVE=archive.zip

wget -O $ARCHIVE https://code.soundsoftware.ac.uk/hg/emotion-recognition/archive/tip.zip

mkdir ../dataset
unzip -q -d ../dataset $ARCHIVE
rm $ARCHIVE
