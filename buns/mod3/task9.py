n = int(input('число шагов: '))
k = n // 8
x, y = -k, -k
o = n % 8
L = (n // 8 + 1) * 2 
x, y = -k, (-k - 1)
r = o - 1    
p = r // L        
rL = r % L    
if p == 0:                                  
    x, y = (-k + rL), (-k - 1)
elif p == 1:                             
    x, y = (-k + L - 1), (-k - 1 + rL)
elif p == 2:                               
    x, y = (-k + L - 1 - rL), (-k - 1 + L)
else:                                  
    x, y = (-k - 1), (-k - 1 + L - rL)
print((x, y))
