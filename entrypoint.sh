#!/bin/sh -l

# fail on error
set -e

echo "Hello $1"

# install deps
pip install -r build-requirements.txt

# generate docs
tox -e docs

time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT
