import os
from PIL import Image


#전사 직업군
class knight:
    def __init__(self) -> None:
        pass
    def hit(self):
        print("아주 세게 떄렸음 ㅇㅇ")

#궁수 직업군
class archer:
    def __init__(self) -> None:
        pass
    def hit(Self):
        print("따끔했다.")        

class Monster:
    def __init__(self,hp):
        self.hp = hp



#파댕이 소환술
def image():
    imag1 = Image.open("test\OIP.jpeg")
    imag1.show()
    return 0

#화면 지우기
def clear_screen(job,floor):
    os.system('cls')
    if job != 0:
        print(f"당신의 직업:{job}")
        print(f"현재 층수:{floor}\n\n\n\n\n")
    return 0

