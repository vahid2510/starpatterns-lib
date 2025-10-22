from starpatterns import (
    pyramid, pyramid_inv, diamond, hourglass, tri_left, tri_right, rect, twin_pyramids,
    draw, border, plus, cross, chess, circle_border, circle_fill, diamond_border, diamond_fill, letter_A,
    sierpinski_bit
)

print("\n== Row patterns ==")
tri_left(6); print()
tri_right(6); print()
pyramid(6); print()
pyramid(6, hollow=True); print()
diamond(5); print()
hourglass(5, hollow=True); print()
rect(4, 12); print()
rect(5, 16, hollow=True); print()
twin_pyramids(6); print()

print("\n== Grid patterns ==")
cross(21); print()
plus(21); print()
border(21); print()
chess(16); print()
circle_border(25, 10); print()
circle_fill(21, 9); print()
diamond_border(21, 10); print()
diamond_fill(21, 10); print()
letter_A(21); print()

print("\n== Fractals ==")
sierpinski_bit(32)
