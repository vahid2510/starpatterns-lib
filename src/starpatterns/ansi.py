import sys
CSI = "\x1b["

def clear():
    sys.stdout.write(CSI + "2J" + CSI + "H"); sys.stdout.flush()

def home():
    sys.stdout.write(CSI + "H"); sys.stdout.flush()

def hide_cursor():
    sys.stdout.write(CSI + "?25l"); sys.stdout.flush()

def show_cursor():
    sys.stdout.write(CSI + "?25h"); sys.stdout.flush()

def render(lines):
    home(); sys.stdout.write("\n".join(lines)); sys.stdout.flush()
