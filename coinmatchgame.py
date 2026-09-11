import random
 
 
class CoinMatchGame:
    """동전 앞뒤 맞추기 게임 (간단 버전)"""
 
    SIDES = ["앞면", "뒷면"]
 
    def play(self, guess: str) -> str:
        """동전을 던져 예측이 맞았는지 '성공'/'실패'로 반환"""
        result = random.choice(self.SIDES)
        return "성공" if guess == result else "실패"
 
    def save_result(self, nickname: str, result: str, filepath: str = "coin_match_result.txt"):
        """(닉네임, 결과)를 텍스트 파일에 한 줄씩 누적 저장"""
        with open(filepath, "a", encoding="utf-8") as f:
            f.write(f"{(nickname, result)}\n")
 
    def run(self):
        """게임 진행 -> 닉네임 입력 -> 결과 저장까지 한 번에 수행"""
        guess = input("앞면 또는 뒷면을 선택하세요: ").strip()
        result = self.play(guess)
        print(f"결과: {result}")
 
        nickname = input("닉네임을 입력하세요: ").strip()
        self.save_result(nickname, result)
        print("결과가 coin_match_result.txt 에 저장되었습니다.")