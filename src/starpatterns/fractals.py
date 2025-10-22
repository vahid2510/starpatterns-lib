def sierpinski_bit(n_pow2=32, ch='*'):
    for i in range(n_pow2):
        print(' '*(n_pow2 - i) + ''.join(ch if (i & j) == 0 else ' ' for j in range(n_pow2)))
