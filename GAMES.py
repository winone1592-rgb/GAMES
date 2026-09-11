from dice_game import DiceGame
from rock_game import RockPaperScissors
from zerogame import ZeroGame
from coinmatchgame import CoinMatchGame


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


# 전체 프로그램
class App:

    def __init__(self):

        # 로그인
        self.login_manager = LoginManager("admin", "1234")

        # 게임 객체
        self.dice_game = DiceGame()
        self.rock_game = RockPaperScissors()
        self.zero_game = ZeroGame()
        self.coin_game = CoinMatchGame()


    # 전체 메뉴 출력
    def print_menu(self):

        print()
        print("===== 게임 프로그램 =====")
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


    # 가위바위보 메뉴
    def rock_menu(self):

        while True:

            print()
            print("===== 가위바위보 게임 =====")
            print("1. 가위바위보 게임 시작")
            print("2. 가위바위보 게임 기록보기")
            print("3. 뒤로가기")

            choose = input("메뉴를 선택해주세요: ")

            if choose == "1":

                result = self.rock_game.play()

                nickname = input("닉네임을 입력하세요: ").strip()

                self.rock_game.save_result(nickname, result)

                print("결과가 rock_paper_scissors_result.txt 에 저장되었습니다.")

            elif choose == "2":

                self.rock_game.show_result()

            elif choose == "3":

                break

            else:

                print("잘못된 메뉴선택입니다.")


    # 제로 게임 메뉴
    def zero_menu(self):

        while True:

            print()
            print("===== 제로 게임 =====")
            print("1. 제로게임 시작")
            print("2. 제로게임 기록보기")
            print("3. 뒤로가기")

            choose = input("메뉴를 선택해주세요: ")

            if choose == "1":

                self.zero_game.play()

            elif choose == "2":

                try:
                    with open("zerogame.txt", "r", encoding="utf-8") as file:

                        print()
                        print("===== 제로게임 기록 =====")
                        print(file.read())

                except FileNotFoundError:

                    print("저장된 기록이 없습니다.")

            elif choose == "3":

                break

            else:

                print("잘못된 메뉴선택입니다.")


    # 동전던지기 메뉴
    def coin_menu(self):

        while True:

            print()
            print("===== 동전던지기 게임 =====")
            print("1. 동전던지기 게임 시작")
            print("2. 동전던지기 게임 기록보기")
            print("3. 뒤로가기")

            choose = input("메뉴를 선택해주세요: ")

            if choose == "1":

                self.coin_game.run()

            elif choose == "2":

                try:
                    with open("coin_match_result.txt", "r", encoding="utf-8") as file:

                        print()
                        print("===== 동전던지기 게임 기록 =====")
                        print(file.read())

                except FileNotFoundError:

                    print("저장된 기록이 없습니다.")

            elif choose == "3":

                break

            else:

                print("잘못된 메뉴선택입니다.")


    # 주사위 메뉴
    def dice_menu(self):

        while True:

            print()
            print("===== 주사위 게임 =====")
            print("1. 주사위 게임 시작")
            print("2. 주사위 게임 기록보기")
            print("3. 뒤로가기")

            choose = input("메뉴를 선택해주세요: ")

            if choose == "1":

                self.dice_game.play()

            elif choose == "2":

                self.dice_game.show_history()

            elif choose == "3":

                break

            else:

                print("잘못된 메뉴선택입니다.")


    # 프로그램 실행
    def run(self):

        # 로그인
        if not self.login_manager.login():
            return

        # 로그인 성공 후 전체 메뉴
        while True:

            self.print_menu()

            menu = self.input_menu()

            # 1. 가위바위보
            if menu == 1:

                self.rock_menu()

            # 2. 제로
            elif menu == 2:

                self.zero_menu()

            # 3. 동전
            elif menu == 3:

                self.coin_menu()

            # 4. 주사위
            elif menu == 4:

                self.dice_menu()

            # 5. 종료
            elif menu == 5:

                print("프로그램을 종료합니다.")
                break

            else:

                print("잘못된 메뉴입니다.")


# 프로그램 시작
app = App()
app.run()