# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
# AA -> 26+1
# AZ -> 26+26
# BA -> 26(2) + 1
# ZZ -> 26(26) + 26
# AAA -> (26^2) + 26(1) + 1
# AZ -> 26(1) + 1(26)
# BA
from collections import deque
n = 1
n = 28
n = 701
alph = 'ZABCDEFGHIJKLMNOPQRSTUVWXY'
ans = deque()
while n > 0:
    ans.appendleft(alph[n % 26])
    n -= 1
    n //= 26

print("".join(ans))
