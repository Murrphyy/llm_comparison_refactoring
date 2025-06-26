class Monster:

    def __init__(self, hp, attack):
        self.hp = hp
        self.attack = attack
        self.death = False
def battle(monster1, monster2):
    monster2.hp -= monster1.attack
    if monster2.hp <= 0:
        monster2.death = True
    return monster2.death

def wrapped_artificially():
    a, b, c, d = map(int, input().split())
    t_monster = Monster(a, b)
    a_monster = Monster(c, d)
    while True:
        result = battle(t_monster, a_monster)
        if result:
            print('Yes')
            break
        result = battle(a_monster, t_monster)
        if result:
            print('No')
            break


if __name__ == "__main__":
    wrapped_artificially()
