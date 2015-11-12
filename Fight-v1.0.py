__author__ = 'Skyeyes'


class Player:
    def __init__(self, name, ATK, HP):
        self.__name = name
        self.__ATK = ATK
        self.__HP = HP

    def get_hurt(self, other_atk):
        atk = other_atk
        hp = self.__HP
        hurt = min(atk, hp)
        self.__HP -= hurt
        return hurt

    def get_name(self):
        return self.__name

    def get_atk(self):
        return self.__ATK

    def get_hp(self):
        return self.__HP


class GameFlow:
    __name = []
    __atk = []
    __hp = []

    def get_input(self, player_num):
        self.__name.append(input("player" + str(player_num + 1) + "'s name: "))
        self.__atk.append(int(input("player" + str(player_num + 1) + "'s atk: ")))
        self.__hp.append(int(input("player" + str(player_num + 1) + "'s hp: ")))

    def create_player(self):
        self.get_input(0)
        self.get_input(1)
        return Player(self.__name[0], self.__atk[0], self.__hp[0]), \
               Player(self.__name[1], self.__atk[1], self.__hp[1])


class View:
    __player1, __player2 = GameFlow().create_player()

    def print_template(self, player_1, player_2):
        hurt = player_2.get_hurt(player_1.get_atk())
        print(player_1.get_name() + " attack " + player_2.get_name() + ", " +
              player_2.get_name() + " get " + str(
            hurt) + " point hurt, " +
              player_2.get_name() + "'s hp: " + str(player_2.get_hp()))

    def judge_winner(self):
        if self.__player1.get_hp() == 0:
            print(self.__player2.get_name() + " win")
        elif self.__player2.get_hp() == 0:
            print(self.__player1.get_name() + " win")

    def Game_print(self):
        i = 0
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
