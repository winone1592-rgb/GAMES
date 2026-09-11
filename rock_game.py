# 가위바위보 게임
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
            result = "무승부"
            print("무승부입니다.")

        elif user == "가위" and computer == "보":
            result = "승리"
            print("이겼습니다.")

        elif user == "바위" and computer == "가위":
            result = "승리"
            print("이겼습니다.")

        elif user == "보" and computer == "바위":
            result = "승리"
            print("이겼습니다.")

        else:
            result = "패배"
            print("졌습니다.")

        return result

    def save_result(self, nickname, result):
        with open("rock_paper_scissors_result.txt", "a", encoding="utf-8") as file:
            file.write(nickname + " " + result + "\n")

    def show_result(self):
        try:
            with open("rock_paper_scissors_result.txt", "r", encoding="utf-8") as file:
                print()
                print("===== 가위바위보 게임 기록 =====")
                print(file.read())
        except FileNotFoundError:
            print("저장된 기록이 없습니다.")
