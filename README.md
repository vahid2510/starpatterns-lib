# starpatterns

کتابخانه‌ای برای ساخت الگوهای متنی ستاره‌ای (ASCII) در ترمینال: مثلث، هرم، لوزی، الگوهای ماتریسی، فرکتال‌ها و حتی چند انیمیشن ANSI.

## نصب
```bash
pip install .
```
یا:
```bash
pipx run build && pip install dist/*.whl
```

## استفاده سریع
```python
from starpatterns import pyramid, diamond, draw, cross, anim_wave

pyramid(5)               # هرم مرکزی توپر
diamond(4, hollow=True)  # لوزی توخالی
draw(21, lambda i,j,n: j==i or j==n-1-i)  # ضربدر X
# anim_wave()            # انیمیشن موج (ANSI)
```

## مدل ریاضی
- الگوهای سطری با سه‌تایی `(s(i), w(i), fill)` ساخته می‌شوند. برای هرم: `s = n - i` و `w = 2i - 1`.
- الگوهای ماتریسی با شرط نقطه‌ای `f(i,j,n)` تعریف می‌شوند. مثال ضربدر: `f = (j==i) ∨ (j==n-1-i)`.
- برای ضخیم‌سازی مرز، فاصله تا مرز را `≤ k` بگیرید. برای تکسچر، شرط شکل را با ماسک `(i+j)%2` ترکیب کنید.

## ماژول‌ها
- `row_patterns.py`: مثلث/هرم/لوزی/ساعت‌شنی و مستطیل‌ها
- `grid_patterns.py`: کادر، قطرها، دایره/لوزی اقلیدسی/منهتنی، شطرنجی و...
- `fractals.py`: سیرپینسکی و دوستان
- `animations.py`: انیمیشن‌های متنی با ANSI
- `ansi.py`: کمکی‌های ANSI
- `__init__.py`: سطح API عمومی

## اجرای مثال‌ها
```bash
python -m starpatterns.examples.catalog
```

## تست
```bash
pytest -q
```

## مجوز
MIT
