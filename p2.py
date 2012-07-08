def fib(max=10):
  i = 1
  j = 1

  while j < max:
    yield j

    tmp = i + j

    i = j
    j = tmp

if __name__ == '__main__':
    print sum(n for n in fib(4000000) if n % 2 == 0)
