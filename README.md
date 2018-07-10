## Executor
A command line tool for running C and C++ code against sample test cases on SPOJ and Codeforces.

## Installation

1. Clone this repository.
2. Run `sudo python3 setup.py install`.
3. Try running `executor --help` If no errors appear then executor was successfully installed.

## Usage

Included a sample file `sample/spoj.c` which contains the solution for the problem
[Life, the Universe and Everything](http://www.spoj.com/problems/TEST/) which has the tag `TEST` in the url. To retrieve the sample test cases and check against spoj.c, use:

```
executor sample/spoj.c spoj TEST
```

This can be used for codeforces as well, for the problem tag, look for the contest number, the problem tag (A, B, C etc)
and whether its a problem in the ongoing contest or from a problem set. Incase its part of a ongoing contest use the tag
`c482a`, for problem set use `p482a`.

File `sample/codeforces.c` contains the solution for the problem [Watermelon](http://codeforces.com/problemset/problem/4/A) which has the tag `p4a`. To retrieve the sample test cases and check against codeforces.c use:

```
executor sample/codeforces.c codeforces p4a
```

There are two other command available
1. `check` should be used when the sample cases were already retrieved and we check code against them.
2. `custom` for running code against custom input.
