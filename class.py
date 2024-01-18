#클래스 사용법 복습

from tool import clear_screen
from time import sleep

#전사 직군
class Warrior:
    def __init__(self,hp,damage):
        self.hp = hp
        self.damage = damage

    def hit(self):
        print("때치!")
#궁수 직군
class Archer:
    def __init__(self,hp,damage):
        self.hp = hp
        self.damage = damage    
    
    def hit(self):
        print("쇽!")

#마법사 직군
class Magician:
    def __init__(self,hp,damage):
        self.hp = hp
        self.damage = damage    
    
    def hit(self):
        print("얍!")



if __name__ == "__main__":
    seungmin = Magician(5000,150) #인스턴스 생성
    soldier = Archer(500,10)
    
    while (seungmin.hp > 0):  
        print(f"seungmin's hp = {seungmin.hp}")  
        print(f"soldier's hp = {soldier.hp}")
        seungmin.hit()
        soldier.hp -= seungmin.damage
        sleep(1)

        if soldier.hp > 0:
            clear_screen()
        else:
            clear_screen()
            print("fallen soldier")
            break

