# 각자의 게임을 클래스화 하는거에요!
import random


class RockPaperScissors:

    def __init__(self):
        self.choices = ["가위", "바위", "보"]

    def play(self):
        num = random.randint(0, 2)
        computer = self.choices[num]

        user = input("가위, 바위, 보 중 하나를 입력하세요: ")

        print("컴퓨터:", computer)

        if user == computer:
            print("무승부입니다.")

        elif user == "가위" and computer == "보":
            print("이겼습니다.")

        elif user == "바위" and computer == "가위":
            print("이겼습니다.")

        elif user == "보" and computer == "바위":
            print("이겼습니다.")

        else:
            print("졌습니다.")


game = RockPaperScissors()
game.play() 