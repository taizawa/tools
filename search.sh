#!/usr/local/bin/zsh

find . -name \*.$1 | xargs grep $2

exit 0
