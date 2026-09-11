import random


class ZeroGame:
    def __init__(self):
        self.user_finger = 0
        self.computer_finger = 0
        self.user_guess = 0
        self.computer_guess = 0
        self.total = 0
        self.who = ""
        self.count = 0
        self.result = []


    # 처음 추측할 사람 정하기
    def guess_choose(self):
        print("플레이 순서를 정합니다.")
    

        self.who = random.choice(["유저", "컴퓨터"])

        if self.who == "유저":
            print("유저가 먼저 추측합니다.")
        else:
            print("컴퓨터가 먼저 추측합니다.")
        print('한 번씩 번갈아 가며 추측합니다.')


    # 유저 손가락 선택
    def user_choice(self):
        self.user_finger = int(input("몇 개를 내시겠습니까? (0~2): "))


    # 컴퓨터 손가락 선택
    def computer_choice(self):
        self.computer_finger = random.randint(0, 2)

    # 유저가 총합 예상
    def user_guess_number(self):
        self.user_guess = int(input("총 손가락 개수를 예상하세요 (0~4): "))


    # 컴퓨터가 총합 예상
    def computer_guess_number(self):
        self.computer_guess = random.randint(0, 4)
        print(f"컴퓨터는 {self.computer_guess}개라고 예상했습니다.")


    # 실제 손가락 총합 계산
    def calculate_total(self):
        self.total = self.user_finger + self.computer_finger


    # 게임 실행
    def play(self):
        print("=== 제로게임 시작 ===")

        self.guess_choose()

        while True:

            print()
            print("-------------------")

            # 둘 다 손가락 내기
            self.user_choice()
            self.computer_choice()

            # 실제 총합 계산
            self.calculate_total()

            # 유저 차례
            if self.who == "유저":

                self.count += 1

                self.user_guess_number()

                print(f"내 손가락: {self.user_finger}")
                print(f"컴퓨터 손가락: {self.computer_finger}")
                print(f"실제 총합: {self.total}")

                if self.user_guess == self.total:
                    print("정답입니다!")
                    print(f"{self.count}번 만에 맞혔습니다.")

                    nickname = input("닉네임을 입력하세요: ")

                    self.result.append((nickname, self.count))

                    print("게임 결과:", self.result)

                    break

                else:
                    print("틀렸습니다!")

                    self.who = "컴퓨터"


            # 컴퓨터 차례
            else:

                self.computer_guess_number()

                print(f"내 손가락: {self.user_finger}")
                print(f"컴퓨터 손가락: {self.computer_finger}")
                print(f"실제 총합: {self.total}")

                if self.computer_guess == self.total:
                    print("컴퓨터가 맞혔습니다!")

                else:
                    print("컴퓨터가 틀렸습니다!")

                self.who = "유저"


game = ZeroGame()
game.play()