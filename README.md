# sordid sorting

this is a set of dead simple, barebones python implementations of a few sorting
algorithms. so far, it contains quicksort, merge sort, insertion sort, and
bubble sort. as expected, bubble sort sucks. if you don't believe me, just take
[barry o's word for it][1].

## sort clarg number list
```
$ python sort.py -1 -1 8 6 2 9 1 6 -10 -5 -5 -2 -10 2 -5 2 -3 -8 0 -2
QSRT: 0.06201171875ms    [-10, -8, -5, -5, -5, -3, -2, -2, -1, -1, 0, 1, 2, 2, 2, 6, 6, 8, 9]
MSRT: 0.1279296875ms     [-10, -8, -5, -5, -5, -3, -2, -2, -1, -1, 0, 1, 2, 2, 2, 6, 6, 8, 9]
NSRT: 0.05615234375ms    [-10, -8, -5, -5, -5, -3, -2, -2, -1, -1, 0, 1, 2, 2, 2, 6, 6, 8, 9]
BSRT: 0.064697265625ms   [-10, -8, -5, -5, -5, -3, -2, -2, -1, -1, 0, 1, 2, 2, 2, 6, 6, 8, 9]
```

## make and sort file of numbers
```
$ ./make_nums.sh 10000 10k
$ python sort.py -f 10k.txt
QSRT: 53.744140625ms
MSRT: 106.817871094ms
NSRT: 3431.44116211ms
BSRT: 21690.2368164ms
```

[1]: https://www.youtube.com/watch?v=k4RRi_ntQc8
