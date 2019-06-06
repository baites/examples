#!/usr/bin/env bash

for input in `ls tests/0*[^a]`
do
    if [ ! -f $input.a ]; then
        cat $input | python ../solution_naive.py > "$input.a"
    fi
    cat $input | python solution.py | diff - "$input.a" > /dev/null
    status=$?
    if [ $status -ne 0 ]; then
        echo "Error $input"
    fi
done
