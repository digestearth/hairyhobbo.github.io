#!/bin/bash

for f in ./*.jpg ; do echo "$f"; ./upload_pic.sh "$f" $1 $2 ; done
