from dataclasses import dataclass

@dataclass
class Camera():

    def __init__(
        self,
        focal_length: float,
        width: int,
        height: int,
        rotation_deg: int = 0
    ):
        self.focal_length = focal_length
        self.width = width
        self.height = height
        self.rotation_deg = rotation_deg

    def obtain_measurements_text(cls):
        default_width = int(input("Camera Width (mm): "))
        default_height = int(input("Camera Height (mm): "))
        default_focal_length = float(input("Focal Length (mm): "))

        return cls(
            width = default_width,
            height = default_height,
            focal_length = default_focal_length
        )

