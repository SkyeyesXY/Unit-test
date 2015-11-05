# -*- coding: utf-8 -*-
__author__ = 'Skyeyes'


class Player:
    def __init__(self, name, ATK, DEF, HP):
        self.name = name
        self.ATK = ATK
        self.DEF = DEF
        self.HP = HP

    def get_hurt(self, other_atk):
        get_hurt = max(other_atk - self.DEF, 0)
        return get_hurt

    def hp_lose(self, other_atk):
        hurt = min(self.get_hurt(other_atk), self.HP)
        self.HP -= hurt
        return hurt


def print_mes(a, b):
    hurt = b.hp_lose(a.ATK)
    if hurt == 0:
        print(a.name + "不能对" + b.name + "造成伤害！" + "攻击无效！")
    else:
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
    def1 = int(input("角色1的防御："))
    hp1 = int(input("角色1的生命值："))
    player1 = Player(name1, atk1, def1, hp1)
    name1 = input("角色2的名称：")
    atk1 = int(input("角色2的攻击："))
    def2 = int(input("角色2的防御："))
    hp1 = int(input("角色2的生命值："))
    player2 = Player(name1, atk1, def2, hp1)
    i = 0
    while True:
        if player1.get_hurt(player2.ATK) == 0 and player2.get_hurt(player1.ATK) == 0:
            print("双方攻击无效！")
            break
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
        break


print_all()

