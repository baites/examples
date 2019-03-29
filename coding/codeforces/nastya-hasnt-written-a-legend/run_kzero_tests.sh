#!/usr/bin/env bash

for input in `ls kzeros_tests/0*[^a]`
do
    if [ ! -f $input.a ]; then
        cat $input | python solution_kzeros_naive.py > "$input.a"
    fi
    cat $input | python solution_kzeros.py | diff - "$input.a"
    status=$?
    if [ $status -ne 0 ]; then
        echo "Error $input"
        exit 1
    fi
done
