def mod_exp(a, b, mod):
  if b == 0:
    return 1
  r = mod_exp(a,b//2,mod)
  if b % 2 != 0:
    r = ((r**2) * (a % mod)) % mod 
  else:
    r = (r**2) % mod 
  return r

a, b = map(int, input().split())

result = mod_exp(a, b, 107)
print(result)
