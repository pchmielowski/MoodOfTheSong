#!/bin/bash

CODE=code

find $CODE -name \*.py -exec pep8 {} +
find $CODE -name \*.py -exec pyflakes {} +
pdd --source $CODE > /dev/null

