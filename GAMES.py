import random


# 로그인 관련
class LoginManager:
    def __init__(self, correct_id, correct_pw, max_attempts=3):
        self.correct_id = correct_id
        self.correct_pw = correct_pw
        self.max_attempts = max_attempts

    def login(self):
        for count in range(self.max_attempts):
            user_id = input("ID를 입력하세요: ")
            user_pw = input("PASSWORD를 입력하세요: ")

            if user_id == self.correct_id and user_pw == self.correct_pw:
                print("로그인 되었습니다.")
                return True
            else:
                print("아이디 또는 비밀번호가 틀렸습니다.")

        print("로그인 3회 실패로 프로그램을 종료합니다.")
        return False


# 가위바위보 게임
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


# 전체 프로그램
class App:

    def __init__(self):
        self.login_manager = LoginManager("admin", "1234")

    # 메인 메뉴
    def print_menu(self):
        print()
        print("1. 가위바위보 게임")
        print("2. 제로 게임")
        print("3. 동전던지기 게임")
        print("4. 주사위 게임")
        print("5. 게임 종료")

    # 메뉴 입력
    def input_menu(self):
        while True:
            try:
                menu = int(input("메뉴를 선택하세요: "))
                return menu

            except ValueError:
                print("숫자만 입력해주세요.")

    # 프로그램 실행
    def run(self):

        if not self.login_manager.login():
            return

        while True:

            self.print_menu()
            menu = self.input_menu()

            # 1. 가위바위보 게임
            if menu == 1:
                print()
                print("===== 가위바위보 게임 =====")
                print("1. 가위바위보 게임 시작")
                print("2. 가위바위보 게임 기록보기")
                print("3. 뒤로가기")

                choose = input("메뉴를 선택해주세요: ")

                if choose == "1":

                    game = RockPaperScissors()

                    result = game.play()

                    nickname = input("닉네임을 입력하세요: ").strip()

                    game.save_result(nickname, result)

                    print("결과가 rock_paper_scissors_result.txt 에 저장되었습니다.")

                elif choose == "2":

                    game = RockPaperScissors()
                    game.show_result()

                elif choose == "3":
                    continue

                else:
                    print("잘못된 메뉴선택입니다.")

            # 2. 제로 게임
            elif menu == 2:
                print()
                print("===== 제로 게임 =====")
                print("1. 제로게임 시작")
                print("2. 제로게임 기록보기")
                print("3. 뒤로가기")

                choose = input("메뉴를 선택해주세요: ")

                if choose == "1":
                    pass

                elif choose == "2":
                    pass

                elif choose == "3":
                    continue

                else:
                    print("잘못된 메뉴선택입니다.")

            # 3. 동전던지기 게임
            elif menu == 3:
                print()
                print("===== 동전던지기 게임 =====")
                print("1. 동전던지기 게임 시작")
                print("2. 동전던지기 게임 기록보기")
                print("3. 뒤로가기")

                choose = input("메뉴를 선택해주세요: ")

                if choose == "1":
                    pass

                elif choose == "2":
                    pass

                elif choose == "3":
                    continue

                else:
                    print("잘못된 메뉴선택입니다.")

            # 4. 주사위 게임
            elif menu == 4:
                print()
                print("===== 주사위 게임 =====")
                print("1. 주사위 게임 시작")
                print("2. 주사위 게임 기록보기")
                print("3. 뒤로가기")

                choose = input("메뉴를 선택해주세요: ")

                if choose == "1":
                    pass

                elif choose == "2":
                    pass

                elif choose == "3":
                    continue

                else:
                    print("잘못된 메뉴선택입니다.")

            # 5. 프로그램 종료
            elif menu == 5:
                print("프로그램을 종료합니다.")
                break

            else:
                print("잘못된 메뉴입니다.")


app = App()
app.run()