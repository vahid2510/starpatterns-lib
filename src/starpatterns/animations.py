import time, math
from .ansi import clear, hide_cursor, show_cursor, render

def anim_wave(W=70, H=20, A=6, k=0.25, dt=0.04, T=300, ch='*'):
    clear(); phase = 0.0
    try:
        hide_cursor()
        for _ in range(T):
            grid = [[' ']*W for _ in range(H)]
            mid = H//2
            for x in range(W):
                y = mid + int(A*math.sin(phase + k*x))
                if 0 <= y < H: grid[y][x] = ch
            render([''.join(r) for r in grid])
            phase += 0.25
            time.sleep(dt)
    finally:
        show_cursor()

def anim_bounce(W=40, H=12, dt=0.03, T=600, ch='*'):
    clear(); x,y,vx,vy = 1,1,1,1
    try:
        hide_cursor()
        for _ in range(T):
            lines = []
            lines.append('#'*W)
            for r in range(1, H-1):
                row = ['#'] + [' ']*(W-2) + ['#']
                if r == y: row[x] = ch
                lines.append(''.join(row))
            lines.append('#'*W)
            render(lines)
            x += vx; y += vy
            if x <= 1 or x >= W-2: vx *= -1
            if y <= 1 or y >= H-2: vy *= -1
            time.sleep(dt)
    finally:
        show_cursor()
