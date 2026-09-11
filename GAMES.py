# 각자의 게임을 클래스화 하는거에요!
"""
동전 앞뒤 맞추기 게임 (1인용)
- 컴퓨터가 동전을 던지고, 플레이어가 앞면/뒷면을 맞추는 게임
- 다른 게임 클래스들과 합치기 쉽도록 독립적으로 구성
"""

import random


class CoinMatchGame:

    HEADS = "앞면"
    TAILS = "뒷면"
    SIDES = [HEADS, TAILS]

    def __init__(self, player_name):
        self.player_name = player_name
        self.reset()

    def reset(self):
        """점수 및 기록 초기화"""
        self.score = 0
        self.total_rounds = 0
        self.history = [] 

    def flip_coin(self) -> str:
        """동전을 무작위로 던짐"""
        return random.choice(self.SIDES)

    def play_round(self, guess: str) -> dict:
        """
        한 라운드 진행
        guess: "앞면"/"뒷면", "H"/"T", "앞"/"뒤" 등 자유롭게 입력 가능
        return: {"round":.., "guess":.., "result":.., "correct": bool, "score":..}
        """
        guess = self._normalize(guess)
        if guess not in self.SIDES:
            raise ValueError(f"'{guess}'는 올바른 선택이 아닙니다. {self.SIDES} 중 하나를 입력하세요.")

        result = self.flip_coin()
        correct = guess == result

        self.total_rounds += 1
        if correct:
            self.score += 1

        round_data = {
            "round": self.total_rounds,
            "guess": guess,
            "result": result,
            "correct": correct,
            "score": self.score,
        }
        self.history.append(round_data)
        return round_data

    @staticmethod
    def _normalize(guess: str) -> str:
        """앞/뒤, H/T, 앞면/뒷면 등 다양한 입력을 표준 형태로 변환"""
        g = guess.strip().lower()
        if g in ["앞", "앞면", "h", "head", "heads"]:
            return CoinMatchGame.HEADS
        if g in ["뒤", "뒷면", "t", "tail", "tails"]:
            return CoinMatchGame.TAILS
        return guess  # 매칭 안 되면 원본 반환 -> 위에서 에러 처리됨
