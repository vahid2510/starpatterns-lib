import io, sys
from starpatterns import pyramid, cross, draw

def capture(fn, *args, **kwargs):
    buf = io.StringIO()
    old = sys.stdout
    sys.stdout = buf
    try:
        fn(*args, **kwargs)
    finally:
        sys.stdout = old
    return buf.getvalue()

def test_pyramid_basic():
    out = capture(pyramid, 3)
    assert '*' in out and out.count('\n') >= 3

def test_cross_draw():
    out = capture(cross, 7)
    assert out.splitlines()[0].count('*') == 1
