# -*- coding: utf-8 -*-
__author__ = 'Skyeyes'


class Data:
    role = ["Common", "Soldier", "Hero"]
    weapon = {0: ["None", 0], 1: ["Stick", 1], 2: ["Sword", 3], 3:["Spear", 5], }


    class Weapon:
        def __init__(self, name, atk):
            self.__name = name
            self.__atk = atk

        def get_name(self):
            return self.__name

        def get_atk(self):
            return self.__atk


    class Player:
        def __init__(self, name, atk, defence, hp, role, weapon = 0):
            self.__name = name
            self.__atk = atk
            self.__def = defence
            self.__hp = hp
            self.__role = eole
            self.__weapon = Data.Weapon(Data.weapon[weapon][0], Data.weapon[weapon][1])

        def get_hurt(self, other_atk, other_weapon):
            get_hurt = max(other_atk + other_weapon - self.__def, 0)
            return get_hurt

        def hp_lose(self, other_atk, other_weapon):
            hurt = min(self.get_hurt(other_atk, other_weapon), self.__hp)
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

        def get_role(self):
            return self.__role

        def get_weaponname(self):
            return self.__weapon.get_name()

        def get_weaponatk(self):
            return self.__weapon.get_atk()


class GameFlow:
    __name = 0
    __atk = 0
    __def = 0
    __hp = 0
    __rolenum = 0
    __weaponnum = 0

    def get_input(self, player_num):
        self.__name = input("player" + str(player_num + 1) + "'s name: ")
        self.__atk = int(input("player" + str(player_num + 1) + "'s atk: "))
        self.__def = int(input("player" + str(player_num + 1) + "'s def: "))
        self.__hp = int(input("player" + str(player_num + 1) + "'s hp: "))
        self.__rolenum = int(input("player" + str(player_num + 1) + "'s role(1.Common  2.Soldier  3.Hero): ")) - 1
        if self.__rolenum[player_num] == 0:
            self.__weaponnum = 0
        else:
            self.__weaponnum = int(input("player" + str(player_num + 1) + "'s weapon is(1.Stick  2.Sword  3.Spear): "))

    def create_player1(self):
        self.get_input(0)

        return Data.Player(self.__name, self.__atk, self.__def, self.__hp, Data.role[self.__rolenum], self.__weaponnum), \

    def create_palyer2(self):
        self.get_input(1)
        Data.Player(self.__name, self.__atk, self.__def, self.__hp, Data.role[self.__rolenum], self.__weaponnum), \


class View:
    __player1, __player2 = GameFlow().create_player()

    def print_template(self, player_1, player_2):
        hurt = player_2.hp_lose(player_1.get_atk(), player_2.get_weaponatk())
        if hurt == 0:
            print(player_1.get_name() + " can't hurt " + player_2.get_name())
        elif player_1.get_role() == "Common":
            print(player_1.get_name() + " attack " + player_2.get_name() + ", " +
                  player_2.get_name() + " get " + str(
                  hurt) + " point hurt, " +
                  player_2.get_name() + "'s hp: " + str(player_2.get_hp()))
        else:
            print(player_1.get_role() + " " + player_1.get_name() +"use" +player_1.get_weaponname() + " attack " + player_2.get_name() + ", " +
                  player_2.get_name() + " get " + str(
                  hurt) + " point hurt, " +
                  player_2.get_name() + "'s hp: " + str(player_2.get_hp()))

    def print_winner(self):
        if self.__player1.get_hp() == 0:
            print(self.__player2.get_name() + " win!")
        elif self.__player2.get_hp() == 0:
            print(self.__player1.get_name() + " win!")

    def Game(self):
        i = 0
        while True:
            if self.__player1.get_hurt(self.__player2.get_atk(), self.__player2.get_weaponatk()) == 0 and self.__player2.get_hurt(
                    self.__player1.get_atk(), self.__player1.get_weaponatk()) == 0:
                print("Each player can't hurt other one!")
                break
            while True:
                if i % 2 == 0:
                    if self.__player1.get_hp() != 0:
                        self.print_template(self.__player1, self.__player2)
                        self.print_winner()
                    else:
                        break
                else:
                    if self.__player2.get_hp() != 0:
                        self.print_template(self.__player2, self.__player1)
                        self.print_winner()
                    else:
                        break
                i += 1


def main():
    View().Game()

if __name__ == "__main__":
    main()