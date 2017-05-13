#!/bin/bash
source const.bash

ssh -X -i $KEY $USER@$ADDR
