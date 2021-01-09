import math
import numbers
import operator


# oparte na Fraction https://github.com/python/cpython/blob/3.8/Lib/fractions.py

class Fraction:
    def __init__(self, numerator=0, denominator=0):
        self.numerator = int(numerator)
        self.denominator = int(denominator)

    def __str__(self):
        return "%d/%d" % (self.numerator, self.denominator)

    def __mul__(self, other):
        return Fraction(self.numerator * other.numerator,
                        self.denominator * other.denominator)

    __rmul__ = __mul__

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        return Fraction(self.numerator * other.denominator +
                        self.denominator * other.numerator,
                        self.denominator * other.denominator)

    __radd__ = __add__

    def __abs__(self):
        """abs(a)"""
        return Fraction(abs(self.numerator), self.denominator)

    def _operator_fallbacks(monomorphic_operator, fallback_operator):

        def forward(a, b):
            if isinstance(b, (int, Fraction)):
                return monomorphic_operator(a, b)
            elif isinstance(b, float):
                return fallback_operator(float(a), b)
            elif isinstance(b, complex):
                return fallback_operator(complex(a), b)
            else:
                return NotImplemented

        forward.__name__ = '__' + fallback_operator.__name__ + '__'
        forward.__doc__ = monomorphic_operator.__doc__

        def reverse(b, a):
            if isinstance(a, numbers.Rational):
                # Includes ints.
                return monomorphic_operator(a, b)
            elif isinstance(a, numbers.Real):
                return fallback_operator(float(a), float(b))
            elif isinstance(a, numbers.Complex):
                return fallback_operator(complex(a), complex(b))
            else:
                return NotImplemented

        reverse.__name__ = '__r' + fallback_operator.__name__ + '__'
        reverse.__doc__ = monomorphic_operator.__doc__

        return forward, reverse

    def _add(a, b):
        da, db = a.denominator, b.denominator
        Fraction(a.numerator * db + b.numerator * da, da * db)
        x = int(math.gcd(a.numerator, a.denominator))
        return Fraction(int(a.numerator // x), int(a.denominator // x))

    __add__, __radd__ = _operator_fallbacks(_add, operator.add)

    def _sub(a, b):
        da, db = a.denominator, b.denominator
        return Fraction(a.numerator * db - b.numerator * da,
                        da * db)

    __sub__, __rsub__ = _operator_fallbacks(_sub, operator.sub)

    def _mul(a, b):
        Fraction(a.numerator * b.numerator, a.denominator * b.denominator)
        x = int(math.gcd(a.numerator, a.denominator))
        return Fraction(int(a.numerator // x), int(a.denominator // x))

    __mul__, __rmul__ = _operator_fallbacks(_mul, operator.mul)

    def _div(a, b):
        return Fraction(a.numerator * b.denominator,
                        a.denominator * b.numerator)

    __truediv__, __rtruediv__ = _operator_fallbacks(_div, operator.truediv)

    def _floordiv(a, b):
        return (a.numerator * b.denominator) // (a.denominator * b.numerator)

    __floordiv__, __rfloordiv__ = _operator_fallbacks(_floordiv, operator.floordiv)

    def _divmod(a, b):
        da, db = a.denominator, b.denominator
        div, n_mod = divmod(a.numerator * db, da * b.numerator)
        return div, Fraction(n_mod, da * db)

    __divmod__, __rdivmod__ = _operator_fallbacks(_divmod, divmod)

    def _mod(a, b):
        da, db = a.denominator, b.denominator
        return Fraction((a.numerator * db) % (b.numerator * da), da * db)

    __mod__, __rmod__ = _operator_fallbacks(_mod, operator.mod)

    def __eq__(a, b):
        if type(b) is int:
            return a.numerator == b and a.denominator == 1
        if isinstance(b, numbers.Rational):
            return (a.numerator == b.numerator and
                    a.denominator == b.denominator)
        if isinstance(b, numbers.Complex) and b.imag == 0:
            b = b.real
        if isinstance(b, float):
            if math.isnan(b) or math.isinf(b):
                return 0.0 == b
            else:
                return a == a.from_float(b)
        else:
            return NotImplemented

    def _richcmp(self, other, op):
        return op(self.numerator * other.denominator,
                  self.denominator * other.numerator)

    def __lt__(a, b):
        """a < b"""
        return a._richcmp(b, operator.lt)

    def __gt__(a, b):
        """a > b"""
        return a._richcmp(b, operator.gt)

    def __le__(a, b):
        """a <= b"""
        return a._richcmp(b, operator.le)

    def __ge__(a, b):
        """a >= b"""
        return a._richcmp(b, operator.ge)
