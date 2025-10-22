# starpatterns

A **Python library** for generating advanced **ASCII star patterns**, **fractal geometries**, and **ANSI text animations** right inside the terminal.

Author: **Vahid Ahmadi Khorami**
License: **MIT License**
Version: **0.1.0**
Repository: [https://github.com/vahid2510/starpatterns-lib](https://github.com/vahid2510/starpatterns-lib)

---

## 🌟 Overview

`starpatterns` is a creative Python toolkit designed for programmers, educators, and enthusiasts who love visual mathematics, ASCII art, and algorithmic design. It allows users to print geometric shapes and patterns directly in the terminal using simple mathematical rules and Python functions.

From classic **pyramids and diamonds** to intricate **fractal models** and **animated waves**, this library offers both elegance and educational value. Each function corresponds to a mathematical model, making it suitable for both art and teaching algorithmic geometry.

---

## ✨ Key Features

* 🧩 **Row-based patterns**: triangles, pyramids, diamonds, hourglasses, rectangles, twin pyramids.
* 🧮 **Matrix-based patterns**: borders, crosses, plus signs, chessboards, circles (Euclidean and Manhattan), and text-based shapes.
* 🌀 **Fractals**: bitwise Sierpinski triangle and recursive geometric structures.
* 🎞️ **Animations**: wave motion and bouncing ball rendered with ANSI cursor control.
* 📐 **Mathematical modeling** for each pattern — easy to extend and customize.

---

## 📦 Installation

### Option 1 — Local installation

```bash
git clone https://github.com/vahid2510/starpatterns-lib.git
cd starpatterns-lib
pip install .
```

### Option 2 — Build wheel manually

```bash
pip install build
python -m build
pip install dist/*.whl
```

### Option 3 — Developer mode

```bash
pip install -e .
```

---

## 🚀 Quick Start

```python
from starpatterns import pyramid, diamond, cross, anim_wave

# Basic static patterns
pyramid(5)                # Solid pyramid
pyramid(5, hollow=True)   # Hollow pyramid
diamond(4, hollow=True)   # Hollow diamond
cross(15)                 # Cross shape

# Animated examples (press Ctrl+C to stop)
# anim_wave()             # Sine wave animation
```

---

## 🧠 Mathematical Theory

Every ASCII pattern is derived from a mathematical model expressed by **functions of line index** or **grid coordinates**.

| Category         | Model                                                                | Description                                     |
| ---------------- | -------------------------------------------------------------------- | ----------------------------------------------- |
| **Row-based**    | `s(i)` = number of leading spaces, `w(i)` = number of stars per line | e.g. Pyramid → `s = n - i`, `w = 2i - 1`        |
| **Matrix-based** | `f(i, j, n)` = Boolean condition defining filled cells               | e.g. Cross → `f = (j == i) or (j == n - 1 - i)` |
| **Fractal**      | Recursive or bitwise self-similarity function                        | e.g. Sierpinski → print `*` if `(i & j) == 0`   |

### Extensions

* For **hollow** shapes, restrict filled points to boundary conditions.
* For **textures**, add periodic masks: `(i + j) % 2 == 0`.
* For **animated forms**, transform index coordinates by time: `(i, j, t)`.

---

## 🧩 Module Structure

| Module                | Description                                                                             |
| --------------------- | --------------------------------------------------------------------------------------- |
| `ansi.py`             | Handles cursor control, screen clearing, and rendering via ANSI escape sequences.       |
| `row_patterns.py`     | Line-based geometric patterns (triangles, pyramids, diamonds, hourglasses, rectangles). |
| `grid_patterns.py`    | Matrix-based shapes (borders, crosses, circles, chessboards, letters).                  |
| `fractals.py`         | Bitwise or recursive fractal generators.                                                |
| `animations.py`       | Wave and bouncing ball terminal animations.                                             |
| `examples/catalog.py` | Demonstrates over 200 sample outputs.                                                   |
| `tests/test_basic.py` | Unit tests using `pytest`.                                                              |

---

## 📘 Usage Examples

### 1. Row Patterns

```python
from starpatterns import pyramid, diamond, hourglass

pyramid(6)
pyramid(6, hollow=True)
diamond(5, hollow=True)
hourglass(5)
```

### 2. Matrix Patterns

```python
from starpatterns import cross, border, plus, chess, letter_A

cross(15)
border(15, k=1)
plus(15)
chess(12)
letter_A(21)
```

### 3. Fractals

```python
from starpatterns import sierpinski_bit
sierpinski_bit(32)
```

### 4. Animations

```python
from starpatterns import anim_wave, anim_bounce
anim_wave()      # Sine wave motion
anim_bounce()    # Bouncing ball in box
```

---

## 🧪 Testing

The project includes simple test coverage with **pytest**:

```bash
pytest -q
```

Expected output:

```
..                                                               [100%]
2 passed in 0.10s
```

---

## ⚙️ Continuous Integration (CI)

This repository includes a **GitHub Actions** workflow (`.github/workflows/ci.yml`) that automatically runs all tests under Python 3.11 for every push or pull request.

---

## 📚 License

**MIT License** — Copyright © 2025 **Vahid Ahmadi Khorami**.

Permission is granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction, including use, modification, and distribution.

---

## 🌈 Future Plans

* Add recursive fractal trees and L-systems.
* Implement ANSI color support for multicolor patterns.
* Provide CLI tools for real-time pattern generation.
* Add parameterized pattern templates for classroom visualization.

---

## 💬 Contact

**Author:** Vahid Ahmadi Khorami
**GitHub:** [@vahid2510](https://github.com/vahid2510)


---

### ⭐ If you like this project, give it a star on GitHub!
