#!/bin/bash

rsync -avzP -e 'ssh' pi:/root/pwb/git/alg/  ./
