def mod_exp(a, b, mod):
  if b == 0:
    return 1
  r = mod_exp(a,b//2,mod)
  if b % 2 != 0:
    r = ((r**2) * (a % mod)) % mod 
  else:
    r = (r**2) % mod 
  return r

def geometric_series_sum(a, n, m):
    if a == 1:
        return n % m
    mod = m * (a - 1)
    a_n = mod_exp(a, n, mod)
    sum_series = (a * (a_n - 1)) // (a - 1)
    return sum_series % m

T = int(input())
for _ in range(T):
    a, n, m = map(int, input().split())
    print(geometric_series_sum(a, n, m))
