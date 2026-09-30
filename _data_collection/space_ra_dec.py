from dataclasses import dataclass

@dataclass
class Position():
    def __init__(
            self,
            ra: float,
            dec: float,
    ):
        self.ra = ra
        self.dec = dec

    def obtain_pos(cls):
        _ra = float(input("Camera Right Ascension: "))
        _dec = float(input("Camera Declination: "))

        return cls(
            ra = _ra,
            dec = _dec,
        )

    