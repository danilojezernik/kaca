from src.app.console import Console

console = Console(sirina=10, visina=10)

while not console.svet.konec():
    console.narisi()
    console.input()

