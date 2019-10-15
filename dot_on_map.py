import math
from haversine import haversine, Unit

from person_class import Person


class DotOnMap:
    _EARTH_RADIUS = 6372795

    def __init__(self, latitude=0.0, longitude=0.0):
        """Object on map take coordinates type
        latitude = DD.DDDDD default 0.0
        longitude = DD.DDDDD default 0.0"""
        self._latitude = latitude
        self._longitude = longitude

    def get_lat(self) -> float:
        """широта точки"""
        return self._latitude

    def get_lon(self) -> float:
        """долгота точки"""
        return self._longitude

    def _convert_to_radian(self):
        # перевести координаты в радианы
        lat_r = math.radians(self._latitude)
        long_r = math.radians(self._longitude)
        return {'lat': lat_r, 'long': long_r}

    def distance_to_0(self) -> float:
        """растояние от точки до 0 координаты\n
        использует haversine"""
        return haversine((self.get_lat(), self.get_lon()), (0, 0))
        # radian_2 = self._convert_to_radian()
        # # косинусы, синусы и дельта
        # coslat1 = 1
        # coslat2 = math.cos(radian_2.get('lat'))
        # sinlat1 = 0
        # sinlat2 = math.sin(radian_2.get('lat'))
        # delta = self._longitude
        # cdelta = math.cos(radian_2.get('long'))
        # sdelta = math.sin(radian_2.get('long'))
        # # подстановка в большую формулу
        # up = math.sqrt(math.pow(coslat2 * sindelta, 2) + math.pow(coslat1 * sinlat2 - sinlat1 * coslat2 * cosdelta, 2))
        # down = sinlat1 * sinlat2 + coslat1 * coslat2 * cosdelta
        # arctang = math.atan2(up, down)
        # dist = arctang * self.EARTH_RADIUS
        # return dist

    def distance_to_point(self, point_2) -> float:
        """растояние между текущей точкой и точкой переданой в параметры\n
        принимает в параметры объект типа DotOnMap\n
        использует самописную реализацию"""
        # перевод грудусоп в радианы
        radian_1 = self._convert_to_radian()
        radian_2 = point_2._convert_to_radian()
        # косинусы, синусы и дельта
        coslat1 = math.cos(radian_1.get('lat'))
        coslat2 = math.cos(radian_2.get('lat'))
        sinlat1 = math.sin(radian_1.get('lat'))
        sinlat2 = math.sin(radian_2.get('lat'))
        delta = radian_2.get('long') - radian_1.get('long')
        cosdelta = math.cos(delta)
        sindelta = math.sin(delta)
        # подстановка в большую формулу
        up = math.sqrt(math.pow(coslat2 * sindelta, 2) + math.pow(coslat1 * sinlat2 - sinlat1 * coslat2 * cosdelta, 2))
        down = sinlat1 * sinlat2 + coslat1 * coslat2 * cosdelta
        arctang = math.atan2(up, down)
        dist = arctang * self._EARTH_RADIUS
        return dist

    def distance_to_point_2(self, point_2) -> float:
        """растояние между текущей точкой и точкой переданой в параметры\n
        принимает в параметры объект типа DotOnMap\n
        использует haversine библиотеку"""
        return haversine((self.get_lat(), self.get_lon()), (point_2.get_lat(), point_2.get_lon()), Unit.METERS)

    # мой метод считает вродибы тоже правильно но есть разбежность с методом из библиотеки
    # 392327.2230661257   - мой вариант
    # 392217.2595594006   - из haversine

    def coordinate_converter(self) -> str:
        """Выводит координаты точки в формате\n
            latitude DD°MM'SS" \n
            longitude DD°MM'SS\""""
        def convert(coord: float):
            coord_dd = int(coord // 1)
            coord_mm = int((coord - coord_dd) * 60 // 1)
            coord_ss = round(((coord - coord_dd) * 60 - coord_mm) * 60)
            return f'{coord_dd}°{coord_mm}\'{coord_ss}"'
        return f'latitude {convert(self.get_lat())}\n' \
               f'longitude {convert(self.get_lon())}'

    def __str__(self):
        return f'lat: {self.get_lat()}, long: {self.get_lon()}'


if __name__ == '__main__':
    dot_test = DotOnMap(45.7597, 4.8422)
    print(dot_test.coordinate_converter())
    dot_test_2 = DotOnMap(48.8567, 2.3508)
    print(dot_test_2)
    print(dot_test.distance_to_0())
    print(dot_test_2.distance_to_0())
    print(dot_test.distance_to_point(dot_test_2))
    print(dot_test.distance_to_point_2(dot_test_2))
