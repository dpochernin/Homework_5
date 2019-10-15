def is_year_leap(y: int):
    try:
        int(y)
    except TypeError(f'ERROR {y} is not year'):
        return None
    if y == 0:
        raise ValueError(f'Year can not be 0')
    if (y % 4) or (not (y % 100) and (y % 400)):
        return False
    else:
        return True


def triangle_possible(a: float, b: float, c: float) -> bool:
    abc = [a, b, c]
    abc.sort()
    if (abc[0] + abc[1]) > abc[2]:
        return True
    else:
        return False


def triangle_type(a: float, b: float, c: float) -> str:
    if triangle_possible(a, b, c):
        if a == b == c:
            return 'Equilateral triangle'
        elif a == b or b == c:
            return 'Isosceles triangle'
        else:
            return 'Versatile triangle'
    else:
        return 'Not a triangle'
