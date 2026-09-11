# 각자의 게임을 클래스화 하는거에요!
import random

class DiceGame:

    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.draw_score = 0
        self.filename = "dice_history.txt"

    def roll_dice(self):
        return random.randint(1, 6)

    def save_result(self, nickname, result):
        with open(self.filename, "a", encoding="utf-8") as file:
            file.write(f"{nickname},{result}\n")
        print(f"\n[안내] {nickname}님의 게임 결과({result})가 '{self.filename}'에 저장되었습니다.")

    def show_history(self):
        print("\n--- 🎲 주사위 게임 누적 결과 이력 ---")
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                for line in file:
                    parts = line.strip().split(',')
                    if len(parts) == 2:
                        print(f"👤 닉네임: {parts[0]} | 🏆 결과: {parts[1]}")
        except FileNotFoundError:
            print("아직 저장된 결과가 없습니다. 첫 게임의 주인공이 되어보세요!")
        print("--------------------------------------\n")

    def play(self):
        print()
        print("====================")
        print("      주사위 게임")
        print("====================")

        while True:
            print("1. 주사위 던지기")
            print("2. 게임 취소(종료)")
            choice = input("선택해주세요 (1 또는 2): ")

            if choice == '1':
                break 
            elif choice == '2':
                print("\n주사위 게임을 취소하고 메뉴로 돌아갑니다.")
                return (None, "취소")  
            else:
                print("\n⚠️ 잘못된 입력입니다. 숫자 1 또는 2만 입력해주세요.\n")
        # -----------------------------

        player_dice = self.roll_dice()
        computer_dice = self.roll_dice()

        print()
        print("플레이어 주사위 :", player_dice)
        print("컴퓨터 주사위 :", computer_dice)

        if player_dice > computer_dice:
            print()
            print("🎉 성공!")
            self.player_score += 1
            result = "성공"

        elif player_dice < computer_dice:
            print()
            print("💥 실패!")
            self.computer_score += 1
            result = "실패"

        else:
            print()
            print("🤝 무승부입니다.")
            self.draw_score += 1
            result = "무승부"

        print()
        nickname = input("닉네임을 입력하세요: ")
        
        self.save_result(nickname, result)
        
        self.show_history()

        return (nickname, result)

if __name__ == "__main__":
    game = DiceGame() 
    
    while True:
        result = game.play() 
        
        if result == (None, "취소"):
            break

        retry = input("\n다시 하시겠습니까? (y/n): ")
        if retry.lower() != 'y':
            print("\n주사위 게임을 완전히 종료합니다.")
            break