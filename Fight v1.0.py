# -*- coding: utf-8 -*-
__author__ = 'Skyeyes'


class Player:
    def __init__(self, name, ATK, HP):
        self.name = name
        self.ATK = ATK
        self.HP = HP

    def get_hurt(self, other_atk):
        atk = other_atk
        hp = self.HP
        hurt = min(atk, hp)
        self.HP -= hurt
        return hurt


def print_mes(a, b):
    hurt = b.get_hurt(a.ATK)
    print(str(a.name) + "攻击" + str(b.name) + ", " + str(b.name) + "收到" + str(hurt) + "点伤害，" + str(
        b.name) + "剩余生命值：" + str(b.HP))


def judge_winner(a, b):
    if a.HP == 0:
        print(str(b.name) + "获胜")
    else:
        print(str(a.name) + "获胜")


def print_all():
    name1 = input("角色1的名称：")
    atk1 = int(input("角色1的攻击："))
    hp1 = int(input("角色1的生命值："))
    player1 = Player(name1, atk1, hp1)
    name1 = input("角色2的名称：")
    atk1 = int(input("角色2的攻击："))
    hp1 = int(input("角色2的生命值："))
    player2 = Player(name1, atk1, hp1)
    i = 0
    while True:
        if i % 2 == 0:
            if player1.HP != 0:
                print_mes(player1, player2)
            else:
                break
        else:
            if player2.HP != 0:
                print_mes(player2, player1)
            else:
                break
        i += 1

    judge_winner(player1, player2)


print_all()



