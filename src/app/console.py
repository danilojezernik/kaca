from src.domain.svet import Svet


class Console:
    def __init__(self, sirina: int, visina: int):
        self.svet = Svet(sirina=sirina, visina=visina)
        self.sirina = sirina
        self.visina = visina

    def narisi(self):
        for y in range(self.visina):
            for x in range(self.sirina):

                simbol = '.'
                for del_kace in self.svet.kaca.deli:
                    if del_kace.x == x and del_kace.y == y:
                        simbol = 'X'

                if self.svet.hrana.x == x and self.svet.hrana.y == y:
                    simbol = 'o'

                print(simbol + ' ', end="")
            print()

    def input(self):
        dx = int(input("Vnesi delta x:"))
        dy = int(input("Vnesi delta y:"))
        self.svet.kaca.premik(dx=dx, dy=dy)