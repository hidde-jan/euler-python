def diff_sum_squares(count=100):
  sum_of_squares = 0
  square_of_sums = 0

  for i in xrange(count + 1):
    sum_of_squares += i * i
    square_of_sums += i
  return square_of_sums ** 2 - sum_of_squares

if __name__ == '__main__':
  print diff_sum_squares()
