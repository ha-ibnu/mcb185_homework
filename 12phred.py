"""Write functions that convert quality value symbols into error rates and vice-versa. The ord() function returns the ASCII value of a letter. The chr() function turns an ASCII value into a letter.

Demonstrate the functions work by calling them several times. Edge cases should return None."""

import math

def char_to_prob(s):
    if not isinstance(s, str) or len(s) != 1: return None
    Q = ord(s) - 33

    if Q < 0: return None
    return 10**(-Q / 10)

def prob_to_char(n):
    if not isinstance(n, (int, float)) or n <= 0 or n >= 1: return None
    Q = round(-10 * math.log10(n))
    P = Q + 33
    if P < 33 or P > 126: return None
    return chr(P)

print(char_to_prob('i'))
print(char_to_prob('b'))
print(char_to_prob('n'))
print(char_to_prob('u'))
print(prob_to_char(char_to_prob('i')))
print(prob_to_char(char_to_prob('b')))
print(prob_to_char(char_to_prob('n')))
print(prob_to_char(char_to_prob('u')))


