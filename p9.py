
__docstring__ = """
Find a, b and c, such that
      a < b < c,
      a + b + c = 1000
      a^2 + b^2 = c^2.
"""

def pythagorean_triplet():
    for a in xrange(1, 1000):
        for b in xrange(a + 1, 1000):
            c = 1000 - a - b
            if a ** 2 + b ** 2 == c **2:
                return (a, b, c)

if __name__ == '__main__':
    a, b, c = pythagorean_triplet()

    print a, b, c, a * b * c
