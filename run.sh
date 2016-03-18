#!/usr/bin/env bash
sudo apt-get install python-dev libxml2-dev libxslt1-dev zlib1g-dev

virtualenv ./.env/
. ./.env/bin/activate

pip install -r req.txt