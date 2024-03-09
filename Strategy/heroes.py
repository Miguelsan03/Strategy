class Iattack():
    def attack(self):
        pass
class Idefend():
    def defend(self):
        pass
class Imovement():
    def movement(self):
        pass

class High_atck(Iattack):
    def attack(self):
        print("Tengo 10 puntos de ataque")
        return 10
class Med_atck(Iattack):
    def attack(self):
        print("Tengo 5 puntos de ataque")
        return 5
class Low_atck(Iattack):
    def attack(self):
        print("Tengo 2 puntos de ataque")
        return 2
    
class High_def(Idefend):
    def attack(self):
        print("Tengo 10 puntos de defensa")
        return 10
class Med_def(Idefend):
    def attack(self):
        print("Tengo 5 puntos de defensa")
        return 5
class Low_def(Idefend):
    def attack(self):
        print("Tengo 2 puntos de defensa")
        return 2
    
class High_mov(Imovement):
    def attack(self):
        print("Tengo 7 casillas de movimiento")
        return 10
class Med_mov(Imovement):
    def attack(self):
        print("Tengo 4 casillas de movimiento")
        return 5
class Low_mov(Imovement):
    def attack(self):
        print("Tengo 2 casillas de movimiento")
        return 2
    
class Hero:
    def __init__(self, attack:Iattack, defense:Idefend, movement:Imovement) -> None:
        pass
    def roar():
        pass
class magician(Hero):
    def __init__(self, attack: Iattack, defense: Idefend, movement: Imovement) -> None:
        super().__init__(Med_atck, Low_def, High_mov)
    def roar(self):
        print("I'm a magician!")
class soldier(Hero):
    def __init__(self, attack: Iattack, defense: Idefend, movement: Imovement) -> None:
        super().__init__(Low_atck, Med_def, Med_mov)
    def roar(self):
        print("I'm a soldier!")
class archer(Hero):
    def __init__(self, attack: Iattack, defense: Idefend, movement: Imovement) -> None:
        super().__init__(High_atck, Low_def, Low_mov)
    def roar(self):
        print("I'm an archer!")
    
    
