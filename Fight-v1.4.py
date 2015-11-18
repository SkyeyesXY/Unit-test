# -*- coding: utf-8 -*-
__author__ = 'Skyeyes'

class Player:
    def __init__(self, args):
        self.__name, self.__atk, self.__def, self.__hp, self.__role, self.__weapon, self.__weaponatk, self.__shield = args

    def get_hurt(self, other_atk, otherweaponatk):
        hurt = max(other_atk + otherweaponatk - self.__def - int(self.__shield), 0)
        hurt = min(hurt, self.__hp)
        return hurt

    def hp_lose(self, other_atk, otherweaponatk):
        hurt = self.get_hurt(other_atk, otherweaponatk)
        self.__hp -= hurt
        return hurt

    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__atk

    def get_hp(self):
        return self.__hp

    def reply_hp(self, hp):
        self.__hp = hp

    def get_role(self):
        return self.__role

    def get_weaponname(self):
        return self.__weapon

    def get_weaponatk(self):
        return self.__weaponatk


class View:
    outputtable = []  # 输出表，记录玩家的输出顺序
    draw = False
    player1 = 0
    player2 = 0

    def get_input(self, player_num):
        name = input("player" + str(player_num ) + "'s name: ")
        atk = int(input("player" + str(player_num ) + "'s atk: "))
        defence = int(input("player" + str(player_num) + "'s def: "))
        hp = int(input("player" + str(player_num) + "'s hp: "))
        role = input("player" + str(player_num) + "'s role(no role input 'n'): ")
        if role != "n":
            weapon = input("player" + str(player_num) + "'s weapon is(if don't need weapon input 'n'): ")
            if weapon != "n":
                weaponatk = int(input("player" + str(player_num) + "'s weaponapk is: "))
            else:
                weaponatk = "n"
            choose_shield = input("do you need a shield(y/n): ")
            if choose_shield == "y":
                shield = int(input("you shield's def is: "))
            else:
                shield = 0
        else:
            weaponatk = 0
            weapon = "n"
            shield = 0
        return name, atk, defence, hp, role, weapon, weaponatk, shield


    def print_template(self, player_1, player_2):
        hurt = player_2.hp_lose(player_1.get_atk(), player_1.get_weaponatk())
        if hurt == 0:                   #这只是对输出的模板的判断和游戏过程并没有联系，不是所有的判断都叫过程判断
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



class Game:

    def control(self, view):        #创造玩家，进行输出顺序判断的游戏过程控制
        View.player1 = Player((view.get_input(0)))
        View.player2 = Player((view.get_input(1)))
        hpcopy1 = view.player1.get_hp()         #记录预执行前的血量
        hpcopy2 = view.player2.get_hp()
        if view.player1.get_hurt(view.player2.get_atk(), view.player1.get_weaponatk()) == 0 and view.player2.get_hurt(view.player1.get_atk(), view.player1.get_weaponatk()) == 0:
                view.draw = True  # draw：平局
        else:
            flag = 0#判断输出顺序的标记
            while True:
                if flag % 2 == 0:
                    view.player2.hp_lose(view.player1.get_atk(), view.player1.get_weaponatk())
                    view.outputtable.append(1)  # 轮到玩家1输出则输出表记录1
                    if view.player2.get_hp() == 0:
                        view.outputtable.append(3)  # 若玩家1胜利记录3
                        break
                else:
                    view.player1.hp_lose(view.player2.get_atk(), view.player2.get_weaponatk())
                    view.outputtable.append(2)  # 轮到玩家2输出则输出表记录2
                    if view.player1.get_hp() == 0:
                        view.outputtable.append(4)  # 若玩家2胜利记录4
                        break
                flag += 1
        view.player1.reply_hp(hpcopy1)
        view.player2.reply_hp(hpcopy2)

    def start(self, view):
        self.control(view)
        view.game_print()



def main():
    view = View()
    Game().start(view)


if __name__ == "__main__":
    main()
