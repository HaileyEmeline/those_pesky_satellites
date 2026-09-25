from dataclasses import dataclass

@dataclass
class FieldOfView():
    def __init__(
            self,
            width_deg: float,
            height_deg: float,
            rotation_deg: float = 0.0
    ):
        self.width_deg = width_deg
        self.height_deg = height_deg
        self.rotation_deg = rotation_deg

    def obtain_fov(cls):
        width = float(input("Width in degrees: "))
        height = float(input("Height in degrees: "))
        rotation = float(input("If known, degree of rotation: "))

        return cls(
            width_deg = width,
            height_deg = height,
            rotation_deg = rotation
        )

    