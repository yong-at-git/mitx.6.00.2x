#! /usr/bin/env python3
def fast_fib_rec(memo: {}, n: int):
    if n == 0 or n == 1:
        return 1

    if n in memo:
        return memo[n]
    else:
        memo[n] = fast_fib_rec(memo, n - 1) + fast_fib_rec(memo, n - 2)
        return memo[n]


def fast_fib_itr(memo: {}, n: int):
    memo[0] = 1
    memo[1] = 1

    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]

    return memo[i]


if __name__ == "__main__":
    n = 120
    print("fast_bib_rec n and value,", n, fast_fib_rec({}, n))
    print("fast_bib_itr n and value,", n, fast_fib_itr({}, n))
