
def triangs():
  n = 0
  t = 0

  while True:
      n += 1
      t = t + n

      yield t

def number_of_divs(x):
  divs = 1

  for n in xrange(x / 2):
    if x % (n + 1) == 0:
      divs += 1

  return divs

for x in triangs():
  n = number_of_divs(x)
  if n >= 500:
    print x
    print "DONE!"
    exit(0)
