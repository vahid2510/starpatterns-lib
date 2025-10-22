import math
def draw(n, cond, ch='*'):
    for i in range(n):
        row = []
        for j in range(n):
            row.append(ch if cond(i, j, n) else ' ')
        print(''.join(row))

def border(n, k=1, ch='*'):
    def cond(i,j,n):
        d = min(i, j, n-1-i, n-1-j)
        return d < k
    draw(n, cond, ch)

def plus(n, ch='*'):
    c = n//2
    draw(n, lambda i,j,n: i==c or j==c, ch)

def cross(n, ch='*'):
    draw(n, lambda i,j,n: j==i or j==n-1-i, ch)

def chess(n, ch='*'):
    draw(n, lambda i,j,n: (i+j)%2==0, ch)

def circle_border(n, r=None, ch='*'):
    c = n//2; r = r or c
    eps = max(1, n//24)
    draw(n, lambda i,j,n: abs(math.hypot(i-c, j-c)-r) <= eps, ch)

def circle_fill(n, r=None, ch='*'):
    c = n//2; r = r or c
    draw(n, lambda i,j,n: math.hypot(i-c, j-c) <= r, ch)

def diamond_border(n, r=None, ch='*'):
    c = n//2; r = r or c
    draw(n, lambda i,j,n: abs(i-c)+abs(j-c) == r, ch)

def diamond_fill(n, r=None, ch='*'):
    c = n//2; r = r or c
    draw(n, lambda i,j,n: abs(i-c)+abs(j-c) <= r, ch)

def letter_A(n, ch='*'):
    c = n//2
    def cond(i,j,n):
        left = j == c - i and i <= c
        right = j == c + i and i <= c
        mid = i == c and c - i < j < c + i
        return left or right or mid
    draw(n, cond, ch)
