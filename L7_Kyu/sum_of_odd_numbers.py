"""
      1
     3 5
    7 9 11
  13 15 17 19
21 23 25 27 29 ...

Calculate the row sums of this triangle from the row index
(starting at index 1) e.g.:

row_sum_odd_numbers(1); # 1
row_sum_odd_numbers(2); # 3 + 5 = 8

I think then formula is to get max value:
(n + 1) * n

to get minimum value:
n * (n - 1) + 1
"""


def row_sum_odd_numbers(n):
    max = (n + 1) * n
    min = n * (n - 1) + 1
    odd_rows = []
    for i in range(min, max):
        if i % 2 is not 0:
            odd_rows.append(i)

    return sum(odd_rows)


row_sum_odd_numbers(2)
