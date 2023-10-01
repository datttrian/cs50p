import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("1/2") == 50
    assert convert("99/100") == 99
    assert convert("1/100") == 1


def test_gauge():
    assert gauge(50) == "50%"def main():
    frac = input("Fraction: ")
    pct = convert(frac)
    print(gauge(pct))


def convert(fraction):
    x, y = fraction.split("/")
    if int(x)/int(y) > 1:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    return int(int(x)/int(y) * 100)


def gauge(percentage):
    try:
        if 0 <= percentage <= 1:
            return "E"
        elif 99 <= percentage <= 100:
            return "F"
        elif 1 < percentage < 99:
            return f"{int(percentage)}%"
        else:
            raise TypeError
    except TypeError:
        pass


if __name__ == "__main__":
    main()
    assert gauge(99) == "F"
    assert gauge(1) == "E"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("2/1")