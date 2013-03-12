#!/usr/local/bin/zsh

find . -name \*.$1 | xargs grep -n $2

exit 0
