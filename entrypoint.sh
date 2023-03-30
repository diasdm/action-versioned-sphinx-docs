#!/bin/sh -l

# fail on error
set -e

echo "Building docs with version ${1}"

# install deps
pip install -r build-requirements.txt

# generate docs
VERSION=$1 tox -e docs
