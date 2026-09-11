import random

class ZeroGame:
    def __init__(self):
        self.user_finger = 0
        self.computer_finger = 0
        self.user_guess = 0
        self.total = 0


    def guess_choose(self):
        print('플레이 순서를 정합니다.')
        self.who=random.choice(['유저', '컴퓨터'])
        if self.who == '유저':
            print('유저가 먼저 추측합니다.')
        else:
            print('컴퓨터가 먼저 추측합니다.')

    def user_choice(self):
        self.user_finger = int(input("몇 개를 내시겠습니까? (0~2): "))

    def computer_choice(self):
        self.computer_finger = random.randint(0, 2)



    def user_guess_number(self):
        self.user_guess = int(input("총 손가락 개수를 예상하세요 (0~4): "))


    def computer_guess_number(self):
        self.computer_guess = random.randint(0, 4)
        print(f"컴퓨터는 {self.computer_guess}개라고 예상했습니다.")


    def calculate_total(self):
        self.total = self.user_finger + self.computer_finger


    def show_result(self):
        print()
        print(f"내 손가락: {self.user_finger}")
        print(f"컴퓨터 손가락: {self.computer_finger}")
        print(f"실제 총합: {self.total}")

        if self.user_guess == self.total:
            print("정답입니다!")
        else:
            print("틀렸습니다!")

    def play(self):
        print("=== 제로게임 시작 ===")

        while True:

            self.computer_choice()
            self.user_guess_number()
            self.calculate_total()
            self.show_result()


game = ZeroGame()
game.play()