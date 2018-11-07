if [[ $1 == "" ]]; then
    while read line; do
        clang++ -std=c++11 -g $line -lgtest && ./a.out
    done
else
    clang++ -std=c++11 -g $1 -lgtest && ./a.out
fi
