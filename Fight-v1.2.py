# -*- coding: utf-8 -*-
__author__ = 'Skyeyes'


class Data:
    __role = ["Common", "Soldier", "Hero"]

    class Player:
        def __init__(self, name, ATK, DEF, HP, ROLE):
            self.__name = name
            self.__ATK = ATK
            self.__DEF = DEF
            self.__HP = HP
            self.__ROLE = ROLE

        def get_hurt(self, other_atk):
            get_hurt = max(other_atk - self.__DEF, 0)
            return get_hurt

        def hp_lose(self, other_atk):
            hurt = min(self.get_hurt(other_atk), self.__HP)
            self.__HP -= hurt
            return hurt

        def get_name(self):
            return self.__name

        def get_atk(self):
            return self.__ATK

        def get_def(self):
            return self.__DEF

        def get_hp(self):
            return self.__HP

        def get_role(self):
            return self.__ROLE

    def getrole(self, number):
        return self.__role[number]


# noinspection PyArgumentList
class GameFlow:
    __name = []
    __atk = []
    __def = []
    __hp = []
    __rolenum = []

    def get_input(self, player_num):
        self.__name.append(input("player" + str(player_num + 1) + "'s name: "))
        self.__atk.append(int(input("player" + str(player_num + 1) + "'s atk: ")))
        self.__def.append(int(input("player" + str(player_num + 1) + "'s def: ")))
        self.__hp.append(int(input("player" + str(player_num + 1) + "'s hp: ")))
        self.__rolenum.append(int(input("player" + str(player_num + 1) + "'s role(1.Common  2.Soldier  3.Hero): ")))

    def create_player(self):
        self.get_input(0)
        self.get_input(1)
        return Data.Player(self.__name[0], self.__atk[0], self.__def[0], self.__hp[0], Data.getrole(self.__rolenum[0])), \
               Data.Player(self.__name[1], self.__atk[1], self.__def[1], self.__hp[1], Data.getrole(self.__rolenum[1]))


class View:
    __player1, __player2 = GameFlow().create_player()

    def print_template(self, player_1, player_2):
        hurt = player_2.hp_lose(player_1.get_atk())
        if hurt == 0:
            print(player_1.get_name() + " can't hurt " + player_2.get_name())
        elif player_1.get_role() == "Common":
            print(player_1.get_name() + " attack " + player_2.get_name() + ", " +
                  player_2.get_name() + " get " + str(
                  hurt) + " point hurt, " +
                  player_2.get_name() + "'s hp: " + str(player_2.get_hp()))
        else:
            print(player_1.get_role() + " " + player_1.get_name() + " attack " + player_2.get_name() + ", " +
                  player_2.get_name() + " get " + str(
                  hurt) + " point hurt, " +
                  player_2.get_name() + "'s hp: " + str(player_2.get_hp()))

    def judge_winner(self):
        if self.__player1.get_hp() == 0:
            print(self.__player2.get_name() + " win!")
        elif self.__player2.get_hp() == 0:
            print(self.__player1.get_name() + " win!")

    def Game_print(self):
        i = 0
        while True:
            if self.__player1.get_hurt(self.__player2.get_atk()) == 0 and self.__player2.get_hurt(
                    self.__player1.get_atk()) == 0:
                print("Each player can't hurt other one!")
                break
            while True:
                if i % 2 == 0:
                    if self.__player1.get_hp() != 0:
                        self.print_template(self.__player1, self.__player2)
                        self.judge_winner()
                    else:
                        break
                else:
                    if self.__player2.get_hp() != 0:
                        self.print_template(self.__player2, self.__player1)
                        self.judge_winner()
                    else:
                        break
                i += 1


def main():
    View().Game_print()

if __name__ == "__main__":
    main()
