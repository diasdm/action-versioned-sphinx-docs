#!/bin/sh -l

echo "Hello $1"

tox -e docs

time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT
