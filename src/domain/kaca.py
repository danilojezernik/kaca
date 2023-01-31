from src.domain.del_kace import DelKace


class Kaca:
    def __init__(self, x_glave: int, y_glave: int):
        self.deli: list[DelKace] = []
        for i in range(3):
            del_kace = DelKace(x=x_glave + i, y=y_glave)
            self.deli.append(del_kace)

    def premik(self, dx: int, dy: int):
        stari_x = self.deli[0].x
        stari_y = self.deli[0].y
        self.deli[0].x += dx
        self.deli[0].y += dy

        for i in range(1, len(self.deli)):
            sx = self.deli[i].x
            sy = self.deli[i].y
            self.deli[i].x = stari_x
            self.deli[i].y = stari_y
            stari_x = sx
            stari_y = sy