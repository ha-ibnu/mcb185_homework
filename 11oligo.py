# The Oligo Melting Temp
def tm(A, T, G, C):
    if  A + T + G + C <= 13: return ((A + T)*2 + (G + C)*4)
    elif A + T + G + C > 13: return (64.9 + 41*(G + C - 16.4) / (A + T + G + C))
    else:                    return ("None")

print(tm(5, 7, 3, 4))
print(tm(2, 2, 6, 6))
print(tm(2, 2, 3, 3))

