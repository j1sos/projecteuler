i = 0
ans = 0

while i < 1000:
    if (i % 3 == 0 or i % 5 == 0):
        ans += i
    i += 1
    
print(ans)