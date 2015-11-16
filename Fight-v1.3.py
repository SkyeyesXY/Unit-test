# -*- coding: utf-8 -*-
__author__ = 'Skyeyes'


class Player:
    def __init__(self, name="", atk=0, defence=0, hp=0, role="", weapon=0):
        self.__name = name
        self.__atk = atk
        self.__def = defence
        self.__hpcopy = self.__hp = hp
        self.__role = role
        self.__weapon = weapon

    def get_hurt(self, other_atk):
        hurt = max(other_atk - self.__def, 0)
        hurt = min(hurt, self.__hp)
        return hurt

    def hp_losecopy(self, other_atk):
        hurt = max(other_atk - self.__def, 0)
        hurt = min(hurt, self.__hpcopy)
        self.__hpcopy -= hurt
        return hurt

    def hp_lose(self, other_atk):
        hurt = max(other_atk - self.__def, 0)
        hurt = min(hurt, self.__hp)
        self.__hp -= hurt
        return hurt

    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__atk

    def get_def(self):
        return self.__def

    def get_hp(self):
        return self.__hp

    def get_hpcopy(self):
        return self.__hpcopy

    def get_role(self):
        return self.__role

    def get_weaponname(self):
        return self.__weapon


class View:
    outputtable = []  # 输出表，记录玩家的输出顺序
    draw = False
    name = ""
    atk = 0
    defence = 0
    hp = 0
    role = ""
    weapon = ""
    player1 = Player()
    player2 = Player()

    def get_input(self, player_num):
        self.name = input("player" + str(player_num + 1) + "'s name: ")
        self.atk = int(input("player" + str(player_num + 1) + "'s atk: "))
        self.defence = int(input("player" + str(player_num + 1) + "'s def: "))
        self.hp = int(input("player" + str(player_num + 1) + "'s hp: "))
        self.role = input("player" + str(player_num + 1) + "'s role(no role input 'n'): ")
        if self.role != "n":
            self.weapon = input("player" + str(player_num + 1) + "'s weapon is(if don't need weapon input 'n'): ")

    def print_template(self, player_1, player_2):
        hurt = player_2.hp_lose(player_1.get_atk())
        if hurt == 0:
            print(player_1.get_name() + " can't hurt " + player_2.get_name())
        elif player_1.get_role() == "n":
            print(player_1.get_name() + " attack " + player_2.get_name() + ", " +
                  player_2.get_name() + " get " + str(
                hurt) + " point hurt, " +
                  player_2.get_name() + "'s hp: " + str(player_2.get_hp()))
        elif player_1.get_weaponname() == "n":
            print(player_1.get_role() + " " + player_1.get_name() + " attack " + player_2.get_name() + ", " +
                player_2.get_name() + " get " + str(
                    hurt) + " point hurt, " +
                player_2.get_name() + "'s hp: " + str(player_2.get_hp()))
        else:
            print(player_1.get_role() + " " + player_1.get_name() + " use " + player_1.get_weaponname() + " attack " + player_2.get_name() + ", " +
                player_2.get_name() + " get " + str(
                    hurt) + " point hurt, " +
                player_2.get_name() + "'s hp: " + str(player_2.get_hp()))

    def game_print(self):
        if self.draw == True:
            print("Each player can't hurt other one!")
        else:               #按照游戏输出表的内容输出
            for i in self.outputtable:
                if i == 1:
                    self.print_template(self.player1, self.player2)
                elif i == 2:
                    self.print_template(self.player2, self.player1)
                elif i == 3:
                    print(self.player1.get_name() + " win!")
                elif i == 4:
                    print(self.player2.get_name() + " win!")



def Game(View):
    View.get_input(0)
    View.player1 = Player(View.name, View.atk, View.defence, View.hp, View.role, View.weapon)
    View.get_input(1)
    View.player2 = Player(View.name, View.atk, View.defence, View.hp, View.role, View.weapon)
    if View.player1.get_hurt(View.player2.get_atk()) == 0 and View.player2.get_hurt(View.player1.get_atk()) == 0:
            View.draw = True  # draw：平局
    else:
        flag = 0#判断输出顺序的标记
        while True:
            if flag % 2 == 0:
                View.player2.hp_losecopy(View.player1.get_atk())
                View.outputtable.append(1)  # 轮到玩家1输出则输出表记录1
                if View.player2.get_hpcopy() == 0:
                    View.outputtable.append(3)  # 若玩家1胜利记录3
                    break
            else:
                View.player1.hp_losecopy(View.player2.get_atk())
                View.outputtable.append(2)  # 轮到玩家2输出则输出表记录2
                if View.player1.get_hpcopy() == 0:
                    View.outputtable.append(4)  # 若玩家2胜利记录4
                    break
            flag += 1



def main():
    view = View()
    Game(view)
    view.game_print()


if __name__ == "__main__":
    main()
