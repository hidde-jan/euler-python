import math
import primes

def biggest_prime_factor(n):
  max = int(math.floor(math.sqrt(n)))
  ps = primes.primes(max)
  i = len(ps) - 1

  while i:
    if n % ps[i] == 0:
      return ps[i]

    i -= 1

  return 1

if __name__ == '__main__':
  print biggest_prime_factor(600851475143)
