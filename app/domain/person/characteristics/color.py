from webcolors import rgb_to_name, name_to_rgb


class RGBException(Exception):
    pass


class Color:
    def __init__(self, red: int = 0, green: int = 0, blue: int = 0) -> None:
        self._red = red
        self._green = green
        self._blue = blue

    @property
    def red(self) -> int:
        return self.red

    @red.setter
    def red(self, value: int) -> None:
        if self._validate_color_value(value):
            self._red = value

    @property
    def green(self) -> int:
        return self._green

    @green.setter
    def green(self, value: int) -> None:
        if self._validate_color_value(value):
            self._green = value

    @property
    def blue(self) -> int:
        return self._blue

    @blue.setter
    def blue(self, value: int) -> None:
        if self._validate_color_value(value):
            self._blue = value

    def _validate_color_value(self, value: int) -> bool:
        if not 0 < value <= 255:
            raise RGBException(
                f"the color value must be between 0 and 255. given {value}"
            )
        return True

    @property
    def rgb(self) -> tuple[int, int, int]:
        return (
            self._red,
            self._green,
            self._blue,
        )

    @property
    def name(self) -> str:
        return rgb_to_name(self.rgb)

    def __composite_values__(self) -> tuple[str]:
        return (self.name,)

    def __eq__(self, other: object) -> bool:
        return (
            isinstance(other, Color)
            and self._red == other._red
            and self._green == self._green
            and self._blue == self._blue
        )

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

    @classmethod
    def color_from_name(cls, color_name: str) -> "Color":
        red, green, blue = name_to_rgb(color_name)
        return Color(red=red, green=green, blue=blue)

    def __str__(self) -> str:
        return self.name
