class monster:

    def __init__(self, hp: int, ap: int):
        self.hit_point = hp
        self.attack_point = ap
        self.status = 'healthy'

    def attack(self, enemy: 'monster'):
        enemy.defend(self.attack_point)

    def defend(self, enemy_ap: int):
        self.hit_point -= enemy_ap
        if self.hit_point <= 0:
            self.status = 'dead'

    def is_alive(self) -> bool:
        return not self.is_dead()

    def is_dead(self) -> bool:
        return self.status == 'dead'
def answer(t_hp: int, t_ap: int, a_hp: int, a_ap: int) -> str:
    taka_monster = monster(t_hp, t_ap)
    aoki_monster = monster(a_hp, a_ap)
    while taka_monster.is_alive() and aoki_monster.is_alive():
        taka_monster.attack(aoki_monster)
        if aoki_monster.is_dead():
            return 'Yes'
        aoki_monster.attack(taka_monster)
        if taka_monster.is_dead():
            return 'No'
def main():
    a, b, c, d = map(int, input().split())
    print(answer(a, b, c, d))

def wrapped_artificially():
    if __name__ == '__main__':
        main()


if __name__ == "__main__":
    wrapped_artificially()
