import random


class ZeroGame:
    def __init__(self):
        self.user_finger = 0
        self.computer_finger = 0
        self.user_guess = 0
        self.total = 0
        self.result = ""


    # 유저 손가락 선택
    def user_choice(self):
        self.user_finger = int(input("몇 개를 내시겠습니까? (0~2): "))


    # 컴퓨터 손가락 선택
    def computer_choice(self):
        self.computer_finger = random.randint(0, 2)


    # 유저가 총합 예상
    def user_guess_number(self):
        self.user_guess = int(input("총 손가락 개수를 예상하세요 (0~4): "))


    # 실제 총합 계산
    def calculate_total(self):
        self.total = self.user_finger + self.computer_finger


    # 결과 판정
    def check_result(self):
        
        if self.user_guess == self.total:
            self.result = "승"
            print("정답입니다! 유저가 이겼습니다.")
        else:
            self.result = "패"
            print("오답입니다. 유저가 졌습니다.")


    # txt 저장
    def save_result(self, nickname):
        with open("zerogame.txt", "a", encoding="utf-8") as file:
            file.write(f"({nickname},{self.result})\n")


    # 게임 실행
    def play(self):
        print("=== 제로게임 시작 ===")

        self.user_choice()
        self.computer_choice()
        self.user_guess_number()
        self.calculate_total()

        print()
        print(f"내 손가락: {self.user_finger}")
        print(f"컴퓨터 손가락: {self.computer_finger}")
        print(f"실제 총합: {self.total}")

        self.check_result()

        nickname = input("닉네임을 입력하세요: ")

        self.save_result(nickname)

        print(f"{nickname},{self.result} 결과가 저장되었습니다.")


game = ZeroGame()
game.play()