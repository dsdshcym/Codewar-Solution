def f(n, m)
  sum_1_to_m = (m - 1) * m / 2
  d = n / m
  r = n % m
  return d * sum_1_to_m + (r + 1) * r / 2
end

p f(10, 5)
p f(20, 20)
p f(15, 10)
