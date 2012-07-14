import math

def sieve(n):
    is_prime = [True] * (n - 1)

    for i in xrange(2, int(math.sqrt(n)) + 1):
        if is_prime[i - 2]:
          for j in xrange(i ** 2, n + 1, i):
              is_prime[j - 2] = False

    return is_prime

def sum_primes(n):
    sum = 0
    is_prime = sieve(n)
    i = 2

    while i < n:
        if is_prime[i - 2]:
            sum += i

        i += 1

    return sum

if __name__ == '__main__':
    print sum_primes(2000000)
