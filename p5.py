import math

def smallest_devisible_by_all(below=10):
  i = below
  stop = math.factorial(below)
  test = range(1, below)

  while i < stop:
    if all(i % x == 0 for x in test):
      return i

    i += below

  raise Exception(u"Impossibru!")

if __name__ == '__main__':
  print smallest_devisible_by_all(20)
