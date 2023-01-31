import random

from src.domain.hrana import Hrana
from src.domain.kaca import Kaca


class Svet:
    def __init__(self, sirina: int, visina: int):  # magic methods
        self.sirina: int = sirina
        self.visina: int = visina
        self.kaca = Kaca(x_glave=sirina // 2, y_glave=visina // 2)
        self.hrana = Hrana(x=random.randint(0, sirina), y=random.randint(0, visina))

    def konec(self) -> bool:
        if 0 <= self.kaca.deli[0].x <= self.sirina and 0 <= self.kaca.deli[0].y <= self.visina:
            return False
        else:
            return True