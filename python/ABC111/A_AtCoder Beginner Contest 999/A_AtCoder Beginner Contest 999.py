def chg(n):
  if n==1:
    return 9
  elif n==9:
    return 1
  return n
 
n = int(input())
n,a1 = divmod(n,10)
n,a2 = divmod(n,10)
n,a3 = divmod(n,10)
 
 
print(100*chg(a3)+10*chg(a2)+chg(a1))