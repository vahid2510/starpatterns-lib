from .ansi import render
def _line(spaces:int, width:int, ch:str='*') -> str:
    if width <= 0: return ""
    return " "*spaces + ch*width

def _hollow_line(spaces:int, width:int, ch:str='*') -> str:
    if width <= 0: return ""
    if width == 1: return " "*spaces + ch
    return " "*spaces + ch + " "*(width-2) + ch

def tri_left(n, ch='*', hollow=False):
    for i in range(1, n+1):
        if not hollow or i in (1, n):
            print(ch*i)
        else:
            print(ch + " "*(i-2) + ch)

def tri_right(n, ch='*', hollow=False):
    for i in range(1, n+1):
        if not hollow or i in (1, n):
            print(" "*(n-i) + ch*i)
        else:
            print(" "*(n-i) + ch + " "*(i-2) + ch)

def pyramid(n, ch='*', hollow=False):
    for i in range(1, n+1):
        w, s = 2*i-1, n-i
        print(_hollow_line(s, w, ch) if hollow and i not in (1, n) else _line(s, w, ch))

def pyramid_inv(n, ch='*', hollow=False):
    for i in range(n, 0, -1):
        w, s = 2*i-1, n-i
        if hollow and i not in (1, n):
            print(_hollow_line(s, w, ch))
        elif hollow and i == 1:
            print(" "*(n-1) + ch)
        else:
            print(_line(s, w, ch))

def diamond(n, ch='*', hollow=False):
    pyramid(n, ch, hollow)
    for i in range(n-1, 0, -1):
        w, s = 2*i-1, n-i
        if hollow and i != 1:
            print(_hollow_line(s, w, ch))
        else:
            print(_line(s, w, ch))

def hourglass(n, ch='*', hollow=False):
    for i in range(n, 0, -1):
        w, s = 2*i-1, n-i
        print(_hollow_line(s, w, ch) if hollow and i not in (1, n) else _line(s, w, ch))
    for i in range(2, n+1):
        w, s = 2*i-1, n-i
        print(_hollow_line(s, w, ch) if hollow and i not in (1, n) else _line(s, w, ch))

def rect(rows, cols, ch='*', hollow=False):
    for r in range(rows):
        if not hollow or r in (0, rows-1):
            print(ch*cols)
        else:
            print(ch + " "*(cols-2) + ch)

def twin_pyramids(n, ch='*', gap=None):
    gap = 2*(n-1) if gap is None else gap
    for i in range(1, n+1):
        print(ch*i + " "*(gap - 2*(i-1)) + ch*i)
