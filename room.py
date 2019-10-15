class Room:
    def __init__(self, side_a=0.0, side_b=0.0):
        """"""
        if side_a > 0:
            self._side_a = side_a
        else:
            raise ValueError(f'side_a={side_a}, can not be 0 or less')
        if side_b > 0:
            self._side_b = side_b
        else:
            raise ValueError(f'side_b={side_b}, can not be 0 or less')

    def room_square(self) -> float:
        return self._side_a * self._side_b

    def room_perimeter(self) -> float:
        return (self._side_b + self._side_a) * 2

    def __str__(self):
        return f'a={self._side_a}, b={self._side_a}'
