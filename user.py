from dataclasses import dataclass

@dataclass
class User():
    id: int
    username: str = ''
    balance: float = 0.0
    consumed: float = 0.0
    paid: float = 0.0

    def calculate_debt(self,itemprice):
        self.balance = self.balance - itemprice
        self.consumed = self.consumed + itemprice
