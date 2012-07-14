import math

_PRIMES = [2]

def prime(n):
    i = _PRIMES[-1] + 1

    while len(_PRIMES) < n:
        if all(i % p != 0 for p in _PRIMES):
            _PRIMES.append(i)

        i += 1

    return _PRIMES[n - 1]

if __name__ == '__main__':
    print prime(10001)
