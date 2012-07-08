def largest_palindrome(n_min=10, n_max=99):

    return max(i * j for i in xrange(n_min, n_max + 1)
                     for j in xrange(n_min, n_max + 1)
                     if is_palindrome(i * j))


def is_palindrome(n):
  s = str(n)
  return s == s[::-1]
